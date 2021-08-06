from fastapi import FastAPI
from .nlp import Client

app = FastAPI()
client = Client()

@app.get('/')
def get_root():
    return {"message":"root"}

@app.get('/detect_sentiment/')
async def query_detect_sentiment(text):
    return client.detect_sentiment(text)