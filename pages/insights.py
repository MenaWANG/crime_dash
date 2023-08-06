#from __future__ import annotations
import pandas as pd
import pathlib
import re
import plotly.express as px
import dash
import warnings
from dash import dcc, html, callback
from dash_bootstrap_templates import load_figure_template
import dash_bootstrap_components as dbc
import dash_loading_spinners as dls
from dash.dependencies import Input, Output

# dash.register_page(__name__, path='/', name='EDA')
dash.register_page(
    __name__,
    path='/insights',
    title="Insights",
)

load_figure_template("minty")

warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action="ignore", category=pd.errors.PerformanceWarning)

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("data").resolve()

#  axis formatting
axis_font = dict(
        showline=True,
        showgrid=False,
        showticklabels=True,
        linecolor='rgb(204, 204, 204)',
        zeroline=False,
        linewidth=2,
        ticks='outside',
        tickfont=dict(
            family='San-Serif',
            size=12,
            # color='black',
        ),
    )

def wrangle_LGA_subdivision(file):
    pass
    

layout = dbc.Container(
    [   
        # ======================= Title 1
        dbc.Row(
            [
                dbc.Col([
                    html.H2(
                        "LGA with the Most Increase in Crime (under construction)",
                        style={"font-weight": "bold","color": "#21386E"},
                        className="text-center mb-4",),
                    html.H2(
                        "LGA with the Most Decrease in Crime (under construction)",
                        style={"font-weight": "bold","color": "#21386E"},
                        className="text-center mb-4",),
                    ]
                ),
            ]
        ),
    ]
)