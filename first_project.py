import pandas
import plotly.express
from dash import Dash, html, dcc

app = Dash(__name__)


def add_two_numbers(number1: float, number2: int) -> float:
    """
    Adds two numbers together
    :param number1: specifies the first number to be added
    :param number2: specifies the second number to be added
    :return: returns sum of both parameters
    """
    return number1 + number2



# return true if number is not prime
def find_if_not_prime_number(number):
    for i in range(2, number):
        if number % i == 0:
            return True
    return False


def main():
    my_dict = {
        'prime_number': [],
        'x': [],
    }
    # find all prime numbers between 2 and 20
    for x in range(2, 20):
        if find_if_not_prime_number(x) is False:
            my_dict['prime_number'].append(True)
        else:
            my_dict['prime_number'].append(False)
        my_dict['x'].append(x)
    df = pandas.DataFrame(my_dict)

    # put prime numbers in a graph
    graph = plotly.express.scatter(df, color='prime_number')

    app.layout = html.Div(children=[
        html.H1(children='Prime Numbers'),
        dcc.Graph(id='example-graph', figure=graph)])


if __name__ == "__main__":  # pragma: no cover
    main()
    app.run_server(debug=True)
