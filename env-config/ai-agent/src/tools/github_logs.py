import os
from github import Github
from langchain.tools import tool

@tool
def github_logs_tool(repo_name: str = "DV1-321/env-config"):
    """
    Fetches and summarizes logs from the most recent failed GitHub Action run.
    Use this tool when a deployment or build fails in the CI/CD pipeline.
    """
    # Get token from environment variables
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        return "Error: GITHUB_TOKEN environment variable is not set."

    try:
        g = Github(token)
        repo = g.get_repo(repo_name)
        
        # Fetch the latest failed workflow runs
        failed_runs = repo.get_workflow_runs(status="failure")
        
        if failed_runs.totalCount == 0:
            return f"No failed workflow runs found for {repo_name}."

        latest_run = failed_runs[0]
        run_info = (
            f"Failed Run ID: {latest_run.id}\n"
            f"Event: {latest_run.event}\n"
            f"Conclusion: {latest_run.conclusion}\n"
            f"URL: {latest_run.html_url}\n"
        )
        
        return f"Found a failure in the latest run:\n{run_info}"

    except Exception as e:
        return f"Failed to fetch GitHub logs: {str(e)}"