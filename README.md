# 🤖 Agentic Financial AI Assistant
An advanced financial AI assistant built with a multi-agent architecture using the Phidata framework. This project demonstrates how to create a collaborative team of specialized AI agents that can perform complex financial analysis by fetching real-time stock data and searching the web. The agents are powered by the high-speed Grok LLM and can be deployed and tested in an interactive playground.

# ✨ Key Features
Multi-Agent System: Implements two specialized agents that work together as a team:

Financial Agent: Uses the YFinance tool to fetch detailed stock information, including analyst recommendations, company news, and fundamentals.

Web Search Agent: Uses the DuckDuckGo tool to perform general web searches for supplementary information, always citing its sources.

Agentic Workflows: Leverages Phidata to define complex workflows, enabling seamless collaboration between agents to answer multifaceted queries.

High-Speed LLM Integration: Powered by the Grok LLM (e.g., Llama 3 70B) for incredibly fast inference and response generation.

Real-Time Data: Fetches up-to-the-minute financial data using the yfinance library.

Interactive Playground: Can be easily deployed to the Phidata Playground, providing an interactive chat interface for real-time testing and interaction.

API-Ready: Built with FastAPI, allowing the agentic system to be exposed as an API for easy integration into other applications.

# ⚙️ Tech Stack
Agent Framework: Phidata

Large Language Model (LLM): Grok (via groq-sdk)

Financial Data Tool: YFinance (yfinance)

Web Search Tool: DuckDuckGo Search (duckduckgo-search)

API & Serving: FastAPI, Uvicorn

Environment Management: Python-dotenv, Conda (optional)

Development Environment: VS Code

# 🛠️ How It Works
The system operates by delegating tasks to the most suitable agent, which then uses its equipped tools to gather information.

User Query: The user submits a query through the command line or the Phidata Playground (e.g., "Compare Tesla and Nvidia and provide analyst recommendations").

Agent Orchestration: The Phidata framework receives the query and routes it to the multi-agent team.

Task Delegation & Tool Use:

The Financial Agent is activated for tasks requiring stock data. It calls the YFinanceTool to fetch news, fundamentals, and recommendations for the specified tickers (e.g., 'TSLA', 'NVDA').

The Web Search Agent is activated for broader, qualitative questions. It uses the DuckDuckGoSearch tool to find relevant articles or information.

LLM Processing: The data retrieved from the tools is fed into the Grok LLM, which synthesizes the information based on the instructions given to each agent (e.g., "display financial data in tables").

Collaborative Response: The agents combine their findings to generate a single, comprehensive response that addresses all parts of the user's query.

Output: The final, formatted answer is returned to the user in the interactive interface or printed to the console.

# 🔧 Getting Started
Prerequisites
Python 3.9+

API Keys: You will need API keys from the following services:

Grok: GROQ_API_KEY

Phidata: PHIDATA_API_KEY

Installation
Clone the repository:

Create and activate a Python virtual environment:

Install the required dependencies:

Set up your environment variables:

Create a .env file in the root directory of the project.

Add your API keys to the file:

# 📖 Usage
You can interact with the financial agent in two ways:

1. Command-Line Interface (CLI)
Run the agent directly from your terminal to get an immediate response to a predefined query within the script.

2. Phidata Playground (Recommended)
Deploy the agent to an interactive web interface for dynamic, real-time conversations.

Start the local server:

Connect to the Playground:

Go to the .

Connect to your local application by providing the local server URL (usually http://localhost:8000).

Start asking financial questions!

Example Queries:

"Summarize analyst recommendations and share the latest news for NVDA."

"What are the key fundamentals for Microsoft?"

"Compare the recent performance of GOOGL and META."
