# visualization functions

import json

import plotly
import plotly.express as px


def histogram(data,xlabel=None,ylabel="counts",title=None):
    """
    Display a histogram of the data

    :param data: e.g. a single column of dataframe (does it have to be numerical? maybe works for multiple columns)
    :param xlabel: label for x-axis
    :param ylabel:
    :param title:
    :return: display the plot
    """
    # TODO add feature selection

    fig = px.histogram(data)

    # if xlabel is not None:
    #     plt.xlabel(xlabel)
    # if ylabel is not None:
    #     plt.ylabel(ylabel)
    # if title is not None:
    #     plt.title(title)

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    print(fig.data[0])

    return graphJSON
