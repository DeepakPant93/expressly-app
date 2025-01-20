---
title: Expressly
emoji: 🛠️
colorFrom: blue
colorTo: purple
sdk: docker
app_port: 7860
license: mit
short_description: Expressly - Text Transformation App
---

# Expressly - Text Transformation App Backend

This document provides an overview of the backend server for the Expressly - Text Transformation App. The app is designed to transform text based on user preferences and descriptions, leveraging a CrewAI-based multi-agent AI application.

## Key Features

### Text Transformation Options
The backend supports the following transformation capabilities:
1. **Formats**
   - For details on supported formats, please refer to the [Expressly Wiki](https://github.com/DeepakPant93/expressly/wiki).

2. **Tones**
   - For details on supported tones, please refer to the [Expressly Wiki](https://github.com/DeepakPant93/expressly/wiki).

3. **Target Audience**
   - For details on supported target audiences, please refer to the [Expressly Wiki](https://github.com/DeepakPant93/expressly/wiki).

### Output
The backend processes user inputs and generates formatted text tailored to the specified preferences. Users can easily copy and utilize the output.

## Backend Configuration

### Prerequisites
1. Install `uv` and `crewai` if not already installed:
   ```bash
   pip install uv crewai
   ```
2. Navigate to your project directory and install dependencies:
   ```bash
   crewai install
   ```
   (Optional: Lock dependencies using the CLI command.)

### Customization
1. Add environment variables to the `.env` file:
   ```plaintext
   MODEL=gemini/gemini-1.5-flash
   MODEL_API_KEY=<model_api_key> # Your API key here
   ```
2. Modify configuration files as needed:
   - `src/expressly_server/config/agents.yaml`: Agents configuration.
   - `src/expressly_server/config/tasks.yaml`: Tasks configuration.
   - `src/expressly_server/crew.py`: Crew configuration with custom logic, tools, and arguments.
   - `src/expressly_server/main.py`: Entrypoint to kick off the crew with inputs for agents and tasks.
   - `src/expressly_server/app.py`: FastAPI configuration.
   - `src/expressly_server/web_app.py`: Gradio configuration.


### Running the Backend
To start the backend server and execute tasks:
```bash
crewai run
```

## Additional Notes
- Ensure all environment variables are correctly set in the `.env` file check for [.env.example](.env.example) file for reference.
- Regularly update your agents and tasks configuration to enhance functionality.
- Refer to the CrewAI documentation for advanced customizations.

This backend server powers the text transformation capabilities of Expressly, making it adaptable to a wide range of use cases.
