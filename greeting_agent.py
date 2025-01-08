# greeting_agent.py

def greeting_agent(user_text: str) -> str:
    """
    A specialized agent for greeting:
    - If it detects a known greeting phrase, returns a friendly response.
    - Otherwise, fallback.
    """

    text_lower = user_text.lower().strip()
    known_greetings = ["hello", "hi", "hey", "good morning", "good afternoon"]

    if any(greet in text_lower for greet in known_greetings):
        return "Hello there! 👋 How can I help you today?"
    else:
        return "I only handle greetings (hello, hi, etc.) right now."
