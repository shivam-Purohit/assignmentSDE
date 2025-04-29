from fastapi import FastAPI
from app.routes import itineraries
from app import mcp

app = FastAPI(title="Travel Itinerary Manager")
app.include_router(itineraries.router)
app.include_router(mcp.router)
