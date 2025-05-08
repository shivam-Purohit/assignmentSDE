from fastapi import FastAPI
from app.routes import auth, itineraries, reviews, mcp
from app.database import engine
from fastapi.middleware.cors import CORSMiddleware
from app.models import Base
from fastapi_mcp import FastApiMCP

# Create tables (for dev/testing; use Alembic for production)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Travel Itinerary API",
    description="API for managing and recommending travel itineraries.",
)

app.include_router(auth.router)
app.include_router(itineraries.router)
app.include_router(reviews.router)
app.include_router(mcp.router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount the MCP server
mcp = FastApiMCP(
    app,
    name="Travel Itinerary MCP",
    description="MCP server for travel itinerary APIs",
)
mcp.mount()

@app.get("/", tags=["root"])
def read_root():
    return {"message": "Travel Itinerary API"}
