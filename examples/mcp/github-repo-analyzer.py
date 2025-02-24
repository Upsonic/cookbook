"""
export OPENAI_API_KEY="YOUR_OPENAI_API_KEY" 

If you use Azure;

export AZURE_OPENAI_API_KEY="YOUR_AZURE_OPENAI_API_KEY" 
export AZURE_OPENAI_ENDPOINT="YOUR_AZURE_OPENAI_ENDPOINT"
export AZURE_OPENAI_MODEL_NAME="YOUR_AZURE_OPENAI_MODEL_NAME"
export AZURE_OPENAI_DEPLOYMENT="YOUR_AZURE_OPENAI_DEPLOYMENT"
export AZURE_OPENAI_API_VERSION="YOUR_AZURE_OPENAI_API_VERSION"

# 📂 GitHub Repo Analyzer
This agent retrieves key project details from a GitHub repository, including latest commits, open pull requests, and unresolved issues.

## 🚀 Features
- Fetches the latest commits from a repository
- Lists open pull requests and unresolved issues

## 🔧 Installation

🟥 Ensure you set up your GITHUB API key before running the agent.

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
project_management_agent = Agent("GitHub Repo Analyzer", model="openai/gpt-4o", reflection=True)  # If using Azure, set model="azure/gpt-4o"

# MCP Server Configurations
class GitHubMCP:
    command = "npx"
    args = ["-y", "@modelcontextprotocol/server-github"]
    env = {"GITHUB_PERSONAL_ACCESS_TOKEN": "YOUR_GITHUB_PERSONAL_ACCESS_TOKEN_HERE"}

# Define response format
class ProjectDetailsResponse(ObjectResponse):
    latest_commits: list[str]
    open_pull_requests: list[str]
    open_issues: list[str]

# Define repository to analyze
repo = "https://github.com/Upsonic"

# Task to retrieve project details
project_task = Task(
    "Retrieve the latest commits, open pull requests, and unresolved issues for the repository repo.",
    tools=[GitHubMCP],
    response_format=ProjectDetailsResponse,
    context=[repo]
)

project_management_agent.print_do(project_task)
