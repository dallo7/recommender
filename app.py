import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import bs4
from json import JSONDecodeError
import stkPush
import random
import popularity
import popularityImg
import descriptions
import contentBasedFiltering
import popularityAndCollaborative

price_per_item = 170
price_per_item1 = 240
price_per_item2 = 300
price_per_item3 = 440
price_per_item4 = 325
price_per_item5 = 195
price_per_item6 = 400
price_per_item7 = 500

app = dash.Dash(__name__, title="Recommend cars", external_stylesheets=[dbc.themes.BOOTSTRAP],
                suppress_callback_exceptions=True)

server = app.server

login = dbc.Row([
    dbc.Col([
        dbc.Row([
            dbc.Col(
                dbc.Card(
                    dbc.CardBody([
                        html.P(["Car Recommendation Tool"],
                               style={'font-family': 'cursive', 'text-decoration': 'underline',
                                      'text-align': 'center', 'color': '2px solid black', 'fontSize': 10}),
                        dbc.CardImg(src=bs4.b64_image("img/logo.png"), top=True)]
                    ),
                    style={"width": "10rem", "margin": "0 auto", "border": "2px solid green"}
                ))], justify="center"),

        dbc.Label("Email"),
        dbc.Input(id='email', placeholder="enter email...", type="text", value="johnDoe@car.org"),
        dbc.FormText("Please enter name"),
        html.Hr(),

        dbc.Label("Password"),
        dbc.Input(id='password', placeholder="enter password...", type="text", value="Doe9"),
        dbc.FormText("Please enter password"),
        html.Hr(),

        html.Div(id='loginOutput', style={'text-align': 'center', 'color': ' 2px solid black', 'fontSize': 14}),

        html.Button('Login', id='submit'),

    ], width=6, className="m-5", md=6, sm=12, lg=6,
        style={'marginBottom': 15, 'marginTop': 5, 'color': 'green', 'fontSize': 14})

], style={'marginBottom': 15, 'marginTop': 5, 'color': 'green', 'fontSize': 14}, justify="center")

products = dbc.Row([
    dbc.Row(
        dbc.Col(
            [
                html.H3('Home page with products', style={'color': 'blue', 'font-family': 'Comic Sans MS'}),
                html.P('Welcome to the products page', style={'color': 'green', 'font-family': 'Trebuchet MS'}),
                html.Hr()
            ],
            style={
                'margin': '10px',
                'padding': '10px'
            },
            width=6
        ),
        justify='center',
        align='center',
    ),
    html.Br(),
    dbc.Col([
        dbc.Card(
            [
                dbc.CardHeader(["Popularity-Based Recommender Model"], className="text-center"),
                dbc.CardImg(src=bs4.b64_image("img/car.jpeg"), top=True),
                dbc.CardBody(
                    [
                        html.P(
                            " Make: Volta, Model: Zapped EX, Year: 2024, Body Style: Compact SUV, "
                            "Engine: Electric motor with 275 horsepower and 310 lb-ft of torque, "
                            "Range: 300 miles on a single charge",
                            className="card-text",
                        ),
                        html.Div([
                            dbc.Row([
                                dbc.Col(dbc.Button(f"Add item (Price per item: {price_per_item})", id="add-button",
                                                   color="success", size="sm"), width=8),
                                dbc.Col(dbc.Button("Remove item", id="remove-button", color="danger", size="sm"),
                                        width=2),
                            ]),
                            html.Div(id='output-container', style={'margin-top': '14px', 'margin-bottom': '10px'})
                        ]),
                        dbc.Row([
                            dbc.Col(dbc.Button("recommended for you", color="info", id="reco11",
                                               style={'margin-top': '10px', 'margin-bottom': '10px'}, size="sm"))
                        ]),
                        dbc.Row(id="recco11"),
                        dbc.Row([
                            dbc.Input(id="phone", placeholder="Enter safaricom number and Buy", type="text",
                                      style={'margin-top': '5px', 'margin-bottom': '10px'}, debounce=True),
                            html.Br(),
                        ]),
                        dbc.Button("Buy", id="buy", color="primary", n_clicks=0, size="sm",
                                   style={'margin-top': '5px', 'margin-bottom': '10px'}),
                        dbc.Row(id="stk"),
                    ]
                )
            ],
            style={"width": "24rem"},
            className="p-3 m-2"
        )
    ]),
    dbc.Col([
        dbc.Card(
            [
                dbc.CardHeader(["Content-Based Recommender Model"], className="text-center"),
                dbc.CardImg(src=bs4.b64_image("img/car1.jpeg"), top=True),
                dbc.CardBody(
                    [
                        html.P(
                            " Make: Volta, Model: Zapped EX, Year: 2024, Body Style: Compact SUV, "
                            "Engine: Electric motor with 275 horsepower and 310 lb-ft of torque, "
                            "Range: 300 miles on a single charge",
                            className="card-text",
                        ),
                        html.Div([
                            dbc.Row([
                                dbc.Col(dbc.Button(f"Add item (Price per item: {price_per_item1})", id="add-button1",
                                                   color="success", size="sm"), width=8),
                                dbc.Col(dbc.Button("Remove item", id="remove-button1", color="danger", size="sm"),
                                        width=2),
                            ]),
                            html.Div(id='output-container1', style={'margin-top': '14px', 'margin-bottom': '10px'})
                        ]),
                        dbc.Row([
                            dbc.Col(dbc.Button("recommended for you", color="info", id="reco12",
                                               style={'margin-top': '10px', 'margin-bottom': '10px'}, size="sm")),
                            dbc.Col(dcc.Dropdown(
                                id='my-dropdown0',
                                options=[{'label': i, 'value': i} for i in popularityImg.car_list],
                                value=popularityImg.car_list[0],
                                style={'borderColor': 'green', 'marginBottom': '1px', 'marginTop': '5px',
                                       'marginRight': '5px'}
                            ), width=4)
                        ]),
                        dbc.Row(id="recco12"),
                        dbc.Row([
                            dbc.Input(id="phone1", placeholder="Enter safaricom number and Buy", type="text",
                                      style={'margin-top': '5px', 'margin-bottom': '10px'}, debounce=True),
                            html.Br(),
                        ]),
                        dbc.Button("Buy", id="buy1", color="primary", n_clicks=0, size="sm",
                                   style={'margin-top': '5px', 'margin-bottom': '10px'}),
                        dbc.Row(id="stk1")
                    ]
                ),
            ],
            style={"width": "24rem"},
            className="p-3 m-2"
        )
    ]),
    dbc.Col([
        dbc.Card(
            [
                dbc.CardHeader(["Ensemble of Popularity-Based and Content-Based Model"], className="text-center"),
                dbc.CardImg(src=bs4.b64_image("img/car2.jpeg"), top=True),
                dbc.CardBody(
                    [
                        html.P(
                            " Make: Volta, Model: Zapped EX, Year: 2024, Body Style: Compact SUV, "
                            "Engine: Electric motor with 275 horsepower and 310 lb-ft of torque, "
                            "Range: 300 miles on a single charge",
                            className="card-text",
                        ),
                        html.Div([
                            dbc.Row([
                                dbc.Col(dbc.Button(f"Add item (Price per item: {price_per_item2})", id="add-button2",
                                                   color="success", size="sm"), width=8),
                                dbc.Col(dbc.Button("Remove item", id="remove-button2", color="danger", size="sm"),
                                        width=2),
                            ]),
                            html.Div(id='output-container2', style={'margin-top': '14px', 'margin-bottom': '10px'})
                        ]),
                        dbc.Row([
                            dbc.Col(dbc.Button("recommended for you", color="info", id="reco13",
                                               style={'margin-top': '10px', 'margin-bottom': '10px'}, size="sm")),
                            dbc.Col(dcc.Dropdown(
                                id='my-dropdown1',
                                options=[{'label': i, 'value': i} for i in popularityImg.car_list],
                                value=popularityImg.car_list[1],
                                style={'borderColor': 'green', 'marginBottom': '1px', 'marginTop': '5px',
                                       'marginRight': '5px'}
                            ), width=4)
                        ]),
                        dbc.Row(id="recco13"),
                        dbc.Row([
                            dbc.Input(id="phone2", placeholder="Enter safaricom number and Buy", type="text",
                                      style={'margin-top': '5px', 'margin-bottom': '10px'}, debounce=True),
                            html.Br(),
                        ]),
                        dbc.Button("Buy", id="buy2", color="primary", n_clicks=0, size="sm",
                                   style={'margin-top': '5px', 'margin-bottom': '10px'}),
                        dbc.Row(id="stk2")
                    ]
                ),
            ],
            style={"width": "24rem"},
            className="p-3 m-2"
        )
    ]),
    dbc.Col([
        dbc.Card(
            [
                dbc.CardHeader(["Ensemble of Popularity-Based and Content-Based Model"], className="text-center"),
                dbc.CardImg(src=bs4.b64_image("img/car3.jpeg"), top=True),
                dbc.CardBody(
                    [
                        html.P(
                            " Make: Volta, Model: Zapped EX, Year: 2024, Body Style: Compact SUV, "
                            "Engine: Electric motor with 275 horsepower and 310 lb-ft of torque, "
                            "Range: 300 miles on a single charge",
                            className="card-text",
                        ),
                        html.Div([
                            dbc.Row([
                                dbc.Col(dbc.Button(f"Add item (Price per item: {price_per_item3})", id="add-button3",
                                                   color="success", size="sm"), width=8),
                                dbc.Col(dbc.Button("Remove item", id="remove-button3", color="danger",
                                                   size="sm"), width=2),
                            ]),
                            html.Div(id='output-container3', style={'margin-top': '14px', 'margin-bottom': '10px'})
                        ]),
                        dbc.Row([
                            dbc.Col(dbc.Button("recommended for you", color="info", id="reco14",
                                               style={'margin-top': '10px', 'margin-bottom': '10px'}, size="sm")),
                            dbc.Col(dcc.Dropdown(
                                id='my-dropdown2',
                                options=[{'label': i, 'value': i} for i in popularityImg.car_list],
                                value=popularityImg.car_list[2],
                                style={'borderColor': 'green', 'marginBottom': '1px', 'marginTop': '5px',
                                       'marginRight': '5px'}
                            ), width=4)
                        ]),
                        dbc.Row(id="recco14"),
                        dbc.Row([
                            dbc.Input(id="phone3", placeholder="Enter safaricom number and Buy", type="text",
                                      style={'margin-top': '5px', 'margin-bottom': '10px'}, debounce=True),
                            html.Br(),
                        ]),
                        dbc.Button("Buy", id="buy3", color="primary", n_clicks=0, size="sm",
                                   style={'margin-top': '5px', 'margin-bottom': '10px'}),
                        dbc.Row(id="stk3")
                    ]
                ),
            ],
            style={"width": "24rem"},
            className="p-3 m-2"
        )
    ]),
    dbc.Col([
        dbc.Card(
            [
                dbc.CardHeader(["Popularity-Based Recommender Model"], className="text-center"),
                dbc.CardImg(src=bs4.b64_image("img/car4.jpeg"), top=True),
                dbc.CardBody(
                    [
                        html.P(
                            " Make: Volta, Model: Zapped EX, Year: 2024, Body Style: Compact SUV, "
                            "Engine: Electric motor with 275 horsepower and 310 lb-ft of torque, "
                            "Range: 300 miles on a single charge",
                            className="card-text",
                        ),
                        html.Div([
                            dbc.Row([
                                dbc.Col(dbc.Button(f"Add item (Price per item: {price_per_item4})", size="sm",
                                                   id="add-button4",
                                                   color="success"), width=8),
                                dbc.Col(dbc.Button("Remove item", id="remove-button4", size="sm", color="danger"),
                                        width=2),
                            ]),
                            html.Div(id='output-container4', style={'margin-top': '14px', 'margin-bottom': '10px'})
                        ]),
                        dbc.Row([
                            dbc.Col(dbc.Button("recommended for you", color="info", id="reco15",
                                               style={'margin-top': '10px', 'margin-bottom': '10px'}, size="sm")),
                            dbc.Col(dcc.Dropdown(
                                id='my-dropdown3',
                                options=[{'label': i, 'value': i} for i in popularityImg.car_list],
                                value=popularityImg.car_list[3],
                                style={'borderColor': 'green', 'marginBottom': '1px', 'marginTop': '5px',
                                       'marginRight': '5px'}
                            ), width=4)
                        ]),
                        dbc.Row(id="recco15"),
                        dbc.Row([
                            dbc.Input(id="phone4", placeholder="Enter safaricom number and Buy", type="text",
                                      style={'margin-top': '5px', 'margin-bottom': '10px'}, debounce=True),
                            html.Br(),
                        ]),
                        dbc.Button("Buy", id="buy4", color="primary", n_clicks=0, size="sm",
                                   style={'margin-top': '5px', 'margin-bottom': '10px'}),
                        dbc.Row(id="stk4")
                    ]
                ),
            ],
            style={"width": "24rem"},
            className="p-3 m-2"
        )
    ]),
    dbc.Col([
        dbc.Card(
            [
                dbc.CardHeader(["Content-Based Recommender Model"], className="text-center"),
                dbc.CardImg(src=bs4.b64_image("img/car5.jpeg"), top=True),
                dbc.CardBody(
                    [
                        html.P(
                            " Make: Volta, Model: Zapped EX, Year: 2024, Body Style: Compact SUV, "
                            "Engine: Electric motor with 275 horsepower and 310 lb-ft of torque, "
                            "Range: 300 miles on a single charge",
                            className="card-text",
                        ),
                        html.Div([
                            dbc.Row([
                                dbc.Col(dbc.Button(f"Add item (Price per item: {price_per_item5})", size="sm",
                                                   id="add-button5",
                                                   color="success"), width=8),
                                dbc.Col(dbc.Button("Remove item", id="remove-button5", size="sm", color="danger"),
                                        width=2),
                            ]),
                            html.Div(id='output-container5', style={'margin-top': '14px', 'margin-bottom': '10px'})
                        ]),
                        dbc.Row([
                            dbc.Col(dbc.Button("recommended for you", color="info", id="reco16",
                                               style={'margin-top': '10px', 'margin-bottom': '10px'}, size="sm")),
                            dbc.Col(dcc.Dropdown(
                                id='my-dropdown4',
                                options=[{'label': i, 'value': i} for i in popularityImg.car_list],
                                value=popularityImg.car_list[4],
                                style={'borderColor': 'green', 'marginBottom': '1px', 'marginTop': '5px',
                                       'marginRight': '5px'}
                            ), width=4)
                        ]),
                        dbc.Row(id="recco16"),
                        dbc.Row([
                            dbc.Input(id="phone5", placeholder="Enter safaricom number and Buy", type="text",
                                      style={'margin-top': '5px', 'margin-bottom': '10px'}, debounce=True),
                            html.Br(),
                        ]),
                        dbc.Button("Buy", id="buy5", color="primary", n_clicks=0, size="sm",
                                   style={'margin-top': '5px', 'margin-bottom': '10px'}),
                        dbc.Row(id="stk5")
                    ]
                ),
            ],
            style={"width": "24rem"},
            className="p-3 m-2",
        )
    ]),
], style={'marginLeft': 'auto', 'marginRight': 'auto'})

app.layout = dbc.Container([
    html.Meta(name='viewport', content='width=device-width, initial-scale=1'),
    dcc.Location(id='url', refresh=False),
    dbc.Row([login], id='page-content'),
])


@app.callback(
    Output('page-content', 'children'),
    [Input('submit', 'n_clicks')]
)
def display_page(nclicks):
    if nclicks:
        return products
    else:
        return login


@app.callback(
    Output('recco11', 'children'),
    [Input('reco11', 'n_clicks')]
)
def display_images(nclicks):
    if nclicks:
        image_cards = []
        for car in popularity.popularity():
            img_url = popularityImg.imgCarName.get(car)
            if img_url:
                image_cards.append(
                    dbc.Card(
                        [
                            dbc.CardImg(src=bs4.b64_image(img_url), top=True, style={}),
                            dbc.CardBody([
                                dcc.Markdown(f"**{car.capitalize()}**"),
                                dbc.Button("More Info", color="info", className="me-1",
                                           id=img_url, size="sm"),
                                dbc.Tooltip(descriptions.block_content, target=img_url, trigger="hover",
                                            delay={'show': 0, 'hide': 200},
                                            style={'max-width': '500px', 'padding': '.25rem .5rem',
                                                   'margin-bottom': '20px',
                                                   'color': '#fff', 'text-align': 'center', 'background-color': 'green',
                                                   'border-radius': '.25rem'}
                                            ),
                            ])
                        ], id=img_url, className="m-1",
                        style={'border': '1px solid green', 'display': 'inline-block', 'width': '45%'}
                    )
                )
        random.shuffle(image_cards)
        return image_cards
    return "",


@app.callback(
    Output('recco12', 'children'),
    [Input('reco12', 'n_clicks'),
     Input('my-dropdown0', 'value')]
)
def display_images(n_clicks, value):
    value = f"carName_{value}"
    if n_clicks:
        image_cards = []
        for car in contentBasedFiltering.recommend_cars(value):
            img_url = popularityImg.imgCarName.get(car)
            if img_url:
                image_cards.append(
                    dbc.Card(
                        [
                            dbc.CardImg(src=bs4.b64_image(img_url), top=True, style={}),
                            dbc.CardBody([
                                dcc.Markdown(f"**{car.capitalize()}**"),
                                dbc.Button("More Info", color="info", className="me-1",
                                           id=img_url, size="sm"),
                                dbc.Tooltip(descriptions.block_content, target=img_url, trigger="hover",
                                            delay={'show': 0, 'hide': 200},
                                            style={'max-width': '500px', 'padding': '.25rem .5rem',
                                                   'margin-bottom': '20px',
                                                   'color': '#fff', 'text-align': 'center', 'background-color': 'green',
                                                   'border-radius': '.25rem'}
                                            ),
                            ])
                        ], id=img_url, className="m-1",
                        style={'border': '1px solid green', 'display': 'inline-block', 'width': '45%'}
                    )
                )
        random.shuffle(image_cards)
        return image_cards
    return []


@app.callback(
    Output('recco13', 'children'),
    [Input('reco13', 'n_clicks'),
     Input('my-dropdown1', 'value')]
)
def display_images(n_clicks, value):
    value = f"carName_{value}"
    if n_clicks:
        image_cards = []
        for car in popularityAndCollaborative.popularCollabo(value):
            img_url = popularityImg.imgCarName.get(car)
            if img_url:
                image_cards.append(
                    dbc.Card(
                        [
                            dbc.CardImg(src=bs4.b64_image(img_url), top=True, style={}),
                            dbc.CardBody([
                                dcc.Markdown(f"**{car.capitalize()}**"),
                                dbc.Button("More Info", color="info", className="me-1",
                                           id=img_url, size="sm"),
                                dbc.Tooltip(descriptions.block_content, target=img_url, trigger="hover",
                                            delay={'show': 0, 'hide': 200},
                                            style={'max-width': '500px', 'padding': '.25rem .5rem',
                                                   'margin-bottom': '20px',
                                                   'color': '#fff', 'text-align': 'center', 'background-color': 'green',
                                                   'border-radius': '.25rem'}
                                            ),
                            ])
                        ], id=img_url, className="m-1",
                        style={'border': '1px solid green', 'display': 'inline-block', 'width': '45%'}
                    )
                )
        random.shuffle(image_cards)
        return image_cards
    return []


@app.callback(
    Output('recco14', 'children'),
    Input('my-dropdown2', 'value'))
def display_images(value):
    value = f"carName_{value}"
    image_cards = []
    for car in popularityAndCollaborative.popularCollabo(value):
        img_url = popularityImg.imgCarName.get(car)
        if img_url:
            image_cards.append(
                dbc.Card(
                    [
                        dbc.CardImg(src=bs4.b64_image(img_url), top=True, style={}),
                        dbc.CardBody([
                            dcc.Markdown(f"**{car.capitalize()}**"),
                            dbc.Button("More Info", color="info", className="me-1",
                                       id=img_url, size="sm"),
                            dbc.Tooltip(descriptions.block_content, target=img_url, trigger="hover",
                                        delay={'show': 0, 'hide': 200},
                                        style={'max-width': '500px', 'padding': '.25rem .5rem',
                                               'margin-bottom': '20px',
                                               'color': '#fff', 'text-align': 'center', 'background-color': 'green',
                                               'border-radius': '.25rem'}
                                        ),
                        ])
                    ], id=img_url, className="m-1",
                    style={'border': '1px solid green', 'display': 'inline-block', 'width': '45%'}
                )
            )
    random.shuffle(image_cards)
    return image_cards


@app.callback(
    Output('recco15', 'children'),
    Input('my-dropdown3', 'value'))
def display_images(value):
    value = f"carName_{value}"
    image_cards = []
    for car in popularity.popularity():
        img_url = popularityImg.imgCarName.get(car)
        if img_url:
            image_cards.append(
                dbc.Card(
                    [
                        dbc.CardImg(src=bs4.b64_image(img_url), top=True, style={}),
                        dbc.CardBody([
                            dcc.Markdown(f"**{car.capitalize()}**"),
                            dbc.Button("More Info", color="info", className="me-1",
                                       id=img_url, size="sm"),
                            dbc.Tooltip(descriptions.block_content, target=img_url, trigger="hover",
                                        delay={'show': 0, 'hide': 200},
                                        style={'max-width': '500px', 'padding': '.25rem .5rem',
                                               'margin-bottom': '20px',
                                               'color': '#fff', 'text-align': 'center', 'background-color': 'green',
                                               'border-radius': '.25rem'}
                                        ),
                        ])
                    ], id=img_url, className="m-1",
                    style={'border': '1px solid green', 'display': 'inline-block', 'width': '45%'}
                )
            )
    random.shuffle(image_cards)
    return image_cards


@app.callback(
    Output('recco16', 'children'),
    Input('my-dropdown4', 'value'))
def display_images(value):
    value = f"carName_{value}"
    image_cards = []
    for car in contentBasedFiltering.recommend_cars(value):
        img_url = popularityImg.imgCarName.get(car)
        if img_url:
            image_cards.append(
                dbc.Card(
                    [
                        dbc.CardImg(src=bs4.b64_image(img_url), top=True, style={}),
                        dbc.CardBody([
                            dcc.Markdown(f"**{car.capitalize()}**"),
                            dbc.Button("More Info", color="info", className="me-1",
                                       id=img_url, size="sm"),
                            dbc.Tooltip(descriptions.block_content, target=img_url, trigger="hover",
                                        delay={'show': 0, 'hide': 200},
                                        style={'max-width': '500px', 'padding': '.25rem .5rem',
                                               'margin-bottom': '20px',
                                               'color': '#fff', 'text-align': 'center', 'background-color': 'green',
                                               'border-radius': '.25rem'}
                                        ),
                        ])
                    ], id=img_url, className="m-1",
                    style={'border': '1px solid green', 'display': 'inline-block', 'width': '45%'}
                )
            )
    random.shuffle(image_cards)
    return image_cards


@app.callback(
    Output('output-container', 'children'),
    Output('stk', 'children'),
    [Input('add-button', 'n_clicks'),
     Input('remove-button', 'n_clicks'),
     Input('phone', 'value'),
     Input('buy', 'n_clicks')]
)
def update_output(n_clicks_add, n_clicks_remove, phone, n_clicksBuy):
    if n_clicks_add is None:
        n_clicks_add = 0
    if n_clicks_remove is None:
        n_clicks_remove = 0

    n_items = n_clicks_add - n_clicks_remove
    if n_items < 0:
        n_items = 0

    total_price = n_items * price_per_item
    transact = None

    if n_clicksBuy:
        if phone.startswith('0') or phone.startswith('254'):
            phone = '254' + phone[1:]
            transact = stkPush.initiate_stk_push(total_price, phone)
            try:
                if transact.status_code == 200:
                    transact = "Payment request sent successfully"
                else:
                    transact = "Payment request Failed!"
            except JSONDecodeError:
                transact = "Try after a minute, Payment not processed!"

    return f'Total price for {n_items} items: {total_price}', transact


@app.callback(
    Output('output-container1', 'children'),
    Output('stk1', 'children'),
    [Input('add-button1', 'n_clicks'),
     Input('remove-button1', 'n_clicks'),
     Input('phone1', 'value'),
     Input('buy1', 'n_clicks')]
)
def update_output(n_clicks_add, n_clicks_remove, phone, n_clicksBuy):
    if n_clicks_add is None:
        n_clicks_add = 0
    if n_clicks_remove is None:
        n_clicks_remove = 0

    n_items = n_clicks_add - n_clicks_remove
    if n_items < 0:
        n_items = 0

    total_price = n_items * price_per_item1
    transact = None

    if n_clicksBuy:
        if phone.startswith('0') or phone.startswith('254'):
            phone = '254' + phone[1:]
            transact = stkPush.initiate_stk_push(total_price, phone)
            if transact.status_code == 200:
                transact = "Transaction successful"
            else:
                transact = "Transaction Failed!"

    return f'Total price for {n_items} items: {total_price}', transact


@app.callback(
    Output('output-container2', 'children'),
    Output('stk2', 'children'),
    [Input('add-button2', 'n_clicks'),
     Input('remove-button2', 'n_clicks'),
     Input('phone2', 'value'),
     Input('buy2', 'n_clicks')]
)
def update_output(n_clicks_add, n_clicks_remove, phone, n_clicksBuy):
    if n_clicks_add is None:
        n_clicks_add = 0
    if n_clicks_remove is None:
        n_clicks_remove = 0

    n_items = n_clicks_add - n_clicks_remove
    if n_items < 0:
        n_items = 0

    total_price = n_items * price_per_item2
    transact = None

    if n_clicksBuy:
        if phone.startswith('0') or phone.startswith('254'):
            phone = '254' + phone[1:]
            transact = stkPush.initiate_stk_push(total_price, phone)
            if transact.status_code == 200:
                transact = "Transaction successful"
            else:
                transact = "Transaction Failed!"

    return f'Total price for {n_items} items: {total_price}', transact


@app.callback(
    Output('output-container3', 'children'),
    Output('stk3', 'children'),
    [Input('add-button3', 'n_clicks'),
     Input('remove-button3', 'n_clicks'),
     Input('phone3', 'value'),
     Input('buy3', 'n_clicks')]
)
def update_output(n_clicks_add, n_clicks_remove, phone, n_clicksBuy):
    if n_clicks_add is None:
        n_clicks_add = 0
    if n_clicks_remove is None:
        n_clicks_remove = 0

    n_items = n_clicks_add - n_clicks_remove
    if n_items < 0:
        n_items = 0

    total_price = n_items * price_per_item3
    transact = None

    if n_clicksBuy:
        if phone.startswith('0') or phone.startswith('254'):
            phone = '254' + phone[1:]
            transact = stkPush.initiate_stk_push(total_price, phone)
            if transact.status_code == 200:
                transact = "Transaction successful"
            else:
                transact = "Transaction Failed!"

    return f'Total price for {n_items} items: {total_price}', transact


@app.callback(
    Output('output-container4', 'children'),
    Output('stk4', 'children'),
    [Input('add-button4', 'n_clicks'),
     Input('remove-button4', 'n_clicks'),
     Input('phone4', 'value'),
     Input('buy4', 'n_clicks')]
)
def update_output(n_clicks_add, n_clicks_remove, phone, n_clicksBuy):
    if n_clicks_add is None:
        n_clicks_add = 0
    if n_clicks_remove is None:
        n_clicks_remove = 0

    n_items = n_clicks_add - n_clicks_remove
    if n_items < 0:
        n_items = 0

    total_price = n_items * price_per_item4
    transact = None

    if n_clicksBuy:
        if phone.startswith('0') or phone.startswith('254'):
            phone = '254' + phone[1:]
            transact = stkPush.initiate_stk_push(total_price, phone)
            if transact.status_code == 200:
                # print(transact)
                transact = "Transaction successful"
            else:
                # print(transact)
                transact = "Transaction Failed!"

    return f'Total price for {n_items} items: {total_price}', transact


@app.callback(
    Output('output-container5', 'children'),
    Output('stk5', 'children'),
    [Input('add-button5', 'n_clicks'),
     Input('remove-button5', 'n_clicks'),
     Input('phone5', 'value'),
     Input('buy5', 'n_clicks')]
)
def update_output(n_clicks_add, n_clicks_remove, phone, n_clicksBuy):
    if n_clicks_add is None:
        n_clicks_add = 0
    if n_clicks_remove is None:
        n_clicks_remove = 0

    n_items = n_clicks_add - n_clicks_remove
    if n_items < 0:
        n_items = 0

    total_price = n_items * price_per_item5
    transact = None

    if n_clicksBuy:
        if phone.startswith('0') or phone.startswith('254'):
            phone = '254' + phone[1:]
            transact = stkPush.initiate_stk_push(total_price, phone)
            if transact.status_code == 200:
                # print(transact)
                transact = "Transaction successful"
            else:
                # print(transact)
                transact = "Transaction Failed!"

    return f'Total price for {n_items} items: {total_price}', transact


@app.callback(
    Output('output-container6', 'children'),
    Output('stk6', 'children'),
    [Input('add-button6', 'n_clicks'),
     Input('remove-button6', 'n_clicks'),
     Input('phone6', 'value'),
     Input('buy6', 'n_clicks')]
)
def update_output(n_clicks_add, n_clicks_remove, phone, n_clicksBuy):
    if n_clicks_add is None:
        n_clicks_add = 0
    if n_clicks_remove is None:
        n_clicks_remove = 0

    n_items = n_clicks_add - n_clicks_remove
    if n_items < 0:
        n_items = 0

    total_price = n_items * price_per_item6
    transact = None

    if n_clicksBuy:
        if phone.startswith('0') or phone.startswith('254'):
            phone = '254' + phone[1:]
            transact = stkPush.initiate_stk_push(total_price, phone)
            if transact.status_code == 200:
                # print(transact)
                transact = "Transaction successful"
            else:
                # print(transact)
                transact = "Transaction Failed!"

    return f'Total price for {n_items} items: {total_price}', transact


@app.callback(
    Output('output-container7', 'children'),
    Output('stk7', 'children'),
    [Input('add-button7', 'n_clicks'),
     Input('remove-button7', 'n_clicks'),
     Input('phone7', 'value'),
     Input('buy7', 'n_clicks')]
)
def update_output(n_clicks_add, n_clicks_remove, phone, n_clicksBuy):
    if n_clicks_add is None:
        n_clicks_add = 0
    if n_clicks_remove is None:
        n_clicks_remove = 0

    n_items = n_clicks_add - n_clicks_remove
    if n_items < 0:
        n_items = 0

    total_price = n_items * price_per_item7
    transact = None

    if n_clicksBuy:
        if phone.startswith('0') or phone.startswith('254'):
            phone = '254' + phone[1:]
            transact = stkPush.initiate_stk_push(total_price, phone)
            if transact.status_code == 200:
                # print(transact)
                transact = "Transaction successful"
            else:
                # print(transact)
                transact = "Transaction Failed!"

    return f'Total price for {n_items} items: {total_price}', transact


if __name__ == '__main__':
    app.run_server(debug=True, port=8050)
    # app.run_server(debug=True, host="192.168.11.249", port=8852)
