# 
import json

# Dash libraries
import dash_core_components as dcc
import dash_html_components as html

def define_layout(app, metadata_div_data):
    return html.Div(
        children = 
        [   
            # MetaDataDump
            html.Div(
                id = 'metadata_div',
                children = json.dumps(metadata_div_data),
                style = {'display': 'none'}
            ),
            # Title
            html.Div(
                [
                    html.Div(
                        [
                            html.Img(
                                src=app.get_asset_url("logo_4_optimised_300.png"),
                                id="hagal-image",
                                style={
                                    "height": "90px",
                                    "width": "auto",
                                    "margin-bottom": "0px",
                                    "margin-left": "20px"
                                }
                            )
                        ],
                        className="one-third column",
                    ),
                    html.Div(
                        [
                        html.H1("Stortings Generator",
                                style={"margin-bottom": "0px","margin-top": "10px"}
                            )
                        ],
                        className="one-half column",
                        id="title"
                    )
                ],
                id="header",
                className="row flex-display",
                style={"margin-bottom": "15px"},
            ),
            # Left pane
            html.Div(
                [
                    html.Div(
                        [  
                            html.Button(
                                id='simulate_button0', 
                                children='Simulate', 
                                n_clicks=0,
                                style={'backgroundColor': '#4ea246'})
                        ],
                        id = "simulate_button0_container",
                        className = "pretty_container"
                    ),
                ],
                id = "left_top_pane",
                className="three columns"
            ),
            # Right pane
            html.Div(
                html.Div(
                    [
                        html.H4('Results',className='control_label'),
                        dcc.Graph(id='hist_000')
                    ],
                    id = "graph00",
                    className="pretty_container"
                ),
                id = 'right_pane',
                className = "nine columns"
            )   
        ]
    )