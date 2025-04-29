from app.database import SessionLocal, engine
from app import models

# Create tables in the database
models.Base.metadata.create_all(bind=engine)

# Seed data for Phuket and Krabi
def seed_data():
    db = SessionLocal()

    # Sample Phuket itinerary (3 days)
    phuket_itinerary = models.Itinerary(name="Phuket 3-Day Tour", duration=3)
    db.add(phuket_itinerary)
    db.commit()
    db.refresh(phuket_itinerary)

    # Day 1 (Phuket) - Arrival & Hotel
    day1 = models.Day(itinerary_id=phuket_itinerary.id, day_number=1, date="2025-05-01")
    db.add(day1)
    db.commit()
    db.refresh(day1)

    # Sample hotel, activity, and transfer for Day 1
    hotel1 = models.Hotel(name="Phuket Beach Resort", address="Patong Beach, Phuket", price=120.0, day_id=day1.id)
    db.add(hotel1)

    activity1 = models.Activity(name="Beach Relaxation", description="Relax on Patong Beach", price=0.0, day_id=day1.id)
    db.add(activity1)

    transfer1 = models.Transfer(type="Car", from_location="Phuket Airport", to_location="Phuket Beach Resort", price=30.0, day_id=day1.id)
    db.add(transfer1)

    # Day 2 (Phuket) - Sightseeing
    day2 = models.Day(itinerary_id=phuket_itinerary.id, day_number=2, date="2025-05-02")
    db.add(day2)
    db.commit()
    db.refresh(day2)

    hotel2 = models.Hotel(name="Patong Paradise Hotel", address="Patong Beach, Phuket", price=150.0, day_id=day2.id)
    db.add(hotel2)

    activity2 = models.Activity(name="Phi Phi Islands Tour", description="Day tour to Phi Phi Islands", price=80.0, day_id=day2.id)
    db.add(activity2)

    transfer2 = models.Transfer(type="Boat", from_location="Patong Beach", to_location="Phi Phi Islands", price=40.0, day_id=day2.id)
    db.add(transfer2)

    # Day 3 (Phuket) - Departure
    day3 = models.Day(itinerary_id=phuket_itinerary.id, day_number=3, date="2025-05-03")
    db.add(day3)
    db.commit()
    db.refresh(day3)

    hotel3 = models.Hotel(name="Phuket Beach Resort", address="Patong Beach, Phuket", price=120.0, day_id=day3.id)
    db.add(hotel3)

    activity3 = models.Activity(name="Shopping in Patong", description="Explore Patong's shopping area", price=50.0, day_id=day3.id)
    db.add(activity3)

    transfer3 = models.Transfer(type="Car", from_location="Phuket Beach Resort", to_location="Phuket Airport", price=30.0, day_id=day3.id)
    db.add(transfer3)

    db.commit()

    # Sample Krabi itinerary (3 days)
    krabi_itinerary = models.Itinerary(name="Krabi 3-Day Adventure", duration=3)
    db.add(krabi_itinerary)
    db.commit()
    db.refresh(krabi_itinerary)

    # Day 1 (Krabi) - Arrival & Hotel
    day1_krabi = models.Day(itinerary_id=krabi_itinerary.id, day_number=1, date="2025-06-01")
    db.add(day1_krabi)
    db.commit()
    db.refresh(day1_krabi)

    hotel1_krabi = models.Hotel(name="Krabi Paradise Resort", address="Ao Nang Beach, Krabi", price=100.0, day_id=day1_krabi.id)
    db.add(hotel1_krabi)

    activity1_krabi = models.Activity(name="Relax at Ao Nang Beach", description="Leisure time at Ao Nang Beach", price=0.0, day_id=day1_krabi.id)
    db.add(activity1_krabi)

    transfer1_krabi = models.Transfer(type="Car", from_location="Krabi Airport", to_location="Krabi Paradise Resort", price=25.0, day_id=day1_krabi.id)
    db.add(transfer1_krabi)

    # Day 2 (Krabi) - Adventure & Sightseeing
    day2_krabi = models.Day(itinerary_id=krabi_itinerary.id, day_number=2, date="2025-06-02")
    db.add(day2_krabi)
    db.commit()
    db.refresh(day2_krabi)

    hotel2_krabi = models.Hotel(name="Ao Nang Beach Hotel", address="Ao Nang Beach, Krabi", price=110.0, day_id=day2_krabi.id)
    db.add(hotel2_krabi)

    activity2_krabi = models.Activity(name="Kayaking at Bor Thor Caves", description="Explore caves and kayaking", price=60.0, day_id=day2_krabi.id)
    db.add(activity2_krabi)

    transfer2_krabi = models.Transfer(type="Car", from_location="Ao Nang Beach", to_location="Bor Thor Caves", price=30.0, day_id=day2_krabi.id)
    db.add(transfer2_krabi)

    # Day 3 (Krabi) - Departure
    day3_krabi = models.Day(itinerary_id=krabi_itinerary.id, day_number=3, date="2025-06-03")
    db.add(day3_krabi)
    db.commit()
    db.refresh(day3_krabi)

    hotel3_krabi = models.Hotel(name="Krabi Paradise Resort", address="Ao Nang Beach, Krabi", price=100.0, day_id=day3_krabi.id)
    db.add(hotel3_krabi)

    activity3_krabi = models.Activity(name="Visit Krabi Town", description="Explore Krabi Town market", price=20.0, day_id=day3_krabi.id)
    db.add(activity3_krabi)

    transfer3_krabi = models.Transfer(type="Car", from_location="Krabi Paradise Resort", to_location="Krabi Airport", price=25.0, day_id=day3_krabi.id)
    db.add(transfer3_krabi)

    db.commit()

    

    db.close()

if __name__ == "__main__":
    seed_data()
