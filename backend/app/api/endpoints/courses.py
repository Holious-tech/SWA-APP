from fastapi import APIRouter, HTTPException, Depends
from typing import Optional
from pydantic import BaseModel
import base64
import asyncio

from ....services.web_scraper import WebScraperAgent, DeeplearningCourseList

router = APIRouter()

class ScrapeRequest(BaseModel):
    url: str
    instructions: str

@router.post("/scrape", response_model=DeeplearningCourseList)
async def scrape_courses(request: ScrapeRequest):
    """
    Scrape courses from the specified URL using the provided instructions.
    
    - **url**: The target URL to scrape (e.g., "https://www.deeplearning.ai/courses")
    - **instructions**: Specific instructions for the LLM on how to process the page
    """
    try:
        scraper = WebScraperAgent()
        result, _ = await scraper.scrape_courses(request.url, request.instructions)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/test")
async def test_endpoint():
    """Test endpoint to verify the API is running."""
    return {"message": "Courses endpoint is working!"}
