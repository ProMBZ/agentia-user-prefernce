# graph_definition.py

from typing_extensions import TypedDict
from langgraph.graph import StateGraph, node, START, END
from front_end_agent import front_end_agent

class ConversationState(TypedDict):
    user_message: str
    response: str

graph_builder = StateGraph(ConversationState)

graph_builder.add_node("front_end_agent", node(front_end_agent))

graph_builder.add_edge(START, "front_end_agent")
graph_builder.add_edge("front_end_agent", END)

graph = graph_builder
