# llm_node.py

import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import SystemMessage, HumanMessage

from greeting_agent import greeting_agent
from user_preference_agent import user_preference_agent

# Load environment variables (GEMINI_API_KEY) from .env
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "missing_key")

def llm_node(state: dict) -> dict:
    """
    Uses Gemini 2.0 to classify user_text as GREETING, USER_PREF, or OTHER.
    Then calls greeting_agent or user_preference_agent accordingly.
    If classification is 'OTHER' but we see "name" or "password" in the text,
    we fallback to user_preference_agent (to handle partial or mis-labeled queries).
    """

    user_text = state["user_message"]
    text_lower = user_text.lower()

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash-exp",
        temperature=0.0,
        api_key=GEMINI_API_KEY
    )

    system_prompt = """You are an intent classification assistant.
Possible intents:
- GREETING (if user is greeting, e.g. "Hello", "Hey")
- USER_PREF (if user refers to name or password, e.g. "My name is ...", "What is my name?", etc.)
- OTHER (anything else)

Analyze the user's message and return ONLY one label: GREETING, USER_PREF, or OTHER.
"""

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_text),
    ]

    classification = llm(messages).content.strip().upper()

    # Fallback check: if classification is OTHER but we see 'name' or 'password', forcibly route to user preference
    if classification == "OTHER":
        if ("name" in text_lower) or ("password" in text_lower):
            classification = "USER_PREF"

    if classification == "GREETING":
        final_response = greeting_agent(user_text)
    elif classification == "USER_PREF":
        final_response = user_preference_agent(user_text)
    else:
        # If still 'OTHER', fallback
        final_response = "I can handle greetings or name/password for now. 🤖"

    return {"response": final_response}
