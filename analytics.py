import requests

def detect_sentiment(text):
    return requests.get('http://127.0.0.1:8000/detect_sentiment/', params={'text':text}).json()


def text_to_list(text):
    return text.split(".")