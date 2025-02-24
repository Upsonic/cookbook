"""
export OPENAI_API_KEY="YOUR_OPENAI_API_KEY" 

If you use Azure;

export AZURE_OPENAI_API_KEY="YOUR_AZURE_OPENAI_API_KEY" 
export AZURE_OPENAI_ENDPOINT="YOUR_AZURE_OPENAI_ENDPOINT"
export AZURE_OPENAI_MODEL_NAME="YOUR_AZURE_OPENAI_MODEL_NAME"
export AZURE_OPENAI_DEPLOYMENT="YOUR_AZURE_OPENAI_DEPLOYMENT"
export AZURE_OPENAI_API_VERSION="YOUR_AZURE_OPENAI_API_VERSION"

# 🛒 Cheapest Product Price Finder
This agent searches multiple e-commerce platforms to find the best price for a given product.

## 🚀 Features
- Compares product prices across multiple online stores
- Returns the best available price along with product details

## 🔧 Installation
```bash
pip install upsonic browser-use playwright
```
"""

from upsonic import Agent, Task, ObjectResponse
from upsonic.client.tools import BrowserUse  # Importing BrowserUse

# Initialize the AI agent
price_finder_agent = Agent("Cheapest Product Price Finder", model="openai/gpt-4o", reflection=True) # If using Azure, set model="azure/gpt-4o"

# Define response format for individual products
class Product(ObjectResponse):
    name: str
    price: float
    url: str

# Define response format for the product list
class ProductList(ObjectResponse):
    products: list[Product]
    best_price: str

# Define e-commerce platforms and product to search
e_commerce_site1 = "Amazon" 
e_commerce_site2 = "eBay" 
e_commerce_site3 = "AliExpress"
product = "Sun Tzu The Art Of War Book"

# Task to track product prices using BrowserUse
track_task = Task(
    "Search for the product on e-commerce sites and report the best price",
    tools=[BrowserUse],
    response_format=ProductList,
    context=[e_commerce_site1, e_commerce_site2, e_commerce_site3, product]
)

price_finder_agent.print_do(track_task)
