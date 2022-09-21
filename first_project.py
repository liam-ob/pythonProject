from dash import Dash
from dash import html
from dash import dcc
import plotly.express as px

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

# get australias dataframe from plotly expresses dataset api
data_frame = px.data.gapminder().query("country=='Australia'")

# create a plotly line graph object with the dataframe
fig = px.line(data_frame, x="year", y="pop", color="country", title="Title")

app.layout = html.Div(children=[
    # display html h1 component
    html.H1(children='Australia Population Growth'),

    # display dash core component as a plotly graph object
    dcc.Graph(
        id='example-graph', figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)
