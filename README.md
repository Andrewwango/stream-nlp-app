# Sentiment analysis for pieces of text.

- NLP pipelines using HuggingFace Transformers.
- NLP bundled into API using FastAPI.
- Analysis results stored in SQLite RDB.
- Live visualisation with Plotly Dash dashboard.

Installation:
`pip install pandas uvicorn transformers fastapi dash`

Get started:
1. Start API: `uvicorn api.api:app --reload`
2. Start Dash dashboard: `python dashboard.py`
3. Ingest files and run analytics: `python ingest.py "input/test.txt"`
4. Refresh dashboard to show results.

