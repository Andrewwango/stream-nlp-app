from transformers import pipeline
from enum import Enum

class Sentiment(Enum):
    VERY_POSITIVE = 5
    POSITIVE = 4
    NEUTRAL = 3
    NEGATIVE = 2
    VERY_NEGATIVE = 1


class Client:
    def __init__(self):
        self.client = pipeline(task='sentiment-analysis',
        model='nlptown/bert-base-multilingual-uncased-sentiment')
    def detect_sentiment(self, text):
        result = self.client(text)[0]
        code = int(result["label"][0])
        return {"sentiment" : Sentiment(code).name, "code" : code, "confidence" : result["score"]}