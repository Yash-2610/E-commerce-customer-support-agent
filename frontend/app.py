import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)
import streamlit as st
from agent import customer_support_bot

st.set_page_config(
    page_title="Customer Support Agent",
    page_icon="🤖"
)

st.title("🤖 Customer Support Agent")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input
prompt = st.chat_input("Ask your question...")

if prompt:

    # Store user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.write(prompt)

    try:

        # Directly call your agent
        bot_reply = customer_support_bot(prompt)

    except Exception as e:

        bot_reply = f"Error: {str(e)}"

    # Store bot response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": bot_reply
        }
    )

    with st.chat_message("assistant"):
        st.write(bot_reply)