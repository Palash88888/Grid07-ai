from langchain.tools import tool

@tool
def mock_searxng_search(query: str) -> str:
    if "ai" in query.lower():
        return "OpenAI releases new model replacing developers"
    if "crypto" in query.lower():
        return "Bitcoin hits all-time high"
    return "Tech innovation continues"
