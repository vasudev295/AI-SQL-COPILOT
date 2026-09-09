# QueryPilot AI

Enterprise-style Text-to-SQL & Data Analyst Copilot.

Natural language -> schema -> Gemini -> SQL guard -> execution -> visualization -> business explanation.

## Features
- Gemini Text-to-SQL
- Schema-aware prompting
- Read-only SQL guardrails
- SQLGlot validation
- Self-correction/retry
- Conversation context
- Plotly charts
- SQLite demo database
- FastAPI API
- Pytest tests

## Windows setup

```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
python data/create_database.py
streamlit run app/frontend/streamlit_app.py
```

Add your Gemini API key to `.env`.

## Demo questions
- What are the top 5 products by revenue?
- Which region generated the most revenue?
- Show monthly revenue for 2025.
- Compare revenue between North and South.
