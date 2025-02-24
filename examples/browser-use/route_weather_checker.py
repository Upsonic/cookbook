"""
export OPENAI_API_KEY="YOUR_OPENAI_API_KEY" 

If you use to Azure;

export AZURE_OPENAI_API_KEY="YOUR_AZURE_OPENAI_API_KEY" 
export AZURE_OPENAI_ENDPOINT="YOUR_AZURE_OPENAI_ENDPOINT"
export AZURE_OPENAI_MODEL_NAME="YOUR_AZURE_OPENAI_MODEL_NAME"
export AZURE_OPENAI_DEPLOYMENT="YOUR_AZURE_OPENAI_DEPLOYMENT"
export AZURE_OPENAI_API_VERSION="YOUR_AZURE_OPENAI_API_VERSION"

# 🌤️ Route Weather Checker 
This Agent to find cities along a driving route and get real-time weather data.

## 🚀 Features
- Finds cities on the fastest driving route
- Fetches real-time weather (temperature & conditions)

## 🔧 Installation
```bash
pip install upsonic browser-use playwright

"""

from upsonic import Agent, Task, ObjectResponse
from upsonic.client.tools import BrowserUse # Importing BrowserUse


route_weather_agent = Agent("Route Weather Checker", model="openai/gpt-4o", reflection=True) #If you yuse to Azure please do model="azure/gpt-4o" 

# Define response format for creating route
class Route(ObjectResponse):
    cities_between_two_cities: list[str]

# Define response format for weather 
class RouteWeather(ObjectResponse):
    drive_route: list[str]
    cities_temperature: list[str]
    cities_condition: list[str]


# Change `starting_city` and `destination_city` to customize the route.
starting_city = "San Francisco"
destination_city= "Santa Cruz"

# Task to find for cities between two city most fastly route using Browser Use
route_task = Task(
    "Find all cities between two cities the fastly driving route.",
    tools=[BrowserUse],
    response_format=Route,
    context=[starting_city, destination_city]
)
route_weather_agent.print_do(route_task)

# Task to finding the weather conditions of the cities on the route using Browser Use
weather_task = Task(
        "Search and find all cities between two cities Weather on Google and extract temperature and conditions.",
        tools=[BrowserUse],
        response_format=RouteWeather,
        context=[route_task]
    )
route_weather_agent.print_do(weather_task)