from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import ReviewCreate, Review
from app.models import Review as ReviewModel, Itinerary as ItineraryModel
from app.database import get_db
from app.dependencies.auth import get_current_user

router = APIRouter()

@router.post("/reviews", response_model=Review)
def create_review(
    review: ReviewCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    itinerary = db.query(ItineraryModel).filter(ItineraryModel.id == review.itinerary_id).first()
    if not itinerary:
        raise HTTPException(status_code=404, detail="Itinerary not found")
    db_review = ReviewModel(
        itinerary_id=review.itinerary_id,
        user_id=current_user.id,
        rating=review.rating,
        comment=review.comment
    )
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review

@router.get("/itineraries/{itinerary_id}/reviews", response_model=list[Review])
def list_reviews(itinerary_id: int, db: Session = Depends(get_db)):
    return db.query(ReviewModel).filter(ReviewModel.itinerary_id == itinerary_id).all()
