from fastapi import APIRouter, Query, Depends
from sqlalchemy.orm import Session
from app.models import Itinerary as ItineraryModel
from app.schemas import Itinerary
from app.database import get_db

router = APIRouter()

@router.get(
    "/mcp/recommend",
    response_model=list[Itinerary],
    operation_id="recommend_itineraries",
    tags=["recommendation"],
    summary="Get recommended itineraries",
    description="""
    Returns recommended itineraries for a given number of nights and region.
    You can choose how to rank the results: by cost, popularity, review rating, or a weighted combination of all.
    This API is AI-agent friendly and allows you to customize your preferences via query parameters.
    """
)
def recommend_itineraries(
    nights: int = Query(..., gt=0, description="Number of nights in the itinerary"),
    region: str = Query(None, description="Optional region to filter itineraries"),
    sort_by: str = Query("combined", enum=["rating", "popularity", "cost", "combined"], description="Sort strategy: rating, popularity, cost, or a weighted combination"),
    weight_rating: float = Query(0.5, ge=0, le=1, description="Weight for rating (used if sort_by=combined)"),
    weight_popularity: float = Query(0.3, ge=0, le=1, description="Weight for popularity (used if sort_by=combined)"),
    weight_cost: float = Query(0.2, ge=0, le=1, description="Weight for cost (used if sort_by=combined; lower cost is better)"),
    db: Session = Depends(get_db)
):
    query = db.query(ItineraryModel).filter(ItineraryModel.is_recommended == True)
    if region:
        query = query.filter(ItineraryModel.region == region)
    query = query.filter(ItineraryModel.duration == nights)
    itineraries = query.all()

    for itinerary in itineraries:
        # Compute average rating
        reviews = getattr(itinerary, "reviews", [])
        itinerary.avg_rating = sum(r.rating for r in reviews) / len(reviews) if reviews else 0

        # Compute cost: sum activity and hotel costs
        cost = 0
        for day in itinerary.days:
            cost += sum(hotel.cost or 0 for hotel in day.hotels)
            cost += sum(activity.cost or 0 for activity in day.activities)
        itinerary.overall_cost = cost

    # Normalize
    max_rating = max((i.avg_rating for i in itineraries), default=1)
    max_popularity = max((i.popularity for i in itineraries), default=1)
    max_cost = max((i.overall_cost for i in itineraries), default=1)

    def combined_score(itinerary):
        return (
            weight_rating * (itinerary.avg_rating / max_rating) +
            weight_popularity * (itinerary.popularity / max_popularity) +
            weight_cost * (1 - itinerary.overall_cost / max_cost)  # lower cost = higher score
        )

    # Sorting
    if sort_by == "rating":
        ranked = sorted(itineraries, key=lambda i: i.avg_rating, reverse=True)
    elif sort_by == "popularity":
        ranked = sorted(itineraries, key=lambda i: i.popularity, reverse=True)
    elif sort_by == "cost":
        ranked = sorted(itineraries, key=lambda i: i.overall_cost)
    else:
        ranked = sorted(itineraries, key=combined_score, reverse=True)

    return ranked
