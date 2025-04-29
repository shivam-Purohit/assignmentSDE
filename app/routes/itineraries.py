from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import models, schemas
from app.database import get_db

router = APIRouter()

# Create a new itinerary
@router.post("/itineraries/", response_model=schemas.Itinerary)
def create_itinerary(itinerary: schemas.ItineraryCreate, db: Session = Depends(get_db)):
    db_itinerary = models.Itinerary(name=itinerary.name, duration=itinerary.duration)
    db.add(db_itinerary)
    db.commit()
    db.refresh(db_itinerary)
    # Add days and associated data
    for day in itinerary.days:
        db_day = models.Day(itinerary_id=db_itinerary.id, day_number=day.day_number, date=day.date)
        db.add(db_day)
        db.commit()
        db.refresh(db_day)
        for hotel in day.hotels:
            db_hotel = models.Hotel(name=hotel.name, address=hotel.address, price=hotel.price, day_id=db_day.id)
            db.add(db_hotel)
        for activity in day.activities:
            db_activity = models.Activity(name=activity.name, description=activity.description, price=activity.price, day_id=db_day.id)
            db.add(db_activity)
        for transfer in day.transfers:
            db_transfer = models.Transfer(type=transfer.type, from_location=transfer.from_location, to_location=transfer.to_location, price=transfer.price, day_id=db_day.id)
            db.add(db_transfer)
        db.commit()
    return db_itinerary

# Get all itineraries
@router.get("/itineraries/", response_model=List[schemas.Itinerary])
def get_itineraries(db: Session = Depends(get_db)):
    return db.query(models.Itinerary).all()
