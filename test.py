# import dash
# from dash import dcc, html
# import dash_bootstrap_components as dbc
# from dash.dependencies import Input, Output
#
# app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
#
# items = {
#     'item1': {'name': 'Item 1', 'price': 100},
#     'item2': {'name': 'Item 2', 'price': 200},
#     'item3': {'name': 'Item 3', 'price': 300},
# }
#
# app.layout = html.Div([
#     dbc.Row([
#         dbc.Col([
#             dbc.Card([
#                 dbc.CardBody([
#                     dbc.CardHeader(items[item_id]['name']),
#                     html.P(f"Price: ${items[item_id]['price']}"),
#                     dcc.Input(id=f'{item_id}-quantity', type='number', value=1),
#                     html.Div(id=f'{item_id}-total-price')
#                 ])
#             ])
#             for item_id in items
#         ])
#     ])
# ])
#
# for item_id in items:
#     @app.callback(
#         Output(f'{item_id}-total-price', 'children'),
#         Input(f'{item_id}-quantity', 'value')
#     )
#     def update_total_price(quantity, item_id=item_id):
#         return f"Total Price: ${items[item_id]['price'] * quantity}"
#
# if __name__ == "__main__":
#     app.run_server(debug=True)


# import dash
# from dash import dcc, html
# import dash_bootstrap_components as dbc
# from dash.dependencies import Input, Output
#
# app = dash.Dash(__name__)
#
# app.layout = dbc.Row([
#     dbc.Input(
#         id='phone-input',
#         type='text',
#         placeholder='Enter your phone number...'
#     ),
#     dbc.Button('Submit', id='submit-button', n_clicks=0),
#     dbc.Row(id='output-div')
# ])
#
# @app.callback(
#     Output('output-div', 'children'),
#     [Input('submit-button', 'n_clicks')],
#     [dash.dependencies.State('phone-input', 'value')]
# )
# def update_output(n_clicks, value):
#     if n_clicks > 0:
#         try:
#             phone_number = int(value)
#             print(phone_number)
#             return f'Phone number {phone_number} received.'
#         except ValueError:
#             return 'Invalid phone number. Please enter a numeric value.'
#     else:
#         return ''
#
# if __name__ == '__main__':
#     app.run_server(debug=True)

#
# import dash
# from dash import html
#
# app = dash.Dash(__name__)
#
# app.layout = html.Div([
#     html.Button('Button 1', id='button-1', n_clicks=0),
#     html.Button('Button 2', id='button-2', n_clicks=0),
#     html.Div(id='output-container')
# ])
#
#
# @app.callback(
#     dash.dependencies.Output('output-container', 'children'),
#     [dash.dependencies.Input('button-1', 'n_clicks'),
#      dash.dependencies.Input('button-2', 'n_clicks')]
# )
# def update_output(n1, n2):
#     ctx = dash.callback_context
#
#     if not ctx.triggered:
#         return 'No button has been clicked yet.'
#     else:
#         button_id = ctx.triggered[0]['prop_id'].split('.')[0]
#         print(button_id)
#         return f'Button {button_id} has been clicked.'
#
#
# if __name__ == '__main__':
#     app.run_server(debug=True)

# import dash
# from dash import html
# import dash_bootstrap_components as dbc
#
# app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
#
# app.layout = html.Div([
#     dbc.Button("Price: 170", id="my-button", color="warning", className="mr-1"),
# ])
#
# @app.callback(
#     dash.dependencies.Output('my-button', 'children'),
#     [dash.dependencies.Input('my-button', 'n_clicks')]
# )
# def update_output(n_clicks):
#     if n_clicks is None:
#         print('Button has not been clicked yet.')
#         return 'Price: 170'
#     else:
#         print(f'Button has been clicked {n_clicks} times.')
#         return f'Price: 170 (clicked {n_clicks} times)'
#
# if __name__ == '__main__':
#     app.run_server(debug=True)


# import dash
# from dash import html
# import dash_bootstrap_components as dbc
#
# app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
#
# price_per_item = 170
#
# app.layout = html.Div([
#     dbc.Button(f"Price per item: {price_per_item}", id="my-button", color="warning", className="mr-1"),
#     html.Div(id='output-container')
# ])
#
# @app.callback(
#     dash.dependencies.Output('output-container', 'children'),
#     [dash.dependencies.Input('my-button', 'n_clicks')]
# )
# def update_output(n_clicks):
#     if n_clicks is None:
#         n_clicks = 0
#     total_price = n_clicks * price_per_item
#     return f'Total price for {n_clicks} items: {total_price}'
#
# if __name__ == '__main__':
#     app.run_server(debug=True)

import dash
from dash import html
import dash_bootstrap_components as dbc

# app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
#
# price_per_item = 170
#
# app.layout = html.Div([
#     dbc.Button(f"Add item (Price per item: {price_per_item})", id="add-button", color="success", className="mr-1"),
#     dbc.Button("Remove item", id="remove-button", color="danger", className="mr-1"),
#     html.Div(id='output-container')
# ])
#
# @app.callback(
#     dash.dependencies.Output('output-container', 'children'),
#     [dash.dependencies.Input('add-button', 'n_clicks'),
#      dash.dependencies.Input('remove-button', 'n_clicks')]
# )
# def update_output(n_clicks_add, n_clicks_remove):
#     if n_clicks_add is None:
#         n_clicks_add = 0
#     if n_clicks_remove is None:
#         n_clicks_remove = 0
#
#     n_items = n_clicks_add - n_clicks_remove
#     if n_items < 0:
#         n_items = 0  # We can't have a negative number of items
#
#     total_price = n_items * price_per_item
#     return f'Total price for {n_items} items: {total_price}'
#
#
# if __name__ == '__main__':
#     app.run_server(debug=True)

import dash
from dash import html
from dash.dependencies import Input, Output

# nextProducts = dbc.Row([
#     dbc.Row([
#         html.H1('More Products Page'),
#         html.P('Recommendations show without clicking.')
#     ], justify="center"),
#     dbc.Col([
#         dbc.Card(
#             [
#                 dbc.CardImg(src=bs4.b64_image("img/car6.jpeg"), top=True),
#                 dbc.CardBody(
#                     [
#                         html.P(
#                             " Make: Volta, Model: Zapped EX, Year: 2024, Body Style: Compact SUV, "
#                             "Engine: Electric motor with 275 horsepower and 310 lb-ft of torque, "
#                             "Range: 300 miles on a single charge",
#                             className="card-text",
#                         ),
#                         html.Div([
#                             dbc.Row([
#                                 dbc.Col(dbc.Button(f"Add item (Price per item: {price_per_item6})", id="add-button6",
#                                                    color="success"), width=8),
#                                 dbc.Col(dbc.Button("Remove item", id="remove-button6", color="danger"), width=2),
#                             ]),
#                             html.Div(id='output-container6', style={'margin-top': '14px', 'margin-bottom': '10px'})
#                         ]),
#                         dbc.Button("recommended for you", color="info", id="reco6",
#                                    style={'margin-top': '10px', 'margin-bottom': '10px'}),
#                         dbc.Row(id="recco6"),
#                         dbc.Row([
#                             dbc.Input(id="phone6", placeholder="Enter safaricom number and Buy", type="text",
#                                       style={'margin-top': '5px', 'margin-bottom': '10px'}, debounce=True),
#                             html.Br(),
#                         ]),
#                         dbc.Button("Buy", id="buy6", color="primary", n_clicks=0,
#                                    style={'margin-top': '5px', 'margin-bottom': '10px'}),
#                         dbc.Row(id="stk6")
#                     ]
#                 ),
#             ],
#             style={"width": "24rem"},
#             className="p-3 m-2"
#         )
#     ]),
#     dbc.Col([
#         dbc.Card(
#             [
#                 dbc.CardImg(src=bs4.b64_image("img/car7.jpeg"), top=True),
#                 dbc.CardBody(
#                     [
#                         html.P(
#                             " Make: Volta, Model: Zapped EX, Year: 2024, Body Style: Compact SUV, "
#                             "Engine: Electric motor with 275 horsepower and 310 lb-ft of torque, "
#                             "Range: 300 miles on a single charge",
#                             className="card-text",
#                         ),
#                         html.Div([
#                             dbc.Row([
#                                 dbc.Col(dbc.Button(f"Add item (Price per item: {price_per_item7})", id="add-button7",
#                                                    color="success"), width=8),
#                                 dbc.Col(dbc.Button("Remove item", id="remove-button7", color="danger"), width=2),
#                             ]),
#                             html.Div(id='output-container7', style={'margin-top': '14px', 'margin-bottom': '10px'})
#                         ]),
#                         dbc.Button("recommended for you", color="info", id="reco7",
#                                    style={'margin-top': '10px', 'margin-bottom': '10px'}),
#                         dbc.Row(id="recco7"),
#                         dbc.Row([
#                             dbc.Input(id="phone7", placeholder="Enter safaricom number and Buy", type="text",
#                                       style={'margin-top': '5px', 'margin-bottom': '10px'}, debounce=True),
#                             html.Br(),
#                         ]),
#                         dbc.Button("Buy", id="buy7", color="primary", n_clicks=0,
#                                    style={'margin-top': '5px', 'margin-bottom': '10px'}),
#                         dbc.Row(id="stk7")
#                     ]
#                 ),
#             ],
#             style={"width": "24rem"},
#             className="p-3 m-2"
#         )
#     ]),
#     html.Br(),
#     dcc.Link('Go to back to products page', href='/products'),
# ])

# app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
#
# app.layout = html.Div([
#     dbc.Button("Click me", id="my-button", color="primary", className="mr-2", value="Click me you will fire!"),
#     html.Span(id="my-output")
# ])
#
#
# @app.callback(
#     Output("my-output", "children"),
#     Input("my-button", "n_clicks"),
#     Input("my-button", "value")
# )
# def update_output(n_clicks, value):
#     if n_clicks:
#         return f" 🤔😞🤞 {value} "
#     else:
#         return "",
#
#
# if __name__ == "__main__":
#     app.run_server(debug=True)
#

# import dash
# from dash import dcc, html
# from dash.dependencies import Input, Output
#
# app = dash.Dash(__name__, suppress_callback_exceptions=True)
#
# app.layout = html.Div([
#     dcc.Location(id='url', refresh=False),
#     html.Div(id='page-content')
# ])
#
# index_page = html.Div([
#     html.H1('Welcome to the Home Page!'),
#     html.Button('Go to Page 2', id='load-page-2', n_clicks=0),
# ])
#
# page_2_layout = html.Div([
#     html.H1('Welcome to Page 2!'),
#     html.Button('Go back to home', id='load-home', n_clicks=0),
# ])
#
# @app.callback(Output('page-content', 'children'),
#               [Input('load-page-2', 'n_clicks'),
#                Input('load-home', 'n_clicks')])
# def display_page(n1, n2):
#     changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
#     if 'load-page-2' in changed_id:
#         return page_2_layout
#     else:
#         return index_page
#
# if __name__ == '__main__':
#     app.run_server(debug=True, port =8987)

# df = pd.read_csv("carData.csv")
#
# car_list = ['ritz', 'sx4', 'ciaz', 'swift', 'ertiga', 'dzire', 'ignis', 'baleno', 'omni', 'fortuner', 'innova',
#             'corolla', 'camry', 'eon', 'xcent', 'elantra', 'creta', 'verna', 'brio', 'amaze']

# newDf = df[df.carName.isin(car_list)].reset_index(drop=True)

# newDf = newDf.to_csv("newDf.csv")

# print(newDf)
#
# exit()


# newDf = pd.read_csv("newDf.csv")
# classes_to_drop = ['city', 'corolla altis']
# newDf = newDf[~newDf['carName'].isin(classes_to_drop)]

# import dash
# from dash import dcc
# import random
#
# import bs4
#
# car_list = ['verna', 'fortuner', 'brio', 'innova']
# img_dict = {'verna': 'img/ritz.jpg', 'fortuner': 'img/sx4.jpg',
#             'brio': 'img/ciaz.jpg', 'innova': 'img/swift.jpg'}
#
# app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
#
# app.layout = dbc.Container([
#     dbc.Row([
#         dbc.Col(
#             dbc.Button('Show Images', id='show-images-button', n_clicks=0),
#             width=3
#         ),
#         dbc.Col(
#             dbc.Row(id='image-row'),
#             width=9
#         )
#     ]),
# ])
#
#
# @app.callback(
#     Output(component_id='image-row', component_property='children'),
#     Input(component_id='show-images-button', component_property='n_clicks')
# )
# def display_images(n_clicks):
#     if n_clicks > 0:
#         image_cards = []
#         for car in car_list:
#             img_url = img_dict.get(car)
#             if img_url:
#                 image_cards.append(
#                     dbc.Card(
#                         [
#                             dbc.CardImg(src=bs4.b64_image(img_url), top=True, style={}),
#                             dbc.CardBody(
#                                 dcc.Markdown(f"**{car.capitalize()}**")
#                             )
#                         ],
#                         style={'border': '1px solid green', 'display': 'inline-block', 'width': '50%'}
#                     )
#                 )
#         # Shuffle the image cards for a random order
#         random.shuffle(image_cards)
#         return image_cards
#     return []
#
#
# if __name__ == '__main__':
#     app.run_server(debug=True, port=8555)


# import pandas as pd

# # Create a DataFrame with 7 int and float columns
# data = {
#     "Column1": [1, 2, 3, 4, 5, 100, 6, 7, 8],
#     "Column2": [1.5, 2.5, 3.5, 4.5, 500.5, 10.5, 6.5, 7.5, 8.5],
#     "Column3": [10, 20, 30, 40, 50, 60, 70, 80, 90],
#     "Column4": [100, 200, 300, 400, 500, 600, 700, 800, 900],
#     "Column5": [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9],
#     "Column6": [1.1, 2.1, 3.1, 4.1, 50.1, 6.1, 7.1, 8.1, 9.1],
#     "Column7": [10.1, 2000.1, 30.1, 40.1, 50.1, 60.1, 70.1, 80.1, 90.1],
# }
# df = pd.DataFrame(data)
#
#
# # Define a function to detect outliers using the interquartile range (IQR) method
# def detect_outliers(df, columns):
#     for col in columns:
#         # Calculate the IQR
#         Q1 = df[col].quantile(0.25)
#         Q3 = df[col].quantile(0.75)
#         IQR = Q3 - Q1
#
#         # Define the outlier boundaries
#         lower_bound = Q1 - 1.5 * IQR
#         upper_bound = Q3 + 1.5 * IQR
#
#         # Find outliers
#         outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
#
#         # Print outliers for the current column
#         if len(outliers) > 0:
#             print(f"Outliers in {col}:")
#             print(outliers)
#
#
# # Detect outliers in all columns
# detect_outliers(df.copy(), df.columns)  # Use a copy to avoid modifying original df

#
# import pandas as pd
# import numpy as np  # Import numpy for IQR calculation
#
# def detect_outliers(df, columns):
#   outlier_dict = {}  # Create a dictionary to store outliers for each column
#   for col in columns:
#       # Calculate the IQR
#       Q1 = df[col].quantile(0.25)
#       Q3 = df[col].quantile(0.75)
#       IQR = np.percentile(df[col], 75) - np.percentile(df[col], 25)  # Use numpy for IQR
#
#       # Define the outlier boundaries
#       lower_bound = Q1 - 1.5 * IQR
#       upper_bound = Q3 + 1.5 * IQR
#
#       # Find outliers
#       outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
#
#       # Add outliers to the dictionary
#       outlier_dict[col] = outliers.index.to_list()  # Store outlier row indices as a list
#
#   return outlier_dict  # Return the dictionary containing outlier indices for each column
#
# # Example usage
# data = {'Column1': [1, 2, 3, 100, 5, 6, 7, 8, 9], 'Column2': [1.5, 2.5, 3.5, 10.5, 5.5, 6.5, 7.5, 8.5, 9.5]}
# df = pd.DataFrame(data)
# outliers_by_column = detect_outliers(df.copy(), df.columns)
#
# # Access outliers for a specific column
# column_name = 'Column1'
# if column_name in outliers_by_column:
#   print(f"Outliers in {column_name}: {outliers_by_column[column_name]}")
# else:
#   print(f"No outliers found in {column_name}")

# import pandas as pd


# def detect_outliers(df, columns):
#   outlier_dict = {}  # Create a dictionary to store outliers for each column
#   for col in columns:
#       # Calculate the IQR
#       Q1 = df[col].quantile(0.25)
#       Q3 = df[col].quantile(0.75)
#       IQR = Q3 - Q1
#
#       # Define the outlier boundaries
#       lower_bound = Q1 - 1.5 * IQR
#       upper_bound = Q3 + 1.5 * IQR
#
#       # Find outliers with values
#       outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)][[col]]  # Select only the column
#
#       # Add outliers to the dictionary as a list of tuples (index, value)
#       outlier_dict[col] = outliers.apply(lambda row: (row.name, row.iloc[0]), axis=1).tolist()
#
#   return outlier_dict  # Return the dictionary containing outlier information
#
# # Example usage
# data = {'Column1': [1, 2, 3, 100, 5, 6, 7, 8, 9], 'Column2': [1.5, 2.5, 3.5, 10.5, 5.5, 6.5, 7.5, 8.5, 9.5]}
# df = pd.DataFrame(data)
# outliers_by_column = detect_outliers(df.copy(), df.columns)
#
# # Access outliers for a specific column
# column_name = 'Column1'
# if column_name in outliers_by_column:
#   print(f"Outliers in {column_name}:")
#   for index, value in outliers_by_column[column_name]:
#     print(f"- Index: {index}, Value: {value}")
# else:
#   print(f"No outliers found in {column_name}")


# from scipy import stats
# import pandas as pd
#
# # Assuming df is your DataFrame
# intFloatColumns = ["ages", "presentPrice"]
#
# # Filter the DataFrame
# outliersDf = df[intFloatColumns]
#
# def detect_outliers(df, columns):
#   for col in columns:
#       # Calculate the IQR
#       Q1 = df[col].quantile(0.25)
#       Q3 = df[col].quantile(0.75)
#       IQR = stats.iqr(df[col])
#
#       # Define the outlier boundaries
#       lower_bound = Q1 - 1.5 * IQR
#       upper_bound = Q3 + 1.5 * IQR
#
#       # Find outliers
#       outliers = df[col][(df[col] < lower_bound) | (df[col] > upper_bound)]
#       non_outliers = df[col][(df[col] >= lower_bound) & (df[col] <= upper_bound)]
#
#       # Print information about the outliers
#       print(f"Outliers for column '{col}':")
#       print(f"- Number of outliers: {len(outliers)}")
#
#       # Print outliers for the current column
#       if len(outliers) > 0:
#         print(f"Outliers in {col}:")
#         print(outliers.to_list())
#
# detect_outliers(outliersDf, intFloatColumns)


#
# # Use SMOTE to oversample the minority class
#
# from imblearn.over_sampling import SMOTE
#
# smote = SMOTE()
# X_resampled, y_resampled = smote.fit_resample(X, y)


import tensorflow
import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

featuresSelected = ['carName', 'ages', 'locations_Arusha', 'locations_Kampala', 'locations_Kisumu', 'locations_Lamu', 'locations_Mwanza', 'locations_Nairobi']
df = pd.read_csv("/content/scaledDf.csv")
def unsupervised_car_recommendation(data, featuresSelected, num_recommendations=4):
    """
  Recommends cars based on location preferences using an unsupervised Neural Network.

  Args:
      data: A pandas DataFrame containing car data.
      featuresSelected: A list of feature names used for the model.
      num_recommendations: Number of car recommendations to return (default: 4).

  Returns:
      A list of the top-n recommended car names.
  """

    # Preprocess data
    categorical_features = [col for col in featuresSelected if col.startswith("locations_")]
    transformer = ColumnTransformer([("onehot", OneHotEncoder(sparse=False), categorical_features)],
                                    remainder="passthrough")
    transformed_data = transformer.fit_transform(data[featuresSelected])

    # Build the unsupervised Neural Network
    model = Sequential()
    model.add(Dense(128, activation="relu", input_shape=(transformed_data.shape[1],)))
    model.add(Dense(64, activation="relu"))
    model.add(Dense(transformed_data.shape[1], activation="sigmoid"))  # Output with same dimensionality as input

    # Compile and train the model (unsupervised learning with mean squared error)
    model.compile(loss="mse", optimizer="adam")
    model.fit(transformed_data, transformed_data, epochs=10, verbose=0)

    # Get test data (assuming locations_Nairobi is set to 1 for user preference)
    test_data = np.array([[0, 0, 0, 0, 0, 0, 1, 0]])  # Set locations_Nairobi to 1

    # Encode test data
    encoded_test_data = transformer.transform(test_data)

    # Get activations from the last layer (interpreted as encoded preferences)
    encoded_preferences = model.predict(encoded_test_data)[0]

    # Calculate cosine similarity to measure preference similarity
    similarities = np.dot(transformed_data, encoded_preferences)

    # Sort cars based on similarity (descending order)
    sorted_indices = np.argsort(similarities)[::-1]

    # Return top recommendations (excluding the test car itself)
    return data["carName"].iloc[sorted_indices[1:num_recommendations + 1]].tolist()


# Example usage (assuming your data is in a pandas DataFrame called 'car_data')
recommended_cars = unsupervised_car_recommendation(car_data.copy(), featuresSelected, num_recommendations=4)
print(f"Recommended Cars: {recommended_cars}")
