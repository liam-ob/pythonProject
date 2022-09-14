from dash import Dash, html, dcc
import plotly.express as px
import pandas

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

# get australias dataframe
df_aus = px.data.gapminder().query("country=='Australia'")

# get new zealands dataframe (this function uses openpyxl)
df_nz = pandas.read_excel(io='new_zealand_data.xlsx', index_col=0)

# combine data frames
concatenated_datasets = pandas.concat([df_aus, df_nz])

fig = px.line(concatenated_datasets, x="year", y="pop", color="country", title="Title")

app.layout = html.Div(children=[
    html.H1(children='Random Data'),

    html.Div(children='''
        Data: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
