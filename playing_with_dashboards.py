import pandas as pd
import plotly.express as px
import dash
import os
from threading import Timer
import webbrowser
import dash_html_components as html
import dash_core_components as dcc
file=pd.read_excel('another.xlsx')
df=file.groupby('Program').agg({'Program':'count'})
df=df.rename(columns={'Program':'Number of defaulters'})
df.reset_index(inplace=True)
fig1 = px.bar(df, x="Program", y="Number of defaulters", title='Roll call defaulters by Program')
file2=file.groupby('Hall').agg({'Hall':'count'})
file2=file2.rename(columns={'Hall':'Number of defaulters'})
file2.reset_index(inplace=True)
fig2=px.pie(file2,names='Hall',values='Number of defaulters',title='Roll call defaulters by Hall')
app=dash.Dash(__name__)
app.layout=html.Div(children=[html.H1("Roll call Defaulters for 300 lvl",style={'textAlign':'center','color':'blue','font-size':40}),
                              html.Div([html.Div(dcc.Graph(figure=fig1,style={'height':'97vh'})),
                                        html.Div(dcc.Graph(figure=fig2))],style={'display':'flex'})

                              ])
def open_browser():
    if not os.environ.get("WERKZEUG_RUN_MAIN"):
        webbrowser.open_new('http://127.0.0.1:8050/')

if __name__ == "__main__":
    Timer(1, open_browser).start()
    app.run_server(debug=True, port=8050)
