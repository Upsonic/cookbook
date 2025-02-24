"""
export OPENAI_API_KEY="YOUR_OPENAI_API_KEY" 

If you use Azure;

export AZURE_OPENAI_API_KEY="YOUR_AZURE_OPENAI_API_KEY" 
export AZURE_OPENAI_ENDPOINT="YOUR_AZURE_OPENAI_ENDPOINT"
export AZURE_OPENAI_MODEL_NAME="YOUR_AZURE_OPENAI_MODEL_NAME"
export AZURE_OPENAI_DEPLOYMENT="YOUR_AZURE_OPENAI_DEPLOYMENT"
export AZURE_OPENAI_API_VERSION="YOUR_AZURE_OPENAI_API_VERSION"

# 🌍 On the Road Museum Travel Planner
This agent finds the best travel route with the most museums along the way using Google Maps MCP.

## 🚀 Features
- Finds the most efficient travel route between two cities
- Lists museums along the way with details like location, open times, and fees

## 🔧 Installation
🟥 Ensure you set up your GOOGLE MAPS API key before running the agent.

```bash
pip install upsonic

# Ensure Node.js is installed
# Visit: https://nodejs.org/

🔗 **For more details about MCP servers** (including NPX, UVX, and Docker-based options), check the docs:
👉 Upsonic AI Docs: https://docs.upsonic.ai/concepts/mcp_tools
🛠 MCP GitHub Repo: https://github.com/modelcontextprotocol
🌍 Other MCP Servers: https://github.com/modelcontextprotocol/servers
```
"""

from upsonic import Agent, Task, ObjectResponse

# Initialize the AI agent
travel_agent = Agent("On the Road Museum Travel Planner", model="openai/gpt-4o")  # If using Azure, set model="azure/gpt-4o"

# Define Google Maps MCP
class GoogleMapsMCP:
    command = "npx"
    args = ["-y", "@modelcontextprotocol/server-google-maps"]
    env = {"GOOGLE_MAPS_API_KEY": "YOUR_GOOGLE_MAPS_API_KEY_HERE"}

# Define response formats
class RouteWithMuseumsResponse(ObjectResponse):
    cities: list[str]
    distance: str
    duration: str
    total_museums: int

class Museum(ObjectResponse):
    name: str
    location: str
    paid: bool
    open_time: str

class MuseumsPerCityResponse(ObjectResponse):
    city_museums: list[Museum]  
  

# Define travel route parameters
origin = "San Francisco"
destination = "Santa Barbara"

# Task to find the best travel route with museums
route_task = Task(
    "Find the best route between origin and destination with the most museums, including cities along the route, total distance, duration, and the total number of museums.",
    tools=[GoogleMapsMCP],
    response_format=RouteWithMuseumsResponse,
    context=[origin, destination]
)
travel_agent.print_do(route_task)

# Task to list museums for each city along the route
museums_task = Task(
    "List all museums for the cities along the route, providing details including the city name, museum name, location, entrance fee requirement, and opening time.",
    tools=[GoogleMapsMCP],
    response_format=MuseumsPerCityResponse,
    context=[route_task]
)
travel_agent.print_do(museums_task)
