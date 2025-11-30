# Simple Web Agent - Backend

This is the FastAPI backend for the Simple Web Agent application.

## Features

- **Web Scraping**: Extract course information from DeepLearning.AI
- **API Endpoints**: RESTful API for frontend communication
- **Asynchronous Processing**: Built with async/await for better performance
- **Environment Configuration**: Easy configuration via environment variables

## Getting Started

### Prerequisites

- Python 3.9+
- pip (Python package manager)
- Playwright (for web scraping)
- OpenAI API key

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/simple-web-agent.git
   cd simple-web-agent/backend
   ```

2. **Create and activate a virtual environment**
   ```bash
   # On Windows
   python -m venv venv
   .\venv\Scripts\activate
   
   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   
   # Install Playwright browsers
   playwright install
   ```

4. **Set up environment variables**
   - Copy `.env.example` to `.env`
   - Update the values in `.env` with your configuration
   
   ```bash
   # On Windows
   copy .env.example .env
   
   # On macOS/Linux
   cp .env.example .env
   ```

### Running the Application

```bash
# Start the development server
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

### API Documentation

Once the server is running, you can access:

- **Interactive API docs**: http://localhost:8000/docs
- **Alternative API docs**: http://localhost:8000/redoc

## Project Structure

```
backend/
├── app/
│   ├── api/               # API routes
│   │   ├── endpoints/     # Route endpoints
│   │   └── __init__.py    # API router configuration
│   ├── core/             # Core functionality
│   │   ├── config.py     # Application settings
│   │   └── __init__.py
│   ├── models/           # Pydantic models
│   │   └── __init__.py
│   ├── services/         # Business logic
│   │   ├── web_scraper.py # Web scraping service
│   │   └── __init__.py
│   └── __init__.py
├── tests/                # Test files
├── .env.example         # Example environment variables
├── main.py              # Application entry point
├── README.md            # This file
└── requirements.txt     # Python dependencies
```

## Environment Variables

Create a `.env` file in the root directory with the following variables:

```
# Backend Configuration
PORT=8000
HOST=0.0.0.0

# OpenAI Configuration
OPENAI_API_KEY=your_openai_api_key_here

# Application Settings
DEBUG=True
ENVIRONMENT=development

# CORS Settings (comma-separated list of allowed origins)
ALLOWED_ORIGINS=http://localhost:3000,http://localhost:8000
```

## Running Tests

```bash
# Run tests
pytest
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
