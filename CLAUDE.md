# Chatbot Project

A simple chatbot web app built with Python, Claude API, and Streamlit.

## Stack

- **Python** with a `.venv` virtual environment
- **Anthropic SDK** (`anthropic`) — Claude API client
- **Streamlit** — chat UI

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export ANTHROPIC_API_KEY=sk-ant-...
streamlit run app.py
```

## Project Structure

```
app.py            # Main Streamlit app
requirements.txt  # Direct dependencies (anthropic, streamlit)
.env.example      # API key template
.venv/            # Virtual environment (not committed)
```

## Key Notes

- API key is read from `ANTHROPIC_API_KEY` environment variable — never hardcode it
- Full conversation history is stored in `st.session_state.messages` and sent to Claude on every turn
- Model in use: `claude-sonnet-4-6`
