# Taken from: https://github.com/alanjones2/Flask-Plotly/tree/main/plotlycallback-gm

from flask import Flask, config, render_template, request
import pandas as pd
import json
import plotly
import plotly.express as px

# from brains.data import url
# from brains.viz import plotly_plots as pp

app = Flask(__name__)


@app.route('/callback', methods=['POST', 'GET'])
def cb():
    return gm(request.args.get('data'))


@app.route('/')
def index():
    return render_template('chartsajax.html', graphJSON=gm())


def gm(country='United Kingdom'):
    df = pd.DataFrame(px.data.gapminder())
    path = "sample_data/example.csv"
    # df = url.path_to_dataframe(path)

    # fig = pp.histogram(df['Age'])

    fig = px.line(df[df['country'] == country], x="year", y="gdpPercap")

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    print(fig.data[0])
    # fig.data[0]['staticPlot']=True

    return graphJSON