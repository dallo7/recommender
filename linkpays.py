import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import bs4
import imageContainer
import stkPush

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

app.layout = dbc.Container([
    html.Meta(name='viewport', content='width=device-width, initial-scale=1'),
    dcc.Location(id='url', refresh=False),
    dbc.Row([], id='page-content')
])

home = dbc.Row([
    dcc.Link('Go to products to Shop', href='/products'),
])

products = dbc.Row([
    dbc.Row([
        html.H1('Home page with products'),
        html.P('Welcome to the products page!')
    ], justify="center"),
    html.Br(),
    dbc.Row([
        dbc.Card(
            [
                dbc.CardImg(src=bs4.b64_image(value[0]), top=True),
                dbc.CardBody(
                    [
                        html.P(
                            " Make: Volta, Model: Zapped EX, Year: 2024, Body Style: Compact SUV, "
                            "Engine: Electric motor with 275 horsepower and 310 lb-ft of torque, "
                            "Range: 300 miles on a single charge",
                            className="card-text",
                        ),
                        html.P(f"Price: ${imageContainer.imgContainer[keys][1]}"),
                        dcc.Input(id=f'{imageContainer.imgContainer[keys]}-quantity'.replace(".", ""), type='number',
                                  value=1),
                        dbc.Row(id=f'{imageContainer.imgContainer[keys]}-total-price'.replace(".", ""),
                                className="p-1 m-2", style={"font-weight": "bold"}),
                        dbc.Button("recommended for you", color="info", id="reco"),
                        dbc.Row(id="recco"),
                        html.Hr(),
                        dbc.Row([
                            dbc.Input(id="phone", placeholder="Enter safaricon number and Buy", type="text"),
                            html.Br(),
                            html.Div([], id="stk")
                        ]),
                        html.Br(),
                        dbc.Button("Buy", id="buy", color="primary", n_clicks=0),
                    ]
                ),
            ],
            style={"width": "24rem"},
            className="p-3 m-2"
        )
        for keys, value in imageContainer.imgContainer.items()
    ]),
    html.Br(),
    dcc.Link('Go to Next Product page', href='/next_products'),
], style={'marginLeft': 'auto', 'marginRight': 'auto'})

nextProducts = "Home123"


# nextProducts = dbc.Row([
#     dbc.Row([
#         html.H1('More Products Page'),
#         html.P('Recommendations show without clicking.')
#     ], justify="center"),
#     dbc.Row([
#         dbc.Card(
#             [
#                 dbc.CardImg(src=bs4.b64_image(imageContainer.imgContainerNxt[key][0]), top=True),
#                 dbc.CardBody(
#                     [
#                         html.P(
#                             " Make: Volta, Model: Zapped EX, Year: 2024, Body Style: Compact SUV, "
#                             "Engine: Electric motor with 275 horsepower and 310 lb-ft of torque, "
#                             "Range: 300 miles on a single charge",
#                             className="card-text",
#                         ),
#                         html.Hr(),
#                         html.P(f"Price: ${imageContainer.imgContainerNxt[key][1]}"),
#                         dcc.Input(id=f'{imageContainer.imgContainerNxt[key]}-quantity', type='number', value=1),
#                         html.Div(id=f'{imageContainer.imgContainerNxt[key]}-total-price'),
#                         dbc.Row(id="recco6"),
#                         dbc.Button("Buy", color="primary"),
#                     ]
#                 ),
#             ],
#             style={"width": "24rem"},
#             className="p-3 m-2"
#         )
#         for key, value in imageContainer.imgContainerNxt.items()
#     ]),
#     html.Br(),
#     dcc.Link('Go to back to products page', href='/products'),
# ], style={'marginLeft': 'auto', 'marginRight': 'auto'})


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/products':
        return products
    elif pathname == '/next_products':
        return nextProducts
    else:
        return home


@app.callback(Output('stk', 'children'),
              [Input('buy', 'n_clicks'),
               State('phone', 'value')])
def stk(n_clicks, phone):
    if n_clicks is None:
        return ""
    elif int(n_clicks) > int(0):
        print(phone)
        return "test"
    else:
        return ""


for keys, value in imageContainer.imgContainer.items():
    @app.callback(
        Output(f'{imageContainer.imgContainer[keys]}-total-price'.replace(".", ""), 'children'),
        Input(f'{imageContainer.imgContainer[keys]}-quantity'.replace(".", ""), 'value')
    )
    def update_total_price(quantity, amount=imageContainer.imgContainer[keys][1]):
        total = amount * quantity
        totalPrice = f"Total Price: ${total}"
        return totalPrice

        # mpesa = stkPush.initiate_stk_push(tel, price)
        # return totalPrice


if __name__ == '__main__':
    # app.run_server(debug=True, port=8888)
    app.run_server(debug=True, host="192.168.11.187", port=8852)
