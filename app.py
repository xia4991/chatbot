import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.environ["MINIMAX_API_KEY"],
    base_url="https://api.minimax.chat/v1",
)

SYSTEM_PROMPT = """You are a friendly and knowledgeable assistant for a clothing store.
Your role is to help customers with:
- Finding the right clothes based on their style, occasion, or budget
- Advice on sizing, fit, and how to combine outfits
- Information about fabrics, care instructions, and product quality
- Current trends and seasonal recommendations
- Store policies such as returns, exchanges, and shipping

Always be warm, approachable, and helpful. If a customer is unsure what they want, ask a few friendly questions to better understand their needs. Keep responses concise and practical."""

st.title("👗 Clothing Store Assistant")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Render existing messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Handle new user input
if prompt := st.chat_input("Message MiniMax..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                model="MiniMax-Text-01",
                messages=[{"role": "system", "content": SYSTEM_PROMPT}] + st.session_state.messages,
                max_tokens=1024,
            )
            reply = response.choices[0].message.content

        st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
