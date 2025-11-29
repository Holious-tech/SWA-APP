# SWA-APP Architecture Documentation

This directory contains the C4 model documentation for the Simple Web Agent (SWA) application.

## Overview

The C4 model is used to document the architecture of the SWA-APP, providing different levels of abstraction:

1. **System Context** - High-level view of the system and its users
2. **Container** - Major components and their interactions
3. **Component** - Internal structure of each container
4. **Code** (not always shown) - Implementation details

## Files

- `workspace.dsl` - Source of truth for the C4 model (Structurizr DSL)
- `diagrams/` - Auto-generated diagrams in various formats
  - `system-context.png` - High-level system context
  - `container.png` - Container diagram
  - `components/` - Component diagrams

## How to Update

1. **Edit the DSL**: Update `workspace.dsl` with your architectural changes
2. **Generate diagrams locally**:
   ```bash
   # Install Structurizr CLI (if not already installed)
   # Generate diagrams
   structurizr-cli export -workspace workspace.dsl -format png -output diagrams/
   ```
3. **View changes**: Check the generated diagrams in the `diagrams/` directory
4. **Commit and push**: The GitHub Actions workflow will automatically update the diagrams on push

## Best Practices

- Keep the DSL file well-organized with clear sections
- Add descriptions to all elements for better documentation
- Use tags to group related elements
- Update the model as the architecture evolves

## Viewing the Model

To view and edit the model interactively:

1. Install Docker
2. Run Structurizr Lite:
   ```bash
   docker run -it --rm -p 8080:8080 -v $(pwd):/usr/local/structurizr structurizr/lite
   ```
3. Open http://localhost:8080 in your browser
