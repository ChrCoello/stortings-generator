#!/usr/local/bin/python3

# General python distribution
import json
from pathlib import Path
#import logging
import random
import pandas as pd

# 3party libraries
from dash import Dash
from dash.dependencies import Input, Output, State
import plotly.express as px


# Locally
APP_NAME = 'stortings-generator'
from utils import parse_trafo_json, rnd_to_sum_with_min
from enums import Metadata
from layout import define_layout

# Initialize app
app = Dash(
    name=__name__,
    assets_url_path='/'+APP_NAME+'/assets', 
    requests_pathname_prefix=None
    )
server = app.server

# Get relative data folder
METADATA_PATH = Path("metadata")
#

# Parse the metadata info
try:
    sites_dct = parse_trafo_json(METADATA_PATH / Metadata.SITES_FN)
except IOError:
    print(f'''Could not get the list of sites from {METADATA_PATH}''')

# Layout app
app.layout = define_layout(app, sites_dct)
app.title='Valg Generator'


# start_simulation_clb
@app.callback(
    Output('hist_000','figure'),
    [Input('simulate_button0', 'n_clicks')],
    [State('metadata_div','children')]
    )
def start_simulation_clb(n_clicks, parties):
	#
    # Init
    fig0 = {}
    #
    if n_clicks>0:
        data_parties = json.loads(parties)

        parties = data_parties['parties']
        parties_order = [party['shortname'] for party in parties]
        random.shuffle(parties)
        total_seats = data_parties['total_seats']
        #colors=data_parties['color']

        seats_assigned = rnd_to_sum_with_min(desired_sum=total_seats, numbers=len(parties), minimum=2, maximum=60)
        df = pd.DataFrame(index=parties_order)
        df_t = pd.DataFrame(data=[(antall,party['shortname'],party['name'],party['color']) for antall,party in zip(seats_assigned,parties)],columns=['seats','party_name','name','color']).set_index('party_name')
        df = df.merge(df_t,how='left',left_index=True,right_index=True).reset_index()
        #
        fig0 = px.bar(
            data_frame=df, 
            x="index", 
            y="seats",
            color='name',
            text='seats',
            color_discrete_sequence=df['color'],
            labels=dict(index='')
            )
        fig0.update_traces(texttemplate='%{text}', textposition='outside')
        fig0.update_layout(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)')
        #
    return fig0

if __name__ == '__main__':
    # Use this during the dev phase
    app.run_server(host='0.0.0.0', port='8080', debug=True)