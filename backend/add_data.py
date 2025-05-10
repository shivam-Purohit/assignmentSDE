from datetime import datetime
from app.database import SessionLocal, engine
from app import models

# Create tables
models.Base.metadata.create_all(bind=engine)

def add_dummy_data():
    db = SessionLocal()

    # ----------- 2-DAY ITINERARY: PHUKET ----------
    itinerary1 = models.Itinerary(
        name="Phuket 2-Day Getaway",
        duration=2,
        region="Phuket",
        description="Short getaway to enjoy beaches and temples in Phuket.",
        is_recommended=True,
        popularity=87
    )
    db.add(itinerary1)
    db.commit()

    # Add Days
    day1 = models.Day(itinerary_id=itinerary1.id, day_number=1, date=datetime(2025, 5, 1))
    day2 = models.Day(itinerary_id=itinerary1.id, day_number=2, date=datetime(2025, 5, 2))
    db.add_all([day1, day2])
    db.commit()

    # Day 1 Hotel + Activity
    hotel1 = models.Hotel(
        name="Andaman Beach Resort",
        address="123 Beach Rd, Phuket",
        rating=4.2,
        checkin_time=datetime(2025, 5, 1, 14),
        checkout_time=datetime(2025, 5, 2, 12),
        cost=1800.00,  # Added cost
        day_id=day1.id
    )
    activity1 = models.Activity(
        name="Big Buddha Visit",
        description="Scenic view of Phuket from the hilltop.",
        duration_hours=2.5,
        category="Sightseeing",
        cost=500.00,  # Added cost
        day_id=day1.id
    )
    db.add_all([hotel1, activity1])

    # Day 2 Transfer + Activity
    transfer1 = models.Transfer(
        type="Car",
        departure_time=datetime(2025, 5, 2, 9),
        arrival_time=datetime(2025, 5, 2, 10),
        duration_minutes=60,
        vehicle_type="SUV",
        day_id=day2.id
    )
    activity2 = models.Activity(
        name="Patong Beach",
        description="Relax at one of Phuket’s most famous beaches.",
        duration_hours=3,
        category="Leisure",
        cost=0.0,  # Free activity
        day_id=day2.id
    )
    db.add_all([transfer1, activity2])
    db.commit()

    # ----------- 3-DAY ITINERARY: KRABI ----------
    itinerary2 = models.Itinerary(
        name="Krabi 3-Day Adventure",
        duration=3,
        region="Krabi",
        description="Adventure trip covering islands and limestone cliffs in Krabi.",
        is_recommended=True,
        popularity=95
    )
    db.add(itinerary2)
    db.commit()

    # Add Days
    k_day1 = models.Day(itinerary_id=itinerary2.id, day_number=1, date=datetime(2025, 6, 10))
    k_day2 = models.Day(itinerary_id=itinerary2.id, day_number=2, date=datetime(2025, 6, 11))
    k_day3 = models.Day(itinerary_id=itinerary2.id, day_number=3, date=datetime(2025, 6, 12))
    db.add_all([k_day1, k_day2, k_day3])
    db.commit()

    # Day 1
    hotel2 = models.Hotel(
        name="Krabi Cliff View Resort",
        address="456 Cliff Rd, Krabi",
        rating=4.5,
        checkin_time=datetime(2025, 6, 10, 13),
        checkout_time=datetime(2025, 6, 12, 12),
        cost=2600.00,  # Added cost
        day_id=k_day1.id
    )
    activity3 = models.Activity(
        name="Ao Nang Beach Walk",
        description="Evening stroll along Ao Nang Beach.",
        duration_hours=2,
        category="Leisure",
        cost=0.0,  # Free activity
        day_id=k_day1.id
    )
    db.add_all([hotel2, activity3])

    # Day 2
    activity4 = models.Activity(
        name="4 Island Tour",
        description="Visit Tup, Chicken, Poda, and Phra Nang islands.",
        duration_hours=6,
        category="Island Hopping",
        cost=2000.00,  # Added cost
        day_id=k_day2.id
    )
    db.add(activity4)

    # Day 3
    transfer2 = models.Transfer(
        type="Boat",
        departure_time=datetime(2025, 6, 12, 8),
        arrival_time=datetime(2025, 6, 12, 9),
        duration_minutes=60,
        vehicle_type="Speedboat",
        day_id=k_day3.id
    )
    activity5 = models.Activity(
        name="Tiger Cave Temple",
        description="Climb to the summit of the sacred temple.",
        duration_hours=3,
        category="Sightseeing",
        cost=100.00,  # Added cost
        day_id=k_day3.id
    )
    db.add_all([transfer2, activity5])

    db.commit()

    # ----------- 4-DAY ITINERARY: PHUKET 2 ----------
    itinerary3 = models.Itinerary(
        name="Phuket 4-Day Escape",
        duration=4,
        region="Phuket",
        description="Explore more of Phuket with longer stays and varied activities.",
        is_recommended=True,
        popularity=75
    )
    db.add(itinerary3)
    db.commit()

    # Add Days
    p_day1 = models.Day(itinerary_id=itinerary3.id, day_number=1, date=datetime(2025, 7, 1))
    p_day2 = models.Day(itinerary_id=itinerary3.id, day_number=2, date=datetime(2025, 7, 2))
    p_day3 = models.Day(itinerary_id=itinerary3.id, day_number=3, date=datetime(2025, 7, 3))
    p_day4 = models.Day(itinerary_id=itinerary3.id, day_number=4, date=datetime(2025, 7, 4))
    db.add_all([p_day1, p_day2, p_day3, p_day4])
    db.commit()

    # Day 1
    hotel3 = models.Hotel(
        name="Phuket Grand Resort",
        address="789 Beachfront Rd, Phuket",
        rating=4.7,
        checkin_time=datetime(2025, 7, 1, 14),
        checkout_time=datetime(2025, 7, 5, 12),
        cost=3200.00,  # Added cost
        day_id=p_day1.id
    )
    activity6 = models.Activity(
        name="Phuket Old Town Exploration",
        description="Visit historical temples and Sino-Portuguese architecture in Old Phuket Town.",
        duration_hours=4,
        category="Sightseeing",
        cost=200.00,  # Added cost
        day_id=p_day1.id
    )
    db.add_all([hotel3, activity6])

    # Day 2
    transfer3 = models.Transfer(
        type="Bus",
        departure_time=datetime(2025, 7, 2, 10),
        arrival_time=datetime(2025, 7, 2, 11),
        duration_minutes=60,
        vehicle_type="Luxury Bus",
        day_id=p_day2.id
    )
    activity7 = models.Activity(
        name="Phi Phi Islands Tour",
        description="Explore the beautiful Phi Phi islands by boat.",
        duration_hours=6,
        category="Island Hopping",
        cost=2200.00,  # Added cost
        day_id=p_day2.id
    )
    db.add_all([transfer3, activity7])

    # Day 3
    hotel4 = models.Hotel(
        name="Phuket Beach Resort",
        address="1001 Oceanview Rd, Phuket",
        rating=4.3,
        checkin_time=datetime(2025, 7, 3, 13),
        checkout_time=datetime(2025, 7, 5, 12),
        cost=2800.00,  # Added cost
        day_id=p_day3.id
    )
    activity8 = models.Activity(
        name="Phuket FantaSea Show",
        description="Enjoy a cultural show featuring Thai performances and a buffet dinner.",
        duration_hours=3,
        category="Entertainment",
        cost=1500.00,  # Added cost
        day_id=p_day3.id
    )
    db.add_all([hotel4, activity8])

    # Day 4
    transfer4 = models.Transfer(
        type="Car",
        departure_time=datetime(2025, 7, 4, 9),
        arrival_time=datetime(2025, 7, 4, 10),
        duration_minutes=60,
        vehicle_type="SUV",
        day_id=p_day4.id
    )
    activity9 = models.Activity(
        name="Relax at Kata Beach",
        description="Spend a relaxing day at Kata Beach.",
        duration_hours=5,
        category="Leisure",
        cost=0.0,  # Free activity
        day_id=p_day4.id
    )
    db.add_all([transfer4, activity9])

    db.commit()

    # ----------- 4-DAY ITINERARY: KRABI 2 ----------
    itinerary4 = models.Itinerary(
        name="Krabi 4-Day Adventure",
        duration=4,
        region="Krabi",
        description="A longer exploration of Krabi, including more islands and stunning cliffs.",
        is_recommended=True,
        popularity=85
    )
    db.add(itinerary4)
    db.commit()

    # Add Days
    k2_day1 = models.Day(itinerary_id=itinerary4.id, day_number=1, date=datetime(2025, 7, 10))
    k2_day2 = models.Day(itinerary_id=itinerary4.id, day_number=2, date=datetime(2025, 7, 11))
    k2_day3 = models.Day(itinerary_id=itinerary4.id, day_number=3, date=datetime(2025, 7, 12))
    k2_day4 = models.Day(itinerary_id=itinerary4.id, day_number=4, date=datetime(2025, 7, 13))
    db.add_all([k2_day1, k2_day2, k2_day3, k2_day4])
    db.commit()

    # Day 1
    hotel5 = models.Hotel(
        name="Krabi Sands Resort",
        address="123 Cliff Rd, Krabi",
        rating=4.6,
        checkin_time=datetime(2025, 7, 10, 14),
        checkout_time=datetime(2025, 7, 14, 12),
        cost=3500.00,  # Added cost
        day_id=k2_day1.id
    )
    activity10 = models.Activity(
        name="Krabi Night Market",
        description="Explore Krabi's famous night market for local food and souvenirs.",
        duration_hours=3,
        category="Leisure",
        cost=0.0,  # Free activity
        day_id=k2_day1.id
    )
    db.add_all([hotel5, activity10])

    # Day 2
    activity11 = models.Activity(
        name="Railay Beach Adventure",
        description="Rock climbing and beach activities at Railay Beach.",
        duration_hours=5,
        category="Adventure",
        cost=1200.00,  # Added cost
        day_id=k2_day2.id
    )
    db.add(activity11)

    # Day 3
    transfer5 = models.Transfer(
        type="Boat",
        departure_time=datetime(2025, 7, 12, 8),
        arrival_time=datetime(2025, 7, 12, 9),
        duration_minutes=60,
        vehicle_type="Speedboat",
        day_id=k2_day3.id
    )
    activity12 = models.Activity(
        name="Phra Nang Cave Beach",
        description="Visit Phra Nang Cave Beach for a unique beach experience.",
        duration_hours=3,
        category="Sightseeing",
        cost=100.00,  # Added cost
        day_id=k2_day3.id
    )
    db.add_all([transfer5, activity12])

    # Day 4
    activity13 = models.Activity(
        name="Krabi Walking Street",
        description="Enjoy a stroll through Krabi Walking Street.",
        duration_hours=2,
        category="Leisure",
        cost=0.0,  # Free activity
        day_id=k2_day4.id
    )
    db.add(activity13)

    db.commit()
    db.close()
    print("✅ Dummy data inserted successfully.")

if __name__ == "__main__":
    add_dummy_data()
