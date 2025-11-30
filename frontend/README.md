# Simple Web Agent - Frontend

This is the React frontend for the Simple Web Agent application, built with TypeScript, Vite, and Tailwind CSS.

## Features

- **Modern React** with TypeScript for type safety
- **Responsive Design** with Tailwind CSS
- **State Management** with React Query
- **Form Handling** with React Hook Form
- **Routing** with React Router
- **UI Components** with Headless UI
- **Icons** with Heroicons

## Prerequisites

- Node.js 16+ and npm/yarn
- Backend API server running (see backend README)

## Getting Started

1. **Install dependencies**:
   ```bash
   cd frontend
   npm install
   # or
   yarn
   ```

2. **Start the development server**:
   ```bash
   npm run dev
   # or
   yarn dev
   ```

3. **Open in your browser**:
   The application will be available at [http://localhost:3000](http://localhost:3000)

## Available Scripts

- `dev` - Start the development server
- `build` - Build the application for production
- `preview` - Preview the production build locally
- `lint` - Run ESLint
- `format` - Format code with Prettier

## Project Structure

```
frontend/
├── public/              # Static files
├── src/
│   ├── assets/          # Images, fonts, etc.
│   ├── components/      # Reusable UI components
│   ├── hooks/           # Custom React hooks
│   ├── layouts/         # Layout components
│   ├── pages/           # Page components
│   ├── services/        # API services
│   ├── styles/          # Global styles
│   ├── utils/           # Utility functions
│   ├── App.tsx          # Main application component
│   └── main.tsx         # Application entry point
├── .env.example         # Example environment variables
├── index.html           # HTML template
├── package.json         # Project dependencies
├── tailwind.config.js   # Tailwind CSS configuration
└── tsconfig.json        # TypeScript configuration
```

## Environment Variables

Create a `.env` file in the frontend directory with the following variables:

```env
VITE_API_URL=http://localhost:8000
```

## Building for Production

To create a production build:

```bash
npm run build
# or
yarn build
```

The build artifacts will be stored in the `dist/` directory.

## License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.
