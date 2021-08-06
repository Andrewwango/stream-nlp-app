from plotnine import ggplot, aes, geom_line, scale_y_discrete
import pandas as pd
import sqlite3
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input
import plotly.express as px
from analytics.analytics import Sentiment

#gg = ggplot(chunk_results) + aes(x="Position", y="Sentiment") + geom_line()\
#     + scale_y_discrete(breaks=[v.value for v in analytics.Sentiment], labels=[v.name for v in analytics.Sentiment], limits=[v.value for v in analytics.Sentiment])
#print(gg)

conn = sqlite3.connect('database/analytics_results.db', check_same_thread=False)
cur = conn.cursor()

app = dash.Dash(__name__)

def serve_layout():
    cur.execute("""SELECT sentiment, sentiment_code, COUNT(*)
FROM overall_sentiment
GROUP BY sentiment_code
ORDER BY sentiment_code ASC""")
    overall_sentiment_counts_data = pd.DataFrame(cur.fetchall(), columns=["sentiment", "code", "count"])

    cur.execute("SELECT DISTINCT filename FROM chunk_sentiment")
    all_filenames = [fn[0] for fn in cur.fetchall()]

    return html.Div(
        children=[
            html.H1(children="Text Analytics",),

            html.P(
                children="Andrew Wang",
            ),

            html.A(html.Button('Refresh Data'),href='/'),

            dcc.Graph(
                figure = px.pie(overall_sentiment_counts_data, values='count', names='sentiment', title='Overall sentiment count')
            ),

            html.Div(
                children=[
                    html.Div(children="Type", className="menu-title"),
                    dcc.Dropdown(
                        id="filename-dropdown",
                        options=[
                            {"label": fn, "value": fn} for fn in all_filenames
                        ],
                        value="Hello",
                        clearable=False,
                        searchable=False,
                        className="dropdown",
                    ),
                ],
            ),

            dcc.Graph(
                id="chunk_sentiment_chart", config={"displayModeBar": False},
            ),
        ]
    )

app.layout = serve_layout

@app.callback(
    [Output("chunk_sentiment_chart", "figure"),],
    [Input("filename-dropdown", "value"),],
)
def update_charts(filename):
    cur.execute("""SELECT sentiment_code, position
FROM chunk_sentiment
WHERE filename = ?
ORDER BY position ASC
""", (filename,))

    chunk_sentiment_raw = cur.fetchall()
    chunk_sentiment_data = pd.DataFrame(chunk_sentiment_raw, columns=["code", "position"])
    chunk_sentiment_chart = px.line(chunk_sentiment_data, x="position", y="code", title='Chunk sentiment')
    chunk_sentiment_chart.update_yaxes(
    ticktext=[v.name for v in Sentiment],
    tickvals=[v.value for v in Sentiment],
)
    return [chunk_sentiment_chart,]


if __name__ == "__main__":
    app.run_server(debug=True)
