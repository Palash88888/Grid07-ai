import json
from typing import TypedDict
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, END
from app.services.mock_tools import mock_searxng_search

llm = ChatOpenAI(model="gpt-4o-mini")

class State(TypedDict):
    bot_id: str
    topic: str
    search_query: str
    search_result: str
    post_content: str


def decide(state):
    return {
        "topic": "AI jobs",
        "search_query": "AI replacing developers"
    }


def search(state):
    result = mock_searxng_search.invoke(state["search_query"])
    return {"search_result": result}


def generate(state):
    prompt = f"""
    You are {state['bot_id']}.
    Context: {state['search_result']}

    Generate a strong opinionated post under 280 characters.

    Return ONLY JSON:
    {{
      "bot_id": "{state['bot_id']}",
      "topic": "{state['topic']}",
      "post_content": "..."
    }}
    """

    res = llm.invoke(prompt)

    try:
        return json.loads(res.content)
    except:
        return {
            "bot_id": state["bot_id"],
            "topic": state["topic"],
            "post_content": res.content[:200]
        }


def build_graph():
    graph = StateGraph(State)

    graph.add_node("decide", decide)
    graph.add_node("search", search)
    graph.add_node("generate", generate)

    graph.set_entry_point("decide")
    graph.add_edge("decide", "search")
    graph.add_edge("search", "generate")
    graph.add_edge("generate", END)

    return graph.compile()


graph = build_graph()


def generate_post(bot_id: str):
    return graph.invoke({"bot_id": bot_id})
