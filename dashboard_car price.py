import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import os
from threading import Timer
import webbrowser
import plotly.express as px
from dash import no_update
auto_data=pd.read_csv('automobileEDA.csv')
auto_data=auto_data.groupby(['drive-wheels', 'body-style'],as_index=False).mean()
app=dash.Dash()
app.layout=html.Div(children=[html.H1('Car Automobile Components',style={'textAlign':'center','color':'black',
                                                                    'font-size':24}),
                              html.Div([
                              html.H2('Drive Wheels Type:',style={'margin-right':'2em'}),
                              dcc.Dropdown(id='demo-dropdown',options=[{'label':'Rear wheel Drive','value':'rwd'},
                                                                       {'label':'Front Wheel Drive','value':'fwd'},
                                                                       {'label':'Four Wheel Drive','value':'4wd'}
                                                                       ],value='rwd'),
                              html.Div([html.Div([],id='plot-1'),
                                        html.Div([],id='plot-2')],style={'display':'flex'}),

])
                              ])
@app.callback([Output(component_id='plot-1',component_property='children'),
               Output(component_id='plot-2',component_property='children')],
              Input(component_id='demo-dropdown',component_property='value'))
def display_selected_drive_charts(value):
    filtered_df = auto_data[auto_data['drive-wheels'] == value].groupby(['drive-wheels', 'body-style'], as_index=False).mean()

    filtered_df = filtered_df

    fig1 = px.pie(filtered_df, values='price', names='body-style', title="Pie Chart")
    fig2 = px.bar(filtered_df, x='body-style', y='price', title='Bar Chart')

    return [dcc.Graph(figure=fig1),dcc.Graph(figure=fig2)]
def open_browser():
    if not os.environ.get("WERKZEUG_RUN_MAIN"):
        webbrowser.open_new('http://127.0.0.1:8050/')

if __name__ == "__main__":
    Timer(1, open_browser).start()
    app.run_server(debug=True, port=8050)