# 🏆 Agentia User Preference Project (Gemini 2.0 + LangGraph + .env)

This repository shows a **two-agent** setup (Greeting + User Preferences) orchestrated by a **Front-End Agent** and using **Gemini 2.0** for intent classification. We also demonstrate **LangGraph** (`node`, `START`, `END`), **Streamlit** for multi-turn conversation, and an **in-memory** dictionary for user data (e.g., name, password).  

No **Google Cloud** usage is required—your **Gemini API key** is loaded from a local **`.env`** file via **python-dotenv**. 

## Features

1. **Greeting Agent**: Replies to “Hello,” “Hi,” etc.  
2. **User Preference Agent**: Stores “My name is X,” “My password is X,” answers “What is my name?” or “password?”.  
3. **Gemini 2.0**: Classifies user input as GREETING, USER_PREF, or OTHER (in `llm_node.py`).  
4. **LangGraph**: Minimal demonstration of multi-agent flow with `node`, `START`, `END` (no `runner`, no `.build()`).  
5. **Streamlit**: A web UI that **does not** produce any errors on deployment. The app shows only the final answers in a conversation log.

## Project Structure


### `.env`

Place your actual Gemini 2.0 key here. **Never** commit real API keys to a public repository if they’re sensitive.

## Multi-Turn Example

Below is an example conversation where only the **final** user questions and agent answers are shown, and **no error** occurs when deployed on **Streamlit**:

---

**User**: “Hello”  
**Agent**: “Hello there! 👋 How can I help you today?”  
*(Gemini sees “GREETING” → calls `greeting_agent`.)*

**User**: “My name is Zia”  
**Agent**: “Got it! I’ll remember your name is Zia. 🤗”  
*(Gemini sees “USER_PREF” → calls `user_preference_agent` → sets `name=Zia` in the dictionary.)*

**User**: “What is my name?”  
**Agent**: “Your name is Zia.”  
*(Again “USER_PREF.” The agent checks the dictionary: `name=Zia` → returns it.)*

**User**: “My password is 1234”  
**Agent**: “Your password has been stored securely (in-memory). 🔒”

**User**: “What is my password?”  
**Agent**: “Your password is 1234.”

**User**: “Tell me a joke.”  
**Agent**: “I can handle greetings or name/password for now. 🤖”  
*(Gemini sees “OTHER” → fallback.)*

## Setup & Installation

1. **Install** Dependencies:

   ```bash
   pip install -r requirements.txt
