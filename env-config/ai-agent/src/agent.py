import os
from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent
from src.tools.github_logs import github_logs_tool
from src.tools.azure_logs import azure_logs_tool
from src.tools.prometheus import prometheus_tool
from src.tools.docsearch import docsearch_tool

# Initialize the Groq LLM (Llama 3 70B is ideal for DevOps logic)
llm = ChatGroq(
    model="llama3-70b-8192",
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY")
)

# Load capabilities defined in your directory structure
tools = [github_logs_tool, azure_logs_tool, prometheus_tool, docsearch_tool]

# Create the stateful agent executor
agent_executor = create_react_agent(llm, tools)

def run_diagnostic(prompt: str):
    """Entry point for processing infrastructure queries."""
    inputs = {"messages": [("user", prompt)]}
    return agent_executor.invoke(inputs)