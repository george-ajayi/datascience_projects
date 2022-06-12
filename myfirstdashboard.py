import pandas as pd
import plotly.express as px
import dash
import dash_html_components as html
import dash_core_components as dcc
file=pd.read_excel('another.xlsx')
file=file.groupby('Hall').agg({'Hall':'count'})
file=file.rename(columns={'Hall':'count'})
file.reset_index(inplace=True)
fig = px.bar(file, x="Hall", y="count", title='Roll call defaulters by Hall')
app=dash.Dash(__name__)
app.layout=html.Div(children=[html.H1('Roll Call  ',style={'textAlign':'center','color':'black','font-size':40}),
                              html.P('Roll Call Defaulters In 300lvl.',style={'textAlign':'center','color':'red'}),
                              dcc.Graph(figure=fig)


                            ])
if __name__=='__main__':
    app.run_server()