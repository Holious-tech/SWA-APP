import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { Toaster } from 'react-hot-toast';

// Layouts
import MainLayout from '@/layouts/MainLayout';

// Pages
import HomePage from '@/pages/HomePage';
import NotFoundPage from '@/pages/NotFoundPage';

// Styles
import '@/styles/globals.css';

// Create a client
const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      refetchOnWindowFocus: false,
      retry: 1,
    },
  },
});

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <Router>
        <div className="min-h-screen bg-gray-50 dark:bg-gray-900">
          <Routes>
            <Route path="/" element={<MainLayout />}>
              <Route index element={<HomePage />} />
              {/* Add more routes here */}
              <Route path="*" element={<NotFoundPage />} />
            </Route>
          </Routes>
          <Toaster
            position="top-right"
            toastOptions={{
              className: 'bg-white dark:bg-gray-800 text-gray-900 dark:text-white',
              duration: 5000,
            }}
          />
        </div>
      </Router>
    </QueryClientProvider>
  );
}

export default App;
