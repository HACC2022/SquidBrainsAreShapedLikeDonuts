# Taken from: https://github.com/alanjones2/Flask-Plotly/tree/main/plotlycallback-gm

from flask import Flask, config, render_template, request, session
import pandas as pd

# Bug 14 fix: https://www.geeksforgeeks.org/python-import-from-parent-directory/
import sys
import os

# getting the name of the directory
# where the this file is present.
current = os.path.dirname(os.path.realpath(__file__))

# Getting the parent directory name
# where the current directory is present.
parent = os.path.dirname(current)

# adding the parent directory to
# the sys.path.
sys.path.append(parent)

# our libaries
from brains.viz import plotly_viz as pp
from brains.data import url as url
from brains.data import summary as summary


app = Flask(__name__)
# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'SquidBrainsAresShapedLikeDonuts' # this is so we can use "session"


def df_session_load(): # because we will do this often, just want a fast way to get it back to a df
    return url.path_to_dataframe(session['path'])


def update_data(form):
    """Update the dataframe"""

    session['path'] = form['fname']
    return


def get_features(form):
    """Update the dataframe"""

    print("form:")
    print(form)
    session['selected'] = form.getlist('selected')
    session['plot_type'] = form.get('plot_type')
    return


@app.route('/', methods=['GET','POST'])
def index():

    if request.method == 'POST':
        if request.form['button'] == "fetch_data":
            print('Fetching data...')

            # parse data
            update_data(request.form)
            df = df_session_load()

            # make summary
            df_summary = summary.df_summary(df)

            # update page
            return render_template('select.html', tables=[df_summary.to_html(classes='data')], titles=df.columns.values)
        elif request.form['button'] == "plot":
            print('plotting data...')

            # parse data
            get_features(request.form)
            df = df_session_load()

            # make summary
            df_summary = summary.df_summary(df)

            # update page
            return render_template('plot.html', graphJSON=plot(),tables=[df_summary.to_html(classes='data')], titles=df.columns.values)
        else:
            # TODO add reset button to each page
            print('resetting...')
            return render_template('start.html')
            pass
    else:
        return render_template("start.html")


def plot(): # TODO add plot type and feature selection trhough callbacks

    # try:
    df = df_session_load()

    if session['plot_type'] == "histogram":
        fig = pp.histogram(df[session['selected']])
    elif session['plot_type'] == "bar":
        fig = pp.bar(df[session['selected']])
    elif session['plot_type'] == "pie":
        fig = pp.pie(df[session['selected']])
    elif session['plot_type'] == "line":
        fig = pp.line(df[session['selected']])
    else:
        fig = None

    return fig
