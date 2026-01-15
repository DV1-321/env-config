import os
from langchain.tools import tool

@tool
def docsearch_tool(query: str):
    """
    Searches the env-config directory for Kubernetes configuration details.
    Use this to find image tags, patches, or resource definitions.
    """
    # Define the path to your config files based on your directory structure
    base_path = r"C:\Azure-Pipeline\env-config\env-config"
    results = []

    # Search logic for specific key files mentioned in your project
    targets = [
        os.path.join(base_path, "overlays", "dev", "patch-deployment.yml"),
        os.path.join(base_path, "overlays", "dev", "kustomization.yml"),
        os.path.join(base_path, "base", "deployment.yml")
    ]

    for file_path in targets:
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                content = f.read()
                if query.lower() in content.lower():
                    results.append(f"Found in {os.path.basename(file_path)}:\n{content}")

    if not results:
        return f"No direct matches for '{query}' found in the manifests."
    
    return "\n---\n".join(results)