# front_end_agent.py

from llm_node import llm_node

def front_end_agent(state: dict) -> dict:
    """
    The front-end agent receives the conversation state, including 'user_message',
    and delegates to llm_node for classification. Returns updated {"response": "..."}.
    """

    return llm_node(state)
