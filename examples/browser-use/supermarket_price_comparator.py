"""
export OPENAI_API_KEY="YOUR_OPENAI_API_KEY" 

If you use Azure;

export AZURE_OPENAI_API_KEY="YOUR_AZURE_OPENAI_API_KEY" 
export AZURE_OPENAI_ENDPOINT="YOUR_AZURE_OPENAI_ENDPOINT"
export AZURE_OPENAI_MODEL_NAME="YOUR_AZURE_OPENAI_MODEL_NAME"
export AZURE_OPENAI_DEPLOYMENT="YOUR_AZURE_OPENAI_DEPLOYMENT"
export AZURE_OPENAI_API_VERSION="YOUR_AZURE_OPENAI_API_VERSION"

# 🛒 Supermarket Price Comparator
This Agent to track and compare product prices across supermarkets.

## 🚀 Features
- Searches for a specific product in multiple supermarkets
- Compares and finds the best price
- Provides direct shopping link for convenience

## 🔧 Installation
```bash
pip install upsonic browser-use playwright
```
"""
from upsonic import Agent, Task, ObjectResponse
from upsonic.client.tools import BrowserUse

# Initialize the AI agent
price_comparator_agent = Agent("Supermarket Price Comparator", model="openai/gpt-4o", reflection=True) # If using Azure, set model="azure/gpt-4o"

# Define response format for price tracking
class Price(ObjectResponse):
    market: str
    best_price: float
    link: str

# Define markets and product to search
market1 = "Walmart"
market2 = "Kroger"
product = "Coca-Cola Classic Soda Pop, 12 fl oz Cans, 24 Pack"

# Task to search for the product across supermarkets using Browser Use
price_task = Task(
    "Search for the product in the markets and find the best price and link.",
    tools=[BrowserUse],
    response_format=Price,
    context=[market2, market1, product]
)
price_comparator_agent.print_do(price_task)
