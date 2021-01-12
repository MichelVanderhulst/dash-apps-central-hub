import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import base64
import pandas as pd
import dash_table

derivatives = ["European option", "European option","Asian option","Exchange option"]
models=["Black-Scholes-Merton","Cox-Ross Rubinstein","Cox-Ross Rubinstein" , "Black-Scholes-Merton"]
URLs=[html.A(html.P("eu-option-bsm.herokuapp.com"),href="https://eu-option-bsm.herokuapp.com"), 
      html.A(html.P('eu-option-crr.herokuapp.com'),href="https://eu-option-crr.herokuapp.com"), 
      html.A(html.P("asian-option-crr.herokuapp.com"),href='https://asian-option-crr.herokuapp.com'), 
      html.A(html.P("exchange-option-bsm.herokuapp.com"),href='http://exchange-option-bsm.herokuapp.com')]
authors=["Michel Vanderhulst","Michel Vanderhulst","Michel Vanderhulst","Michel Vanderhulst"]
lastupdated = ["2020/10/28","2020/11/06","2020/06/20","2021/01/10"]

dictionary={"Derivative":derivatives,"Model":models,"URL":URLs,"Author":authors,"Last updated":lastupdated}
df=pd.DataFrame(dictionary)
table=dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True)

def body():
  return html.Div(children=[
            html.Div(id='left-column', children=[
                dcc.Tabs(
                    id='tabs', value='About this App',
                    children=[
                        dcc.Tab(
                            label='About this App',
                            value='About this App',
                            children=html.Div(children=[
                              html.Br(),
                                html.H4('What is this app?', style={"text-align":"center"}),
                                html.P(
                                    """
                                    This app lists financial derivatives replication strategies web applications. Their goal is to illusstrate through visuals the investment strategies that replicates the derivatives prices, i.e. proving they are arbitrage-free.
                                    """
                                      ),
                                html.Br(),
                                html.Div(table)])
                                 ),
                        dcc.Tab(
                          label="Origin",
                          value="Origin",
                          children=[html.Div(children=[
                            html.Br(),
                            html.H4("Origin of web applications and methodology", style={"text-align":"center"}),
                            html.P([
                              """
                              The web applications were done by Michel Vanderhulst in 2020/2021 for his Master's Thesis under the supervision of Prof. Frédéric Vrins at the Louvain School of Management.
                              Their goal is for future students' thesis to continue updating and adding new derivatives' replication strategies. 
                              """]),
                            html.Br(),
                            html.P([
                              """
                              The first four web apps have as support the written thesis of Michel. The full mathematical proofs and explanations, along the applications' developments (and step-by-step methodology to build one) can be found there. 
                              """]),
                            ])]),
                      #
                      #
                  
    ],),], style={'float': 'left', 'width': '97%', 'margin':"20px"}),
  ])


