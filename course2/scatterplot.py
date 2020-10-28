import pandas as pd
import plotly.graph_objects as go


df = pd.read_csv('course2\resulting_data.csv')

fig = go.Figure(go.Scatter(x=df['AAPL_x'], y=df['AAPL_y'],
                           name='Twitter sentiments'))

fig.update_layout(title='Twitter analysis',
                  plot_bgcolor='rgb(230, 230,230)',
                  showlegend=True)

fig.show()
