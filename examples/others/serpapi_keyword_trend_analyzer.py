"""
export OPENAI_API_KEY="YOUR_OPENAI_API_KEY"  # Enter your API key here 

If you use Azure;

export AZURE_OPENAI_API_KEY="YOUR_AZURE_OPENAI_API_KEY"  # Enter your API key here 
export AZURE_OPENAI_ENDPOINT="YOUR_AZURE_OPENAI_ENDPOINT"
export AZURE_OPENAI_MODEL_NAME="YOUR_AZURE_OPENAI_MODEL_NAME"
export AZURE_OPENAI_DEPLOYMENT="YOUR_AZURE_OPENAI_DEPLOYMENT"
export AZURE_OPENAI_API_VERSION="YOUR_AZURE_OPENAI_API_VERSION"

# 📈 SerpAPI Keyword Trend Analyzer
This agent analyzes keyword trends by fetching the latest search results using SerpAPI.

## 🚀 Features
- Analyzes keyword trends based on search results
- Uses SerpAPI for web search integration
- Returns search results with titles, links, and snippets

## 🔧 Installation

🟥 Ensure you set up your SerpAPI API key before running the agent.

```bash
pip install upsonic requests
```
"""


import requests
import json
from upsonic import Agent, Task, ObjectResponse

# Initialize the AI agent
search_agent = Agent("SerpAPI Keyword Trend Analyzer", model="openai/gpt-4o", reflection=True)  # If using Azure, set model="azure/gpt-4o"

# Define response format
class SearchResult(ObjectResponse):
    title: str
    link: str
    snippet: str

class SearchResponse(ObjectResponse):
    results: list[SearchResult]

# Define SerpAPI Tool
class SerpAPITools:
    def search(self, query: str) -> list[dict]:
        api_key = "YOUR_SERP_API_KEY_HERE"  # Enter your API key here
        url = "https://google.serper.dev/search"
        headers = {'X-API-KEY': api_key, 'Content-Type': 'application/json'}
        payload = json.dumps({"q": query})
        
        response = requests.post(url, headers=headers, data=payload)
        if response.status_code == 200:
            return response.json().get("organic", [])[:10]
        return []

# Define keywords for search
keyword = "AI advancements"

# Task to analyze keyword trends
search_task = Task(
    "Analyze for keyword trends by retrieving the latest search results.",
    response_format=SearchResponse,
    tools=[SerpAPITools],
    context=[keyword]
)
search_agent.print_do(search_task)

