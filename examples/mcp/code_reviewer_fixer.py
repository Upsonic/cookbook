"""
export OPENAI_API_KEY="YOUR_OPENAI_API_KEY" 

If you use Azure;

export AZURE_OPENAI_API_KEY="YOUR_AZURE_OPENAI_API_KEY" 
export AZURE_OPENAI_ENDPOINT="YOUR_AZURE_OPENAI_ENDPOINT"
export AZURE_OPENAI_MODEL_NAME="YOUR_AZURE_OPENAI_MODEL_NAME"
export AZURE_OPENAI_DEPLOYMENT="YOUR_AZURE_OPENAI_DEPLOYMENT"
export AZURE_OPENAI_API_VERSION="YOUR_AZURE_OPENAI_API_VERSION"

# 🛠️ Code Review & Fixer
This agent reviews code repositories and analyzes error logs from Sentry for security vulnerabilities and recommended fixes.

## 🚀 Features
- Identifies security vulnerabilities and coding issues in a repository
- Retrieves and analyzes Sentry error logs for suggested fixes

## 🔧 Installation

🟥 Ensure you set up your GITHUB & SENTRY API key before running the agent.

```bash
pip install mcp-server-sentry
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
code_review_agent = Agent("Code Review & Fixer", model="openai/gpt-4o", reflection=True)  # If using Azure, set model="azure/gpt-4o"

# MCP Server Configurations
class GitHubMCP:
    command = "npx"
    args = ["-y", "@modelcontextprotocol/server-github"]
    env = {"GITHUB_PERSONAL_ACCESS_TOKEN": "YOUR_GITHUB_PERSONAL_ACCESS_TOKEN_HERE"}

class SentryMCP:
    command = "uvx"
    args = ["mcp_server_sentry", "--auth-token", "YOUR_SENTRY_AUTH_TOKEN_HERE"]

# Define response format
class CodeReviewResponse(ObjectResponse):
    repository: str
    issues: list[str]
    recommendations: list[str]

class SentryIssuesResponse(ObjectResponse):
    sentry_issues: list[str]
    recommended_fixes: list[str]

# Define repository to analyze
repo = "https://github.com/Upsonic"

# Task to review code repository
review_task = Task(
    "Analyze the repository repo for potential issues and security vulnerabilities.",
    tools=[GitHubMCP],
    response_format=CodeReviewResponse,
    context=[repo]
)
code_review_agent.print_do(review_task)

# Task to analyze Sentry error logs
sentry_task = Task(
    "Retrieve and analyze recent Sentry error logs, providing recommended fixes.",
    tools=[SentryMCP],
    response_format=SentryIssuesResponse
)
