from fastapi import APIRouter
from .endpoints import courses

# Create the main API router
api_router = APIRouter()

# Include the courses router with the /courses prefix
api_router.include_router(courses.router, prefix="/courses", tags=["courses"])
