workspace "Simple Web Agent (SWA) Application" "C4 model for the Simple Web Agent application" {
    model {
        // ==================================================
        // People and roles
        // ==================================================
        user = person "User" "A user searching for DeepLearning.AI courses"
        
        // ==================================================
        // Software systems
        // ==================================================
        swa = softwareSystem "Simple Web Agent" "Automates course discovery on DeepLearning.AI" {
            // Web Application
            frontend = container "Web Frontend" "React" "Provides the user interface for searching and viewing courses"
            
            // API Layer
            api = container "API Service" "FastAPI" "Handles business logic and coordinates between frontend and data sources"
            
            // Web Scraper
            scraper = container "Web Scraper" "Playwright" "Extracts course data from DeepLearning.AI website"
            
            // Data Storage
            database = container "Database" "SQLite" "Stores course information and user data"
            
            // Relationships between containers
            frontend -> api "Makes API calls to" "HTTPS/JSON"
            api -> scraper "Triggers scraping" "Internal API"
            api -> database "Reads/Writes" "SQL"
            scraper -> database "Stores scraped data" "SQL"
        }
        
        // External systems
        deeplearning_ai = softwareSystem "DeepLearning.AI" "External course provider" "External"
        
        // Relationships with external systems
        scraper -> deeplearning_ai "Scrapes course data from" "HTTPS"
        
        // User interactions
        user -> frontend "Uses"
    }
    
    views {
        // System Context View
        systemContext swa "SystemContext" "System Context Diagram" {
            include *
            autolayout
        }
        
        // Container View
        containerView swa "Containers" "Container View" {
            include *
            autolayout
        }
        
        // Component View (example for API service)
        componentView api "APIComponents" "API Service Components" {
            include *
            autolayout
        }
        
        // System Landscape View
        systemLandscape "SystemLandscape" "System Landscape" {
            include *
            autolayout
        }
    }
    
    // Styles
    styles {
        element "Person" {
            background #08427b
            color #ffffff
        }
        element "Software System" {
            background #1168bd
            color #ffffff
        }
        element "Container" {
            background #438dd5
            color #ffffff
        }
        element "Component" {
            background #85bbf0
            color #000000
        }
        element "External" {
            background #999999
            color #ffffff
        }
    }
}
