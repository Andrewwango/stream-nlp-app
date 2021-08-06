import requests, re
from enum import Enum

def detect_sentiment(text):
    return requests.get('http://127.0.0.1:8000/detect_sentiment/', params={'text':text}).json()


def text_to_list(text):
    pat = r'[.?!]+'
    sentences = re.split(pat, text) #text.split(".")
    positions = [m.start() for m in re.finditer(pat , text)]
    if len(sentences) == len(positions) + 1:
        positions.append(len(text))
    return sentences, positions

class Sentiment(Enum):
    VERY_NEGATIVE = 1
    NEGATIVE = 2
    NEUTRAL = 3
    POSITIVE = 4
    VERY_POSITIVE = 5  
    