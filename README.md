# Claude Chatbot

A simple chatbot web app powered by the MiniMax API with a Streamlit UI.

## Prerequisites

- Python 3.8+
- A [MiniMax API key](https://platform.minimax.chat)

## Setup

1. **Clone the repo and navigate into it**

   ```bash
   cd chatbot
   ```

2. **Create and activate a virtual environment**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set your API key**

   ```bash
   export MINIMAX_API_KEY=your_key_here  # On Windows: set MINIMAX_API_KEY=your_key_here
   ```

## Run

```bash
streamlit run app.py
```

The app will open automatically at `http://localhost:8501`.

## Project Structure

```
app.py            # Main application
requirements.txt  # Python dependencies
.env.example      # API key template
```
