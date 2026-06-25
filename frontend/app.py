import streamlit as st
import requests

st.set_page_config(
    page_title="Customer Support Agent",
    page_icon="🤖"
)

st.title(" Customer Support Agent")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Show previous messages
for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input
prompt = st.chat_input("Ask your question...")

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.write(prompt)

    try:

        response = requests.post(
            "http://backend:8000/chat",
            json={"message": prompt}
        )

        bot_reply = response.json()["response"]

    except Exception as e:

        bot_reply = f"Error: {e}"

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": bot_reply
        }
    )

    with st.chat_message("assistant"):
        st.write(bot_reply)