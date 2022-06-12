import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import os
from threading import Timer
import webbrowser
import plotly.express as px
from dash.dependencies import Input, Output

app=dash.Dash(__name__)
app.layout=html.Div(children=[html.H1('Dashboard'),
            dcc.Dropdown(options=[
                {'label':'New York City','value':'NYC'},
                {'label':'Lagos','value':'NG'},
                {'label':'Ekiti','value':'Ek'}


            ],value='NYC'),
            html.Div([html.Div(dcc.Graph(id='plot1')),
                      html.Div(dcc.Graph(id='plot'))],style={'display':'center'})
                              ])
def open_browser():
    if not os.environ.get("WERKZEUG_RUN_MAIN"):
        webbrowser.open_new('http://127.0.0.1:8050/')

if __name__ == "__main__":
    Timer(1, open_browser).start()
    app.run_server(debug=True, port=8050)
