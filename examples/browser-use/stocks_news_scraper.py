"""
export OPENAI_API_KEY="YOUR_OPENAI_API_KEY" 

If you use Azure;

export AZURE_OPENAI_API_KEY="YOUR_AZURE_OPENAI_API_KEY" 
export AZURE_OPENAI_ENDPOINT="YOUR_AZURE_OPENAI_ENDPOINT"
export AZURE_OPENAI_MODEL_NAME="YOUR_AZURE_OPENAI_MODEL_NAME"
export AZURE_OPENAI_DEPLOYMENT="YOUR_AZURE_OPENAI_DEPLOYMENT"
export AZURE_OPENAI_API_VERSION="YOUR_AZURE_OPENAI_API_VERSION"

# 📰 Stocks News Scraper
AI-powered agent to scrape and summarize the latest stock market news.

## 🚀 Features
- Fetches the latest stock-related news
- Extracts headlines, sources, and article links

## 🔧 Installation
```bash
pip install upsonic browser-use playwright
```
"""
from upsonic import Agent, Task, ObjectResponse
from upsonic.client.tools import BrowserUse

# Initialize the AI agent
news_agent = Agent("Stocks News Scraper", model="openai/gpt-4o", reflection=True) # If using Azure, set model="azure/gpt-4o"

# Define response format for stock news
class StockNews(ObjectResponse):
    headline: str
    source: str
    link: str

class StockNewsList(ObjectResponse):
    news: list[StockNews]

# Define stock symbol
stock_symbol = "TSLA"

# Task to search for the latest stock news using Browser Use
news_task = Task(
    "Search for the latest news articles related to stock symbol and return headlines with sources and links.",
    tools=[BrowserUse],
    response_format=StockNewsList,
    context=[stock_symbol]
)
news_agent.print_do(news_task)
