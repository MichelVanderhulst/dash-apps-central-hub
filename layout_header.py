import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import base64

bg_color="#506784",
font_color="#F3F6FA"

def header():
	return html.Div(
                id='app-page-header',
                children=[html.Div(children=[html.Div(children=[html.H3("Derivatives replication strategies central hub")],
                                                      # style={'width': '100%', 'display': 'inline-block'}
                                                     ),
                    	                   # html.H4("Black-Scholes-Merton model")
                                            html.Div(children=[dbc.Button("About", id="popover-target", outline=True, style={"color":"white", 'border': 'solid 1px white'}),
                                                               dbc.Popover(children=[dbc.PopoverHeader("About"),
                                                                                     dbc.PopoverBody(children=["Michel Vanderhulst",
                                                                                                               html.Br(),                           
                                                                                                              "michelvanderhulst@student.uclouvain.be ",
                                                                                                               html.Hr(), 
                                                                                                               "This app was built for my Master's Thesis, under the supervision of Prof. Frédéric Vrins (frederic.vrins@uclouvain.be)."
                                                                                                              ],
                                                                                                    style={"max-width": "100%", }
                                                                                                    
                                                                                                    ),
                                                                                    ],
                                                                            id="popover",
                                                                            is_open=False,
                                                                            target="popover-target"),
                                                               ],
                                                     style={'display': 'flex', "margin-left": "58%"}
                                                    )
                                            ],
                       		       style={"display":"flex", "font-family":'sans-serif'}
                                   )],
                		 
                style={
                    'background': bg_color,
                    'color': font_color,
                    'padding':20,
                    'margin':'-10px',
                }
            )
