import os
import time
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

with st.sidebar:
    st.header("Token Usage")
    if st.session_state.get("last_usage"):
        u = st.session_state.last_usage
        st.markdown("**Last message**")
        st.text(f"  Prompt:    {u.prompt_tokens}")
        st.text(f"  Response:  {u.completion_tokens}")
        st.divider()
    st.markdown("**Session total**")
    st.text(f"  Tokens:    {st.session_state.get('total_tokens', 0)}")

st.title("👗 Clothing Store Assistant")

# Initialize chat history and token tracking
if "messages" not in st.session_state:
    st.session_state.messages = []
if "total_tokens" not in st.session_state:
    st.session_state.total_tokens = 0
if "last_usage" not in st.session_state:
    st.session_state.last_usage = None
if "last_message_time" not in st.session_state:
    st.session_state.last_message_time = 0

# Render existing messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

COOLDOWN = 5  # seconds between messages

# Handle new user input
if prompt := st.chat_input("Message MiniMax..."):
    now = time.time()
    elapsed = now - st.session_state.last_message_time
    if elapsed < COOLDOWN:
        remaining = int(COOLDOWN - elapsed) + 1
        st.warning(f"Please wait {remaining}s before sending another message.")
    else:
        st.session_state.last_message_time = now
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
                usage = response.usage
                st.session_state.last_usage = usage
                st.session_state.total_tokens += usage.prompt_tokens + usage.completion_tokens

            st.markdown(reply)

        st.session_state.messages.append({"role": "assistant", "content": reply})
