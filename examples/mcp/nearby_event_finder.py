"""
export OPENAI_API_KEY="YOUR_OPENAI_API_KEY" 

If you use Azure;

export AZURE_OPENAI_API_KEY="YOUR_AZURE_OPENAI_API_KEY" 
export AZURE_OPENAI_ENDPOINT="YOUR_AZURE_OPENAI_ENDPOINT"
export AZURE_OPENAI_MODEL_NAME="YOUR_AZURE_OPENAI_MODEL_NAME"
export AZURE_OPENAI_DEPLOYMENT="YOUR_AZURE_OPENAI_DEPLOYMENT"
export AZURE_OPENAI_API_VERSION="YOUR_AZURE_OPENAI_API_VERSION"

# 🎟️ Nearby Event Finder
This agent retrieves upcoming events in a selected city using Google Maps MCP.

## 🚀 Features
- Finds upcoming events based on city and date
- Provides event details including name, location, and category

## 🔧 Installation

🟥 Ensure you set up your GOOGLE MAPS API key before running the agent.

```bash
pip install upsonic

# Ensure Node.js is installed for MCP
# Visit: https://nodejs.org/

🔗 **For more details about MCP servers** (including NPX, UVX, and Docker-based options), check the docs:
👉 Upsonic AI Docs: https://docs.upsonic.ai/concepts/mcp_tools
🛠 MCP GitHub Repo: https://github.com/modelcontextprotocol
🌍 Other MCP Servers: https://github.com/modelcontextprotocol/servers
```
"""

from upsonic import Agent, Task, ObjectResponse

# Initialize the AI agent
event_finder_agent = Agent("Nearby Event Finder", model="openai/gpt-4o")  # If using Azure, set model="azure/gpt-4o"

# Define Google Maps MCP
class GoogleMapsMCP:
    command = "npx"
    args = ["-y", "@modelcontextprotocol/server-google-maps"]
    env = {"GOOGLE_MAPS_API_KEY": "YOUR_GOOGLE_MAPS_API_KEY_HERE"}

# Define response format
class Event(ObjectResponse):
    name: str
    location: str
    date: str
    category: str

class EventList(ObjectResponse):
    events: list[Event]

# Define city and date
city = "New York"
date = ""  # Please enter a date

# Task to find upcoming events
event_task = Task(
    "Find upcoming events happening in city on date, including name, location, and category.",
    tools=[GoogleMapsMCP],
    response_format=EventList,
    context=[city, date]
)

event_finder_agent.print_do(event_task)
