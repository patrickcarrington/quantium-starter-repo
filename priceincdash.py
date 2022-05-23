from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)


df = pd.read_csv('data/output.csv')

fig = px.line(df, x = 'date', y = 'sales', title='Pink Morsel Sales')

app.layout = html.Div(children=[
    html.H1(children='Sales of Pink Morsel'),

    html.Div(children='''
        Sales of Pink Morsel Feb 2018-Feb 2022
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)