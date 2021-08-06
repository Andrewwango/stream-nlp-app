import sys, sqlite3
import pandas as pd
import analytics

if len(sys.argv) != 2:
    print("Usage: python main.py <filename>")
    sys.exit(1)

fn = sys.argv[1]
f = open(fn, "r")
text_raw = f.read()
text_list, punctuation_positions = analytics.text_to_list(text_raw)
f.close()

#Raw sentiment
overall_sentiment = analytics.detect_sentiment(text_raw)

#Chunk sentiment
chunk_sentiments = [analytics.detect_sentiment(text_chunk)["code"] for text_chunk in text_list]

#Output data (TODO: eventually to SQL)
#pd.DataFrame({"Sentiment": chunk_sentiments, "Position": punctuation_positions}).to_csv(fn + "_results.csv")

conn = sqlite3.connect('database/analytics_results.db')
cur = conn.cursor()

chunk_entries = [(fn, chunk, punctuation_positions[i]) for i,chunk in enumerate(chunk_sentiments)]
cur.executemany('INSERT INTO chunk_sentiment VALUES (?,?,?)', chunk_entries)
cur.execute("INSERT INTO overall_sentiment VALUES (?,?,?)", (fn, overall_sentiment["code"], overall_sentiment["sentiment"]))
cur.execute("INSERT INTO metadata VALUES (?,?)", (fn, None))
conn.commit()
conn.close()

