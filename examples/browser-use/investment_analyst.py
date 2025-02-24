"""
export OPENAI_API_KEY="YOUR_OPENAI_API_KEY" 

If you use Azure;

export AZURE_OPENAI_API_KEY="YOUR_AZURE_OPENAI_API_KEY" 
export AZURE_OPENAI_ENDPOINT="YOUR_AZURE_OPENAI_ENDPOINT"
export AZURE_OPENAI_MODEL_NAME="YOUR_AZURE_OPENAI_MODEL_NAME"
export AZURE_OPENAI_DEPLOYMENT="YOUR_AZURE_OPENAI_DEPLOYMENT"
export AZURE_OPENAI_API_VERSION="YOUR_AZURE_OPENAI_API_VERSION"

# 📈 Investing Analyst
#  Agent - Hourly
AI-powered agent that scrapes hourly technical analysis insights from investing platforms.

## 🚀 Features
- Fetches real-time Buy/Sell signals for a stock
- Extracts technical analysis from the top search results


## 🔧 Installation
```bash
pip install upsonic browser-use playwright
```
"""

from upsonic import Agent, Task, ObjectResponse
from upsonic.client.tools import BrowserUse

# Initialize the AI agent
investing_agent = Agent("Investing Analyst- Hourly", model="openai/gpt-4o", reflection=True) # If using Azure, set model="azure/gpt-4o"

# Define response format for stock analysis
class StockSignal(ObjectResponse):
    stock: str
    buy: int
    sell: int

class StockSignalList(ObjectResponse):
    stock: list[StockSignal]

# Define stock symbol
stock_symbol = "TSLA"

# Task to search and extract Buy/Sell signals from Investing.com
investing_task = Task(
    " Search this : 'Investing.com  'stock symbol' technical analysis' on Google and click and open the first link, and extract Buy/Sell counts.",
    tools=[BrowserUse],
    response_format=StockSignal,
    context=[stock_symbol]
)

investing_agent.print_do(investing_task)
