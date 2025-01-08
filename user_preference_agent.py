# user_preference_agent.py

# Minimal in-memory dictionary for one user (user_id=1)
user_data = {
    1: {"name": None, "password": None}
}

def user_preference_agent(user_text: str) -> str:
    """
    Manages storing/retrieving the user's 'name' and 'password'.
    Supports flexible detection of:
      - "My name is X"
      - "My password is X"
      - "What is my name?" or variants
      - "What is my password?" or variants
    """

    current_user_id = 1
    profile = user_data[current_user_id]

    # Normalize the text to catch more variations
    # e.g., "What's my name?" => "what is my name?"
    text_lower = (
        user_text.lower()
        .replace("?", "")
        .replace("'s", " is")
        .strip()
    )
    # Now text_lower might be: "what is my name"

    # 1) Storing name
    if "my name is" in text_lower:
        # Extract name after "my name is"
        name = text_lower.split("my name is")[-1].strip()
        # But use original user_text for the actual name if you prefer exact casing:
        # name = user_text.split("my name is")[-1].strip()
        # (Your choice. Below we just do everything in lowercase for simplicity.)
        profile["name"] = name
        return f"Got it! I'll remember your name is {name}. 🤗"

    # 2) Storing password
    elif "my password is" in text_lower:
        password = text_lower.split("my password is")[-1].strip()
        profile["password"] = password
        return "Your password has been stored securely (in-memory). 🔒"

    # 3) Retrieving name
    elif "what" in text_lower and "my" in text_lower and "name" in text_lower:
        if profile["name"]:
            return f"Your name is {profile['name']}."
        else:
            return "I don’t know your name yet. Please say 'My name is ...'."

    # 4) Retrieving password
    elif "what" in text_lower and "my" in text_lower and "password" in text_lower:
        if profile["password"]:
            return f"Your password is {profile['password']}."
        else:
            return "I don’t have your password yet. Please say 'My password is ...'."

    # Otherwise fallback
    return "I can handle your name/password. Try 'My name is John' or 'What is my password?'."
