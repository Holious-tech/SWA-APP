workspace "AI-Powered Web Scraping and Analysis System" "An AI-powered system designed to scrape dynamic web content, extract structured data using an LLM, and display the results in a user interface." {

    !identifiers hierarchical

    model {
        // --- People ---
        u = person "Developer/Analyst" "The user who configures the scraper, initiates the job, and views the structured results."
        
        // --- External Systems (C1) ---
        ws = softwareSystem "Target Web Server" "Hosts the dynamic content (HTML/JS) to be scraped." {
            tags "External"
        }
        llm = softwareSystem "LLM Service" "The external LLM (e.g., OpenAI API) that converts raw HTML into structured JSON." {
            tags "External"
        }

        // --- Our Software System (C1 Boundary) ---
        ss = softwareSystem "AI Scraper & Analyzer" "The core application that orchestrates the scraping, processing, storage, and presentation of the data." {
            tags "Internal"
            
            // --- C2 Containers ---
            wa = container "Web Application" "Serves the user interface allowing configuration and display of structured results." "React/Next.js"
            db = container "Structured Data Store" "Database storing the final, clean, structured data." "PostgreSQL" { 
                tags "Database" 
            }
            
            // --- C2 Container: Scraping & Processing API ---
            api = container "Scraping & Processing API" "The backend service that runs the WebScraperAgent and LLM Client logic." "Python/FastAPI" {
                
                // --- C3 Components inside the API ---
                scraper = component "WebScraperAgent" "Controls the headless browser (Playwright) to retrieve fully rendered HTML and screenshots." "Python Class"
                
                models = component "Pydantic Data Models" "The defined schema used to enforce the structure of the output JSON." "Python Pydantic Schemas"
                
                processor = component "LLM Processor/Client" "Manages communication with the external LLM for structured extraction." "Python Client"
            }
        }

        // --- C1, C2, C3 Relationships ---
        
        // External Relationships (C1/C2 - People and C2 Internal Links)
        u -> ss.wa "Configures job and views results via"

        // Internal Relationships (C2 - Container to Container)
        ss.wa -> ss.api "Initiates scraping job via API call (Async)"
        ss.wa -> ss.db "Retrieves structured results for display (Read-Only)"
        
        // C3 Component Links: Defines all external communication for the API
        ss.api.scraper -> ws "Accesses dynamic web content from" 
        ss.api.processor -> llm "Requests structured data from" 
        
        // C3 Internal Flow & Storage
        ss.api.processor -> ss.db "Writes final structured data to"
        ss.api.scraper -> ss.api.processor "Passes raw HTML and screenshot to"
        ss.api.processor -> ss.api.models "References schema structure from"
    }

    views {
        systemContext ss "SystemContext" { 
            title "C1: System Context Diagram - AI Scraper & Analyzer"
            description "Shows the core system, its users, and external dependencies."
            include *
        }

        container ss "ContainerDiagram" { 
            title "C2: Container Diagram - AI Scraper & Analyzer"
            description "Shows the high-level code containers within the AI Scraper & Analyzer system."
            include *
        }
        
        component ss.api "API_Components" {
            title "C3: Component Diagram - Scraping & Processing API"
            description "Shows the internal components of the API that execute the core scraping and LLM processing workflow."
            include *
            include ws
            include llm 
            include ss.db
            exclude ss.wa 
        }

        styles {
            element "Element" { 
                color #55aa55
                stroke #55aa55
                strokeWidth 7
                shape roundedbox
            }
            element "Person" { 
                shape person
            }
            element "External" { 
                color #cc3333
                stroke #cc3333
                opacity 70
            }
            element "Internal" { 
                color #1168bd
                stroke #1168bd
            }
            element "Database" { 
                shape cylinder
            }
            relationship "Relationship" { 
                thickness 4
            }
        }
    }

    configuration {
        scope softwaresystem
    }
}