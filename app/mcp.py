from fastapi import APIRouter
from typing import List
from app import schemas

router = APIRouter()

# Recommended itineraries for given number of nights
@router.get("/mcp/{nights}", response_model=List[schemas.Itinerary])
def get_recommended_itineraries(nights: int):
    # Example logic for recommending itineraries
    # You can improve this logic to match your actual recommendation logic
    return [{"id": 1, "name": f"Recommended Itinerary for {nights} Nights", "duration": nights, "days": []}]
