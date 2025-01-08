# app.py

import streamlit as st
from front_end_agent import front_end_agent

def main():
    st.title("👋 Agentia User Preference")
    st.markdown("""
Features :
- Broaden matching in user_preference_agent.py (no matter how you say "What is my name?").
- Add a fallback check in llm_node.py if Gemini says OTHER but text includes "name"/"password".
- Show only the single final response (no conversation log).
    """)

    if "last_response" not in st.session_state:
        st.session_state["last_response"] = ""

    user_text = st.text_input("Type something (e.g. 'What’s my name?', 'My name is Muhammad'):")

    if st.button("Send"):
        # Orchestrate
        state = {"user_message": user_text, "response": ""}
        result = front_end_agent(state)

        # Update only the final response
        st.session_state["last_response"] = result["response"]

    # Display just the single final agent response
    st.write(st.session_state["last_response"])

if __name__ == "__main__":
    main()
