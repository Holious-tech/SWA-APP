"""
API endpoints for the Simple Web Agent application.

This module contains all the API route handlers.
"""

# Import endpoints here to make them available when importing from app.api.endpoints
from .courses import router as courses_router  # noqa: F401

__all__ = ["courses_router"]
