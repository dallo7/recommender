from dash import dcc, html

block_content = [
    dcc.Markdown(
        "'This class of SUVs are bold and classy'", style={'font-family': 'Caramel'}
    ),
    html.Span(
        "Amount : 250 - 400 Negotiable", style={'font-family': 'Times New Roman'}
    )
]