# app.py

import streamlit as st
from front_end_agent import front_end_agent

def main():
    st.title("Agentia User Preference Project")

    st.markdown("""
**Try commands**:
- "Hello" (Greeting Agent)
- "My user id is 1234" (auth user, sets user_id)
- "My name is John"
- "I live in London"
- "I like soccer"
- "What is my name?"
- "Where do I live?"
- "What are my interests?"
- "My password is 999"
- "What is my password?"
""")

    # We'll store conversation state in st.session_state
    if "conv_state" not in st.session_state:
        st.session_state["conv_state"] = {
            "user_id": 1  # default user id
        }

    user_text = st.text_input("Type your message:")
    if st.button("Send"):
        # Pass user_text + the existing conversation state
        # front_end_agent returns {"response": "..."}
        state_dict = {
            "user_id": st.session_state["conv_state"]["user_id"]
        }
        result = front_end_agent(user_text, state_dict)

        # If user_id changed inside the agent, update it
        if "user_id" in state_dict:
            st.session_state["conv_state"]["user_id"] = state_dict["user_id"]

        st.session_state["conv_state"]["last_response"] = result["response"]

    st.write("### Agent's Response:")
    if "last_response" in st.session_state["conv_state"]:
        st.write(st.session_state["conv_state"]["last_response"])

if __name__ == "__main__":
    main()
