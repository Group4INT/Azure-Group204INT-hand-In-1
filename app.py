# Dash
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output

# Plotly
import plotly.express as px

# Get data
import dataModel
order = dataModel.get_data()
df_year = dataModel.get_year()
df_month = dataModel.get_month()



dash_app = dash.Dash(__name__)
app = dash_app.server

# Layout
dash_app.layout = html.Div(
    children=[
        html.Div(className='row',
                 children=[
                     html.Div(className='four columns div-user-controls',
                              children=[
                                  html.H2('Sales dashboard'),
                                  html.P('Select filters from dropdown'),

                                  html.Div(children="Month",
                                           className="menu-title"),
                                  dcc.Dropdown(
                                      id='drop_month',
                                      options=[{'label': selectmonth, 'value': selectmonth}
                                               for selectmonth in df_month['monthnames']],
                                  ),
                                  html.Div(children="Year",
                                           className="menu-title"),
                                  dcc.Dropdown(
                                      id='drop_year',
                                      options=[
                                         {'label': selectyear, 'value': selectyear} for selectyear in df_year]
                                  ),
                              ]
                              ),
                     html.Div(className='eight columns div-for-charts bg-grey',
                              children=[
                                  dcc.Graph(id="sales_product",

                                            )
                              ]
                              ),
                     html.Div(className='four columns div-user-controls',
                              children=[
                                  html.H2('Sales dashboard'),
                                  html.P('Select filters from dropdown'),

                                  html.Div(children="Month",
                                           className="menu-title"),
                                  dcc.Dropdown(
                                      id='drop_month2',
                                      options=[{'label': selectmonth, 'value': selectmonth}
                                               for selectmonth in df_month['monthnames']],
                                  ),
                                  html.Div(children="Year",
                                           className="menu-title"),
                                  dcc.Dropdown(
                                      id='drop_year2',
                                      options=[
                                          {'label': selectyear, 'value': selectyear} for selectyear in df_year]
                                  ),
                              ]
                              ),
                     html.Div(className='eight columns div-for-charts bg-grey',
                                        children=[
                                            dcc.Graph(id="sales_employee",

                                                      )
                                        ]
                              ),

                 ]
                 )
    ]
)

# # Diagram - Product Sales

@ dash_app.callback(Output('sales_product', 'figure'),
                    [Input('drop_month', 'value')],
                    [Input('drop_year', 'value')])
def update_graph(drop_month, drop_year):
    if drop_year:
        if drop_month:
            order_fig1 = order.loc[(order['orderyear'] == drop_year) & (
                order['ordermonth'] == drop_month)]
        else:
            order_fig1 = order.loc[order['orderyear'] == drop_year]
    else:
        if drop_month:
            order_fig1 = order.loc[order['ordermonth'] == drop_month]
        else:
            order_fig1 = order

    return px.bar(order_fig1, x="productname", y="total", title="Sales by product",  color='type', labels={'total': 'Total sales', 'productname': 'Product name', 'type': 'Product Type'})



# Employee Sales  Diagram 

@dash_app.callback(Output('sales_employee', 'figure'),
                   [Input('drop_month2', 'value')],
                   [Input('drop_year2', 'value')])
def update_graph(drop_month, drop_year):
    if drop_year:
        if drop_month:
            order_fig1 = order.loc[(order['orderyear'] == drop_year) & (
                order['ordermonth'] == drop_month)]
        else:
            order_fig1 = order.loc[order['orderyear'] == drop_year]
    else:
        if drop_month:
            order_fig1 = order.loc[order['ordermonth'] == drop_month]
        else:
            order_fig1 = order

    return px.bar(order_fig1,
                  x='emp_name', y='total',
                  color='type',  title='Sales by Employee',
                  hover_data=[],
                  labels={'total': 'Total sales', 'emp_name': 'Employee', 'type': 'Product Type'})


# Run the app
if __name__ == '__main__':
    dash_app.run_server(debug=True)