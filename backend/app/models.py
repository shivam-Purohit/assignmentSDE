from datetime import datetime
from sqlalchemy import Boolean, Column, Date, DateTime, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    reviews = relationship("Review", back_populates="user")

class Itinerary(Base):
    __tablename__ = "itineraries"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    duration = Column(Integer, nullable=False)
    region = Column(String(50), nullable=False)
    description = Column(Text)
    popularity = Column(Integer, default=0)
    is_recommended = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    days = relationship("Day", back_populates="itinerary", cascade="all, delete-orphan")
    reviews = relationship("Review", back_populates="itinerary")

class Day(Base):
    __tablename__ = "days"
    id = Column(Integer, primary_key=True, index=True)
    itinerary_id = Column(Integer, ForeignKey("itineraries.id"), nullable=False)
    day_number = Column(Integer, nullable=False)
    date = Column(Date)
    itinerary = relationship("Itinerary", back_populates="days")
    hotels = relationship("Hotel", back_populates="day")
    transfers = relationship("Transfer", back_populates="day")
    activities = relationship("Activity", back_populates="day")

class Hotel(Base):
    __tablename__ = "hotels"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    address = Column(String(200))
    rating = Column(Float)
    checkin_time = Column(DateTime)
    checkout_time = Column(DateTime)
    cost = Column(Float, default=0.0)  # ✅ NEW
    day_id = Column(Integer, ForeignKey("days.id"))
    day = relationship("Day", back_populates="hotels")

class Transfer(Base):
    __tablename__ = "transfers"
    id = Column(Integer, primary_key=True, index=True)
    type = Column(String(50), nullable=False)
    departure_time = Column(DateTime)
    arrival_time = Column(DateTime)
    duration_minutes = Column(Integer)
    vehicle_type = Column(String(50))
    day_id = Column(Integer, ForeignKey("days.id"))
    day = relationship("Day", back_populates="transfers")

class Activity(Base):
    __tablename__ = "activities"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    duration_hours = Column(Float)
    category = Column(String(50))
    cost = Column(Float, default=0.0)  # ✅ NEW
    day_id = Column(Integer, ForeignKey("days.id"))
    day = relationship("Day", back_populates="activities")

class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True, index=True)
    rating = Column(Float, nullable=False)
    comment = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    itinerary_id = Column(Integer, ForeignKey("itineraries.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    itinerary = relationship("Itinerary", back_populates="reviews")
    user = relationship("User", back_populates="reviews")
