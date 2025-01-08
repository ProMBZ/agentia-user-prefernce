# front_end_agent.py

from greeting_agent import greeting_agent
from user_preference_agent import user_preference_agent

def front_end_agent(user_text: str, state: dict) -> dict:
    """
    The Front-End Orchestration Agent:
    1) Receives the user_text and a conversation state (dict).
    2) Decides if it's a greeting or user preference request (rule-based).
    3) Calls the relevant agent and returns {"response": ...}.
    """

    text_lower = user_text.lower().strip()

    # Check for greeting
    known_greetings = ["hello", "hi", "hey", "good morning", "good afternoon"]
    if any(g in text_lower for g in known_greetings):
        answer = greeting_agent(user_text)
        return {"response": answer}

    # Otherwise assume user preference if it references "name", "password", "location", "interest", or "user id"
    # (in a real system, you might do LLM classification or more advanced logic)
    if any(keyword in text_lower for keyword in ["name", "password", "live in", "interest", "user id", "login token"]):
        answer = user_preference_agent(user_text, state)
        return {"response": answer}

    # Fallback
    return {"response": "I can handle greetings or your user preferences (name, location, interests, etc.)."}

