import plotly.express as px
import pandas as pd
from datetime import datetime
import time

df = pd.read_csv('DIGG_WBTC.csv', usecols=['Timestamp', 'Price'])

df['Timestamp'] = df['Timestamp'].apply(lambda x: datetime.fromtimestamp(float(x)))

fig = px.line(df, x=df.Timestamp, y=df.Price)
while True:
    fig.show()
    time.sleep(5)
