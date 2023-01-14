# Dash app libraries
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import base64
import dash_table

# Making table quickly
import pandas as pd

# Listing manually all the apps created

derivatives = ["European option", 
               "European option",
               "Asian option",
               "Exchange option"]

models      = ["Black-Scholes-Merton",
               "Cox-Ross Rubinstein",
               "Cox-Ross Rubinstein" , 
               "Black-Scholes-Merton"]

URLs        = [html.A(html.P("eu-option-bsm"),href="https://eu-option-bsm.onrender.com", target="_blank"), 
               html.A(html.P('eu-option-crr'),href="https://eu-option-crr.onrender.com", target="_blank"), 
               html.A(html.P("asian-option-crr"),href='https://asian-option-crr.onrender.com', target="_blank"), 
               html.A(html.P("exchange-option-bsm"),href='https://exchange-option-bsm.onrender.com', target="_blank")]

authors     = ["Michel Vanderhulst",
               "Michel Vanderhulst",
               "Michel Vanderhulst",
               "Michel Vanderhulst"]

# Would be a nice addition, idk how to do it. I imagine getting from github the last commit date from each app?                
lastupdated = ["2021/01/04","2021/02/11","2021/02/11","2021/02/14"]

# Building the table fromm all apps info
dictionary={"Derivative":derivatives,"Model":models,"URL":URLs,"Author":authors}
df=pd.DataFrame(dictionary)

# making Dash table out of pandas table
table=dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True)

# Creating the app body
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
                                    This app lists financial derivatives replication strategies web applications. Their goal is to illustrate through visuals the investment strategies that replicates the derivatives prices, i.e. proving they are arbitrage-free.
                                    """
                                      ),
                                html.Br(),
                                html.P(
                                  """
                                  Note: the apps are turned off by default. Upon startup, it can take between 10 to 30 seconds to load. It will then run at full speed.
                                  """),
                                html.Br(),
                                html.Div(table)])
                                 ),
                        dcc.Tab(
                          label="Origin",
                          value="Origin",
                          children=[html.Div(children=[
                            html.Br(),
                            html.H4("Origin of apps and methodology", style={"text-align":"center"}),
                            html.P([
                              """
                              The web applications were done by Michel Vanderhulst in 2020/2021 for his Master's Thesis under the supervision of Prof. Frédéric Vrins at the Louvain School of Management.
                              Their goal is for future students' thesis to continue updating and adding new derivatives' replication strategies. 
                              """]),
                            html.Br(),
                            html.P([
                              """
                              The first four web apps have as support the written Master's thesis. The full mathematical proofs and explanations, along the applications' developments (and step-by-step methodology to build one) can be found there. 
                              """]),
                            html.Br(),
                            html.P(["The source code of the apps can be found at ", html.A("github.com/MichelVanderhulst",href="https://github.com/MichelVanderhulst?tab=repositories", target="_blank"),"."])
                            ])]),
                      #
                      #
                  
    ],),], style={"display":"flex", 'margin':"20px", 'transform':'translateX(+30%)', "width":"60%"}), 
  ])


