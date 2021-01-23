import dash
import plotly.express as px
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go  # or plotly.express as px
import pandas as pd
from datetime import datetime
import time

df = pd.read_csv( 'DIGG_WBTC.csv', usecols=['Timestamp', 'Price'] )

df['Timestamp'] = df['Timestamp'].apply( lambda x: datetime.fromtimestamp( float( x ) ) )

fig = go.Figure( data=[go.Scatter( x=df['Timestamp'], y=df['Price'] )] )

dcc.Graph( id='example-graph-2', figure=fig )
app = dash.Dash()
app.layout = html.Div( [dcc.Graph( figure=fig )] )

app.run_server( debug=True)
