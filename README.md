# Simple Web Agent

A web application that allows users to search and explore DeepLearning.AI courses using AI-powered web scraping.

## Features

- Search and browse DeepLearning.AI courses
- AI-powered content extraction
- Clean, responsive user interface
- Screenshot capture of course pages

## Tech Stack

- **Backend**: FastAPI (Python)
- **Frontend**: React.js with TypeScript
- **AI**: OpenAI GPT-4
- **Web Scraping**: Playwright
- **Styling**: Tailwind CSS

## Getting Started

### Prerequisites

- Python 3.8+
- Node.js 16+
- npm or yarn
- OpenAI API key

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd SWA-APP
   ```

2. Set up the backend:
   ```bash
   # Create and activate a virtual environment
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   
   # Install dependencies
   pip install -r requirements.txt
   ```

3. Set up the frontend:
   ```bash
   cd frontend
   npm install
   ```

4. Create a `.env` file in the root directory and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

### Running the Application

1. Start the backend server:
   ```bash
   uvicorn app.main:app --reload
   ```

2. In a new terminal, start the frontend development server:
   ```bash
   cd frontend
   npm start
   ```

3. Open your browser and navigate to `http://localhost:3000`

## Project Structure

```
SWA-APP/
├── backend/               # Backend source code
│   ├── app/              # Main application package
│   ├── tests/            # Test files
│   └── requirements.txt  # Python dependencies
├── frontend/             # Frontend source code
│   ├── public/           # Static files
│   └── src/              # React source code
├── .gitignore           # Git ignore file
└── README.md            # Project documentation
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
