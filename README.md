A FastAPI-based backend system for managing travel itineraries. This project is built with SQLAlchemy and SQLite and supports the Model Context Protocol (MCP) for seamless integration with AI assistants.

---

## 🚀 Features

- **Database Architecture**: SQLAlchemy models for itineraries, hotels, transfers, and activities
- **RESTful API**: Create, view, and manage multi-day travel itineraries
- **Dummy Data**: Seed script with sample trips for Phuket and Krabi (2, 3, and 4-night variations)
- **Recommended Trips**: Popularity and cost fields help AI suggest optimal plans
- **MCP Integration**: Ready-to-use Model Context Protocol support

---

## Installation

1. Ensure you have Python 3.8+ installed

2. Install uv (fast Python package installer) from [here](https://docs.astral.sh/uv/getting-started/installation/):

3. Clone this repository and navigate to the project directory:

   ```bash
   git clone git@github.com:shivam-Purohit/assignmentSDE.git
   cd itinerary-mcp-server
   ```

4. Create a virtual environment and install dependencies:

   ```bash
    python -m venv venv
   ```

5. Activate the virtual environment:

   **On Linux/macOS:**

   ```bash
   source .venv/bin/activate
   ```

   **On Windows (Command Prompt):**

   ```cmd
   .venv\Scripts\activate.bat
   ```

## Running the Project
 
 Install the dependencies 
```bash
pip install -r requirements.txt
```
Run the server
```bash
uvicorn app.main:app --reload
```
Load the dummy data
```bash
python add_data.py
```


The API will be available at `http://localhost:8000` and the API documentation at `http://localhost:8000/docs`.

## Using the Model Context Protocol (MCP)

🧠 What is MCP in this Context?
MCP (Model Context Protocol) is a structured way to expose your app's models, operations, and logic in a machine-readable format, so AI tools can interact with it seamlessly.

MCP helps an assistant:

- Know what an Itinerary, Day, Activity, or Review means

- Discover available operations: create_itinerary, get_recommendations, add_review, etc.

- Know expected inputs/outputs, types, constraints

- Trigger those operations programmatically via the AP

![Screenshot (183)](https://github.com/user-attachments/assets/2b73706a-b046-4509-9f6f-c317f7265137)

It will rank based on overall cost and will suggest the cheapest first. We can sort based on ratings, reviews by users and popularity.
  ```json
[
  {
    "name": "Krabi 4-Day Adventure",
    "duration": 4,
    "region": "Krabi",
    "description": "A longer exploration of Krabi, including more islands and stunning cliffs.",
    "id": 4,
    "popularity": 85,
    "is_recommended": true,
    "created_at": "2025-04-30T08:29:06.908603",
    "days": [
      {
        "day_number": 1,
        "date": "2025-07-10",
        "hotels": [
          {
            "name": "Krabi Sands Resort",
            "address": "123 Cliff Rd, Krabi",
            "rating": 4.6,
            "checkin_time": "2025-07-10T14:00:00",
            "checkout_time": "2025-07-14T12:00:00",
            "cost": 3500
          }
        ],
        "transfers": [],
        "activities": [
          {
            "name": "Krabi Night Market",
            "description": "Explore Krabi's famous night market for local food and souvenirs.",
            "duration_hours": 3,
            "category": "Leisure",
            "cost": 0
          }
        ]
      },
      {
        "day_number": 2,
        "date": "2025-07-11",
        "hotels": [],
        "transfers": [],
        "activities": [
          {
            "name": "Railay Beach Adventure",
            "description": "Rock climbing and beach activities at Railay Beach.",
            "duration_hours": 5,
            "category": "Adventure",
            "cost": 1200
          }
        ]
      },
      {
        "day_number": 3,
        "date": "2025-07-12",
        "hotels": [],
        "transfers": [
          {
            "type": "Boat",
            "departure_time": "2025-07-12T08:00:00",
            "arrival_time": "2025-07-12T09:00:00",
            "duration_minutes": 60,
            "vehicle_type": "Speedboat"
          }
        ],
        "activities": [
          {
            "name": "Phra Nang Cave Beach",
            "description": "Visit Phra Nang Cave Beach for a unique beach experience.",
            "duration_hours": 3,
            "category": "Sightseeing",
            "cost": 100
          }
        ]
      },
      {
        "day_number": 4,
        "date": "2025-07-13",
        "hotels": [],
        "transfers": [],
        "activities": [
          {
            "name": "Krabi Walking Street",
            "description": "Enjoy a stroll through Krabi Walking Street.",
            "duration_hours": 2,
            "category": "Leisure",
            "cost": 0
          }
        ]
      }
    ],
    "reviews": [
      {
        "rating": 2,
        "comment": "string",
        "id": 2,
        "user": {
          "email": "shivampurohit900@gmail.com",
          "full_name": "shivam",
          "id": 1,
          "is_active": true,
          "created_at": "2025-04-30T08:31:09.782477"
        },
        "created_at": "2025-04-30T08:32:49.155935"
      }
    ],
    "overall_cost": 4800,
    "avg_rating": 2
  },
  {
    "name": "Phuket 4-Day Escape",
    "duration": 4,
    "region": "Phuket",
    "description": "Explore more of Phuket with longer stays and varied activities.",
    "id": 3,
    "popularity": 75,
    "is_recommended": true,
    "created_at": "2025-04-30T08:29:06.895413",
    "days": [
      {
        "day_number": 1,
        "date": "2025-07-01",
        "hotels": [
          {
            "name": "Phuket Grand Resort",
            "address": "789 Beachfront Rd, Phuket",
            "rating": 4.7,
            "checkin_time": "2025-07-01T14:00:00",
            "checkout_time": "2025-07-05T12:00:00",
            "cost": 3200
          }
        ],
        "transfers": [],
        "activities": [
          {
            "name": "Phuket Old Town Exploration",
            "description": "Visit historical temples and Sino-Portuguese architecture in Old Phuket Town.",
            "duration_hours": 4,
            "category": "Sightseeing",
            "cost": 200
          }
        ]
      },
      {
        "day_number": 2,
        "date": "2025-07-02",
        "hotels": [],
        "transfers": [
          {
            "type": "Bus",
            "departure_time": "2025-07-02T10:00:00",
            "arrival_time": "2025-07-02T11:00:00",
            "duration_minutes": 60,
            "vehicle_type": "Luxury Bus"
          }
        ],
        "activities": [
          {
            "name": "Phi Phi Islands Tour",
            "description": "Explore the beautiful Phi Phi islands by boat.",
            "duration_hours": 6,
            "category": "Island Hopping",
            "cost": 2200
          }
        ]
      },
      {
        "day_number": 3,
        "date": "2025-07-03",
        "hotels": [
          {
            "name": "Phuket Beach Resort",
            "address": "1001 Oceanview Rd, Phuket",
            "rating": 4.3,
            "checkin_time": "2025-07-03T13:00:00",
            "checkout_time": "2025-07-05T12:00:00",
            "cost": 2800
          }
        ],
        "transfers": [],
        "activities": [
          {
            "name": "Phuket FantaSea Show",
            "description": "Enjoy a cultural show featuring Thai performances and a buffet dinner.",
            "duration_hours": 3,
            "category": "Entertainment",
            "cost": 1500
          }
        ]
      },
      {
        "day_number": 4,
        "date": "2025-07-04",
        "hotels": [],
        "transfers": [
          {
            "type": "Car",
            "departure_time": "2025-07-04T09:00:00",
            "arrival_time": "2025-07-04T10:00:00",
            "duration_minutes": 60,
            "vehicle_type": "SUV"
          }
        ],
        "activities": [
          {
            "name": "Relax at Kata Beach",
            "description": "Spend a relaxing day at Kata Beach.",
            "duration_hours": 5,
            "category": "Leisure",
            "cost": 0
          }
        ]
      }
    ],
    "reviews": [
      {
        "rating": 5,
        "comment": "string",
        "id": 1,
        "user": {
          "email": "shivampurohit900@gmail.com",
          "full_name": "shivam",
          "id": 1,
          "is_active": true,
          "created_at": "2025-04-30T08:31:09.782477"
        },
        "created_at": "2025-04-30T08:32:38.452485"
      }
    ],
    "overall_cost": 9900,
    "avg_rating": 5
  }
]

  ```

### MCP Configuration

Add this config to the claude json config which can be found in developer settings in claude
  ```json
{
  "mcpServers": {
    "travel-itinerary": {
      "command": "python",
      "args": ["-m", "mcp_proxy", "http://127.0.0.1:8000/mcp"]
    }
  }
}

  ```
You will be able to use the api calls as tools in the claude chat.
![Screenshot (179)](https://github.com/user-attachments/assets/d2804795-e1dc-4fe1-a911-5ce24f2e844b)


Then you can ask questions and it will use the available tools to fetch data and curate a custom answer
![Screenshot (180)](https://github.com/user-attachments/assets/5973ea73-e576-45ad-b5e9-b1c001bdd91d)




### Supported MCP Clients

You can use any MCP-compatible client to interact with this API. MCP clients include:

- [GitHub Copilot](https://github.com/features/copilot)
- [Claude Desktop](https://claude.ai/download)
- And other MCP-compatible assistants

For more information about MCP, visit the [official MCP documentation](https://modelcontextprotocol.io/).
