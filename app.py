import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

from layout_header import header
from layout_body import body


import pandas as pd
import urllib.parse

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server


app.layout = html.Div(
                id='main_page',
                children=[
                    header(),
                    body(),
                         ],
                     )


@app.callback(
    Output("popover", "is_open"),
    [Input("popover-target", "n_clicks")],
    [State("popover", "is_open")],
)
def toggle_popover(n, is_open):
    if n:
        return not is_open
    return is_open




if __name__ == '__main__':
    app.run_server(debug=True)

