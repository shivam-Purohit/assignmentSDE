from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Itinerary(Base):
    __tablename__ = "itineraries"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    duration = Column(Integer)  # Duration in nights

    # Relationships
    days = relationship("Day", back_populates="itinerary")

class Day(Base):
    __tablename__ = "days"
    id = Column(Integer, primary_key=True, index=True)
    itinerary_id = Column(Integer, ForeignKey("itineraries.id"))
    day_number = Column(Integer)
    date = Column(String)

    # Relationships
    itinerary = relationship("Itinerary", back_populates="days")
    hotels = relationship("Hotel", back_populates="day")
    transfers = relationship("Transfer", back_populates="day")
    activities = relationship("Activity", back_populates="day")

class Hotel(Base):
    __tablename__ = "hotels"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    address = Column(String)
    price = Column(Float)
    day_id = Column(Integer, ForeignKey("days.id"))

    # Relationships
    day = relationship("Day", back_populates="hotels")

class Transfer(Base):
    __tablename__ = "transfers"
    id = Column(Integer, primary_key=True, index=True)
    type = Column(String)  # E.g., Flight, Car, etc.
    from_location = Column(String)
    to_location = Column(String)
    price = Column(Float)
    day_id = Column(Integer, ForeignKey("days.id"))

    # Relationships
    day = relationship("Day", back_populates="transfers")

class Activity(Base):
    __tablename__ = "activities"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    day_id = Column(Integer, ForeignKey("days.id"))

    # Relationships
    day = relationship("Day", back_populates="activities")
