import sys
import analytics
if len(sys.argv) != 2:
    print("Usage: python main.py <filename>")
    sys.exit(1)

fn = sys.argv[1]
"""
with open(fn) as jsonFile:
    parsed_json = json.load(jsonFile)
    jsonFile.close()

parsed_results = parsed_json["results"]
transcripts = parsed_results["transcripts"]

for i, t in enumerate(transcripts):
    transcript = t["transcript"]
    print("Original: ", transcript)
    response = requests.get('http://127.0.0.1:8000/detect_sentiment/', params={'text':transcript})
    print(response.json())

"""
f = open(fn, "r")
text_raw = f.read()
text_list = analytics.text_to_list(text_raw)

#Raw sentiment
print(analytics.detect_sentiment(text_raw))

#Chunk sentiment
for text_chunk in text_list:
    print(analytics.detect_sentiment(text_chunk))