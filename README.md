# 🌍 Travel Itinerary Backend System

This is a backend system built using **FastAPI** and **SQLAlchemy** for managing and recommending travel itineraries, focused on the **Phuket** and **Krabi** regions of Thailand. It supports day-wise tracking of hotels, activities, and transfers, and includes an MCP server to recommend itineraries based on trip duration.

---

## 📁 Project Structure

├── app
│   ├── __init__.py
│   ├── main.py               # Entry point for FastAPI app
│   ├── models.py             # SQLAlchemy models (Itinerary, Day, Hotel, Activity, Transfer)
│   ├── schemas.py            # Pydantic schemas for request/response validation
│   ├── database.py           # DB session & engine config
│   ├── mcp.py                # MCP server logic for itinerary recommendations
│   └── routes
│       ├── __init__.py
│       └── itineraries.py    # Routes for creating and viewing itineraries
├── seed_data.py              # Script to populate DB with Phuket & Krabi sample data
├── requirements.txt          # Python dependencies
└── README.md                 # You are here!

---

## 🛠 Setup Instructions (Windows)

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/travel-itinerary-backend.git
cd travel-itinerary-backend
2. Create a Virtual Environment

python -m venv venv
venv\Scripts\activate
3. Install Dependencies

pip install -r requirements.txt
4. Seed the Database
This will create and populate a SQLite database travel.db with sample itineraries.


python seed_data.py
🚀 Running the API Server

uvicorn app.main:app --reload
Server will be available at:
📍 http://127.0.0.1:8000

🌐 API Documentation
Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc

🧩 API Endpoints

Method	Endpoint	Description
POST	/itineraries/	Create a new itinerary
GET	/itineraries/	View all itineraries
GET	/mcp/recommend/	Get a recommended itinerary by duration
🏝 Sample Itineraries
The seed data includes:

Phuket 3-Day Tour

Stay at Patong Beach, Phi Phi Islands tour, shopping

Krabi 3-Day Adventure

Ao Nang Beach relaxation, kayaking, Krabi town market

🧾 Example Request
POST /itineraries/
json
Copy
Edit
{
  "name": "My Thailand Trip",
  "duration": 5
}
📦 Dependencies
fastapi

uvicorn

sqlalchemy

pydantic

(Install using requirements.txt)

🧠 MCP Server
The MCP server is located in app/mcp.py. It recommends itineraries based on the requested number of nights.

Example usage:


GET /mcp/recommend/?nights=3
Returns a pre-defined itinerary of the specified duration.

📬 Feedback & Contributions
Feel free to open issues or submit pull requests if you'd like to contribute!
