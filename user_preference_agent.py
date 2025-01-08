# user_preference_agent.py

"""
User Preference Agent with:
- Context Preservation: name, location, interests...
- Authentication: user_id or token
- Extended Preferences: location, interests, password
- In-memory store (dictionary)
- Checks if data is already set before adding again
"""

# Global dictionary: { user_id: { "name": ..., "password": ..., "location": ..., "interests": [...] } }
user_data = {}

def get_user_profile(user_id: int) -> dict:
    """
    Retrieve or create a new profile dict for the given user_id.
    This ensures context preservation across multiple user queries.
    """
    if user_id not in user_data:
        user_data[user_id] = {
            "name": None,
            "password": None,
            "location": None,
            "interests": []
        }
    return user_data[user_id]

def user_preference_agent(user_text: str, state: dict) -> str:
    """
    The main function that stores/retrieves user preferences.
    - Supports authentication (user_id) stored in state.
    - Extended prefs: name, password, location, interests.
    - Avoids duplicates if user tries to set the same data again.
    - Context is preserved in user_data dict.

    Args:
        user_text (str): The user's latest message.
        state (dict): A conversation state (could hold user_id, etc.).

    Returns:
        str: The agent's response to the user.
    """

    text_lower = user_text.lower().strip()

    # Check user_id in the conversation state; default to 1 if not set
    user_id = state.get("user_id", 1)
    profile = get_user_profile(user_id)

    # 1) Check for user id / auth: "My user id is 999" or "login token 123"
    if "my user id is" in text_lower or "login token" in text_lower:
        new_id = extract_user_id(user_text)
        if new_id:
            state["user_id"] = new_id
            get_user_profile(new_id)  # ensure it's created
            return f"You're now authenticated with user_id={new_id}."
        else:
            return "I couldn't parse your user ID. Try 'My user id is 1234'."

    # 2) Storing name: "My name is X" or "Call me X"
    if ("my name is" in text_lower) or ("call me" in text_lower):
        name = extract_name(user_text)
        if name:
            if profile["name"] == name:
                return f"You already told me your name is {name}."
            else:
                profile["name"] = name
                return f"Got it! I'll remember your name is {name}."
        else:
            return "I couldn't parse your name. Try 'My name is John.'"

    # 3) Storing location: "I live in X" or "I live at X"
    if ("i live in" in text_lower) or ("i live at" in text_lower) or ("remember that i live in" in text_lower):
        location = extract_location(user_text)
        if location:
            if profile["location"] == location:
                return f"I already know you live in {location}."
            else:
                profile["location"] = location
                return f"Got it! You live in {location}."
        else:
            return "I couldn't parse your location. Try 'I live in London.'"

    # 4) Storing interest: "I have interest in soccer" or "I like soccer"
    if ("interest in" in text_lower) or ("i like" in text_lower):
        interest = extract_interest(user_text)
        if interest:
            if interest in profile["interests"]:
                return f"You already told me you're interested in {interest}."
            else:
                profile["interests"].append(interest)
                return f"Got it! I'll remember you're interested in {interest}."
        else:
            return "I couldn't parse your interest. Try 'I have interest in soccer.'"

    # 5) Storing password: "My password is 1234"
    if "my password is" in text_lower:
        password = user_text.split("my password is")[-1].strip()
        if profile["password"] == password:
            return f"I already have your password as {password}."
        else:
            profile["password"] = password
            return "Your password has been stored."

    # 6) Retrieving name: "What is my name?"
    if "what is my name" in text_lower:
        if profile["name"]:
            return f"Your name is {profile['name']}."
        else:
            return "I don't know your name yet. Try 'My name is John.'"

    # 7) Retrieving location: "What is my location?" / "Where do I live?"
    if ("what is my location" in text_lower) or ("where do i live" in text_lower):
        if profile["location"]:
            return f"You live in {profile['location']}."
        else:
            return "I don't know your location yet. Try 'I live in London.'"

    # 8) Retrieving interests: "What are my interests?"
    if "what are my interests" in text_lower:
        if profile["interests"]:
            joined = ", ".join(profile["interests"])
            return f"You're interested in: {joined}."
        else:
            return "You haven't told me about any interests yet."

    # 9) Retrieving password: "What is my password?"
    if "what is my password" in text_lower:
        if profile["password"]:
            return f"Your password is {profile['password']}."
        else:
            return "You haven't set a password yet. Try 'My password is 1234.'"

    # Fallback
    return ("I can store or retrieve your name, password, location, or interests. "
            "Try something like 'Call me John from now on.'")


# ---------------- Helper Functions ----------------

def extract_user_id(text: str) -> int:
    """
    Parse a user ID from text like "My user id is 1234" or "login token 999".
    Returns an int or None if not found.
    """
    import re
    matches = re.findall(r"\d+", text)
    if matches:
        return int(matches[-1])
    return None

def extract_name(text: str) -> str:
    """
    Extract name after "my name is" or "call me".
    """
    text_lower = text.lower()
    if "my name is" in text_lower:
        return text.split("my name is")[-1].strip()
    elif "call me" in text_lower:
        return text.split("call me")[-1].strip()
    return ""

def extract_location(text: str) -> str:
    """
    Extract location after "I live in" / "I live at" / "remember that i live in".
    """
    text_lower = text.lower()
    if "i live in" in text_lower:
        return text.split("i live in")[-1].strip()
    elif "i live at" in text_lower:
        return text.split("i live at")[-1].strip()
    elif "remember that i live in" in text_lower:
        return text.split("remember that i live in")[-1].strip()
    return ""

def extract_interest(text: str) -> str:
    """
    Extract interest after "interest in" or "i like".
    """
    text_lower = text.lower()
    if "interest in" in text_lower:
        return text.split("interest in")[-1].strip()
    elif "i like" in text_lower:
        return text.split("i like")[-1].strip()
    return ""
