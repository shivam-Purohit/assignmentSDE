from pydantic import BaseModel
from typing import List, Optional

class HotelBase(BaseModel):
    name: str
    address: str
    price: float

class HotelCreate(HotelBase):
    pass

class Hotel(HotelBase):
    id: int
    day_id: int

    class Config:
        orm_mode = True

class ActivityBase(BaseModel):
    name: str
    description: str
    price: float

class ActivityCreate(ActivityBase):
    pass

class Activity(ActivityBase):
    id: int
    day_id: int

    class Config:
        orm_mode = True

class TransferBase(BaseModel):
    type: str
    from_location: str
    to_location: str
    price: float

class TransferCreate(TransferBase):
    pass

class Transfer(TransferBase):
    id: int
    day_id: int

    class Config:
        orm_mode = True

class DayBase(BaseModel):
    itinerary_id: int
    day_number: int
    date: str

class DayCreate(DayBase):
    hotels: List[HotelCreate] = []
    activities: List[ActivityCreate] = []
    transfers: List[TransferCreate] = []

class Day(DayBase):
    id: int
    hotels: List[Hotel] = []
    activities: List[Activity] = []
    transfers: List[Transfer] = []

    class Config:
        orm_mode = True

class ItineraryBase(BaseModel):
    name: str
    duration: int  # Duration in nights

class ItineraryCreate(ItineraryBase):
    days: List[DayCreate] = []

class Itinerary(ItineraryBase):
    id: int
    days: List[Day] = []

    class Config:
        orm_mode = True
