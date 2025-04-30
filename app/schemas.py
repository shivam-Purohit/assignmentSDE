from datetime import date, datetime
from pydantic import BaseModel
from typing import List, Optional

class UserBase(BaseModel):
    email: str
    full_name: Optional[str]

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    created_at: datetime

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None

class ActivityBase(BaseModel):
    name: str
    description: Optional[str]
    duration_hours: Optional[float]
    category: Optional[str]
    cost: Optional[float]  # ✅ NEW

class Activity(ActivityBase):
    pass

class TransferBase(BaseModel):
    type: str
    departure_time: datetime
    arrival_time: datetime
    duration_minutes: int
    vehicle_type: str

class Transfer(TransferBase):
    pass

class HotelBase(BaseModel):
    name: str
    address: Optional[str]
    rating: Optional[float]
    checkin_time: datetime
    checkout_time: datetime
    cost: Optional[float]  # ✅ NEW

class Hotel(HotelBase):
    pass

class DayBase(BaseModel):
    day_number: int
    date: Optional[date]
    hotels: List[Hotel] = []
    transfers: List[Transfer] = []
    activities: List[Activity] = []

class Day(DayBase):
    pass

class ItineraryBase(BaseModel):
    name: str
    duration: int
    region: str
    description: Optional[str]

class ItineraryCreate(ItineraryBase):
    days: List[DayBase]

class ReviewBase(BaseModel):
    rating: float
    comment: Optional[str]

class ReviewCreate(ReviewBase):
    itinerary_id: int

class Review(ReviewBase):
    id: int
    user: User
    created_at: datetime

    class Config:
        orm_mode = True

class Itinerary(ItineraryBase):
    id: int
    popularity: int
    is_recommended: bool
    created_at: datetime
    days: List[Day]
    reviews: List[Review] = []

    # ✅ NEW: Derived fields for AI-friendly output
    overall_cost: Optional[float] = 0.0
    avg_rating: Optional[float] = 0.0

    class Config:
        orm_mode = True

# Fix forward reference
Itinerary.update_forward_refs()
