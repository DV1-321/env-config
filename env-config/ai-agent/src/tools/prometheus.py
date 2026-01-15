import os
import requests
from langchain.tools import tool

@tool
def prometheus_tool(query: str):
    """
    Queries Prometheus for demo-app metrics. 
    Use this to check if CPU usage is hitting the 70% HPA threshold.
    """
    prometheus_url = os.getenv("PROMETHEUS_URL", "http://localhost:9090")
    # For now, we return a mock response to allow the agent to start
    return f"Metric result for '{query}': CPU usage is currently at 42%."