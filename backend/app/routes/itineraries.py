from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from app.schemas import ItineraryCreate, Itinerary
from app.models import Itinerary as ItineraryModel
from app.database import get_db
from app.dependencies.auth import get_current_user

router = APIRouter()

@router.post(
    "/itineraries",
    response_model=Itinerary,
    status_code=status.HTTP_201_CREATED,
    operation_id="create_itinerary",
    tags=["itinerary"],
    summary="Create a new itinerary",
    description="Create a new travel itinerary with day-wise details. Requires authentication."
)
def create_itinerary(
    itinerary: ItineraryCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    """
    Create a new itinerary.
    """
    db_itinerary = ItineraryModel(
        name=itinerary.name,
        duration=itinerary.duration,
        region=itinerary.region,
        description=itinerary.description,
    )
    db.add(db_itinerary)
    db.commit()
    db.refresh(db_itinerary)
    # TODO: Add days and nested hotels, transfers, activities here
    return db_itinerary

@router.get(
    "/itineraries/{itinerary_id}",
    response_model=Itinerary,
    operation_id="get_itinerary",
    tags=["itinerary"],
    summary="Get itinerary by ID",
    description="Retrieve a specific itinerary by its ID."
)
def get_itinerary(
    itinerary_id: int,
    db: Session = Depends(get_db)
):
    """
    Get a specific itinerary by its ID.
    """
    itinerary = db.query(ItineraryModel).filter(ItineraryModel.id == itinerary_id).first()
    if not itinerary:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Itinerary not found")
    return itinerary

@router.get(
    "/itineraries",
    response_model=list[Itinerary],
    operation_id="list_itineraries",
    tags=["itinerary"],
    summary="List itineraries",
    description="List all itineraries, optionally filtering by region and duration."
)
def list_itineraries(
    region: str = Query(None, description="Region to filter by"),
    duration: int = Query(None, description="Duration in nights to filter by"),
    db: Session = Depends(get_db)
):
    """
    List all itineraries, optionally filtered by region and/or duration.
    """
    query = db.query(ItineraryModel)
    if region:
        query = query.filter(ItineraryModel.region == region)
    if duration:
        query = query.filter(ItineraryModel.duration == duration)
    return query.all()
