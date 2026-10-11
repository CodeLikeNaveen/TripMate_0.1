# ✈️ TripMate — A Multi-Agent Travel Planner with LangGraph

Planning a trip usually means jumping between multiple websites, tools, and spreadsheets. This project brings that flow into one experience by combining:

- a flight-search agent,
- a hotel-research agent,
- an itinerary-planning agent, and
- a final response agent,

all coordinated through a LangGraph workflow.

## Features

- ✈️ Flight research using AviationStack
- 🏨 Hotel suggestions using Tavily search
- 🧠 Multi-agent orchestration with LangGraph
- 📝 Structured travel itinerary generation
- 🌐 FastAPI backend with a simple web interface
- 💾 Conversation state persistence using PostgreSQL
- ⚡ LLM-powered responses with Groq

## Tech Stack

- Python 3.10+
- FastAPI
- Jinja2 + HTML/CSS/JavaScript frontend
- LangGraph
- LangChain
- Groq LLMs
- PostgreSQL
- Tavily API
- AviationStack API

## Project Structure

```text
.
├── app.py                # FastAPI app entry point
├── backend.py            # LangGraph travel workflow
├── requirements.txt      # Python dependencies
├── static/               # Static frontend assets
├── templates/            # HTML templates
└── tools/                # Flight and web search integrations
```

# Install uv:
- open powershell and run the command
- powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

## Run
- ```uv init```
    - start a basic setup
- ```uv venv```
    - creates a virtual environment
- ```.venv\Scripts\activate```
    - run to activate

## add libraries
- ```uv add -r requirements.txt```

## Run Postgrace server on Render
- [Render.com](https://render.com/)
- [Link of database](https://dashboard.render.com/)


## GROQ API KEY
- [Line for key creation](https://console.groq.com/keys)
- [view all models](https://console.groq.com/playground)

## Aviation Stack API KEY
- [Line for key creation](https://aviationstack.com/)
- [dashboard](https://aviationstack.com/dashboard)

## Aviation Stack API KEY
- [Home Page](https://app.tavily.com/home)