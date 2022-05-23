from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_csv('data/output.csv')

fig = px.line(df, x = 'date', y = 'sales', title='Sales History (ALL REGIONS)')

app.layout = html.Div(
    style= {'textAlign': 'center', 'font-family': 'Helvetica, sans-serif',},
    children=[
        html.Div(
            style={'margin': '30px 0 20px 0', 'font-size': '20px'},
    children=[
        html.H1("Soul Foods - Pink Morsel Historic Sales"),
    ]),
        dcc.Graph(id = 'graph', figure=fig, style={
        'backgroundColor': '#f5f5f5',
        'height': '500px',
        'width': '100%',
    }),
        dcc.RadioItems(
        id='region-select',
        options=[
            {'label': 'All', 'value': 'all'},
            {'label': 'North', 'value': 'north'},
            {'label': 'South', 'value': 'south'},
            {'label': 'East', 'value': 'east'},
            {'label': 'West', 'value': 'west'}
        ],
        value='all',
    
        )
    ]
)

@app.callback(
    Output('graph', 'figure'),
    [Input('region-select', 'value')])

def update_graph(region):
    if region == 'all':
        return fig
    else:
        df_regionalised = df[df['region'] == region]
        
        fig_regionalised = px.line(df_regionalised, x='date', y='sales', title="Sales History (" + region.upper() + " region)")
        return fig_regionalised


if __name__ == '__main__':
    app.run_server(debug=True)