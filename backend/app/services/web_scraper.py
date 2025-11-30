import asyncio
import nest_asyncio
from typing import Optional, Tuple
from playwright.async_api import async_playwright
from openai import OpenAI
from pydantic import BaseModel
from ...core.config import settings

# Apply nest_asyncio to allow nested event loops
nest_asyncio.apply()

class DeeplearningCourse(BaseModel):
    title: str
    description: str
    presenter: list[str]
    imageUrl: str
    courseURL: str

class DeeplearningCourseList(BaseModel):
    courses: list[DeeplearningCourse]

class WebScraperAgent:
    def __init__(self):
        self.playwright = None
        self.browser = None
        self.page = None
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)

    async def init_browser(self):
        """Initialize the Playwright browser instance."""
        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.chromium.launch(
            headless=True,
            args=[
                "--disable-dev-shm-usage",
                "--no-sandbox",
                "--disable-setuid-sandbox",
                "--disable-accelerated-2d-canvas",
                "--disable-gpu",
                "--no-zygote",
                "--disable-audio-output",
                "--disable-software-rasterizer",
                "--disable-webgl",
                "--disable-web-security",
                "--disable-features=LazyFrameLoading",
                "--disable-features=IsolateOrigins",
                "--disable-background-networking"
            ]
        )
        self.page = await self.browser.new_page()

    async def scrape_content(self, url: str) -> str:
        """Scrape content from the given URL."""
        if not self.page or self.page.is_closed():
            await self.init_browser()
        await self.page.goto(url, wait_until="load")
        await self.page.wait_for_timeout(2000)  # Wait for dynamic content
        return await self.page.content()

    async def take_screenshot(self, path: str = "screenshot.png") -> str:
        """Take a screenshot of the current page."""
        await self.page.screenshot(path=path, full_page=True)
        return path

    async def screenshot_buffer(self) -> bytes:
        """Get a screenshot as bytes."""
        screenshot_bytes = await self.page.screenshot(type="png", full_page=False)
        return screenshot_bytes

    async def close(self):
        """Close the browser and release resources."""
        if self.browser:
            await self.browser.close()
        if self.playwright:
            await self.playwright.stop()
        self.playwright = None
        self.browser = None
        self.page = None

    async def process_with_llm(self, html: str, instructions: str, truncate: bool = False) -> DeeplearningCourseList:
        """Process HTML content with OpenAI's LLM to extract structured data."""
        if truncate:
            html = html[:150000]  # Truncate to stay under token limits
            
        completion = self.client.chat.completions.create(
            model="gpt-4",  # or the specific model you have access to
            messages=[{
                "role": "system",
                "content": f"""
                You are an expert web scraping agent. Your task is to:
                Extract relevant information from this HTML to JSON 
                following these instructions:
                {instructions}
                
                Extract the title, description, presenter, 
                the image URL and course URL for each of 
                all the courses for the deeplearning.ai website

                Return ONLY valid JSON, no markdown or extra text.
                """
            }, {
                "role": "user",
                "content": html
            }],
            temperature=0.1,
            response_model=DeeplearningCourseList
        )
        
        if hasattr(completion, 'choices') and completion.choices:
            return completion.choices[0].message.parsed
        return DeeplearningCourseList(courses=[])

    async def scrape_courses(self, target_url: str, instructions: str) -> Tuple[Optional[DeeplearningCourseList], Optional[bytes]]:
        """Scrape courses from the target URL with the given instructions."""
        result = None
        screenshot = None
        
        try:
            # Scrape content and capture screenshot
            html_content = await self.scrape_content(target_url)
            screenshot = await self.screenshot_buffer()
            
            # Process content with LLM
            result = await self.process_with_llm(html_content, instructions)
            
        except Exception as e:
            print(f"Error during scraping: {str(e)}")
            raise
            
        finally:
            await self.close()
            
        return result, screenshot
