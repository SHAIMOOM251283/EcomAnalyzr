import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

class DashBoard:

    def __init__(self):
        self.app = dash.Dash(__name__)
        self.laptops, self.phones = self.load_data()
        self.set_up_app_layout()

    def load_data(self):
        # DemoBlaze data
        demo_laptops = pd.read_csv("DemoBlaze/laptops_data.csv")
        demo_phones = pd.read_csv("DemoBlaze/phones_data.csv")
        demo_laptops['Price'] = demo_laptops['Price'].replace('[\$,]', '', regex=True).astype(float)
        demo_phones['Price'] = demo_phones['Price'].replace('[\$,]', '', regex=True).astype(float)
        demo_laptops['Source'] = 'DemoBlaze'
        demo_phones['Source'] = 'DemoBlaze'

        # AjaxData data
        ajax_laptops = pd.read_csv("AjaxData/laptops_data.csv")
        ajax_phones = pd.read_csv("AjaxData/phones_data.csv")
        ajax_laptops['Price'] = ajax_laptops['Price'].replace('[\$,]', '', regex=True).astype(float)
        ajax_phones['Price'] = ajax_phones['Price'].replace('[\$,]', '', regex=True).astype(float)
        ajax_laptops['Source'] = 'AjaxData'
        ajax_phones['Source'] = 'AjaxData'

        # Combine datasets for laptops and phones
        laptops = pd.concat([demo_laptops, ajax_laptops], ignore_index=True)
        phones = pd.concat([demo_phones, ajax_phones], ignore_index=True)

        return laptops, phones

    def set_up_app_layout(self):
        # Set up the app layout
        self.app.layout = html.Div([
            html.H1("E-Commerce Product Comparison"),
    
            # Dropdown for category selection
            html.Label("Select Category:"),
            dcc.Dropdown(
                id="category-dropdown",
                options=[
                    {"label": "Laptops", "value": "Laptops"},
                    {"label": "Phones", "value": "Phones"}
                ],
                value="Laptops"
            ),
    
            # Three graphs for bar chart, scatter plot, and box plot
            html.Div([
                dcc.Graph(id="bar-chart"),
                dcc.Graph(id="scatter-plot"),
                dcc.Graph(id="box-plot")
            ])
        ])

    def update_charts(self, selected_category):
        # Select the data based on the dropdown choice
        data = self.laptops if selected_category == "Laptops" else self.phones

        # Bar chart: average prices by source
        bar_fig = px.bar(
            data.groupby('Source')['Price'].mean().reset_index(),
            x='Source',
            y='Price',
            title=f"Average Prices for {selected_category}",
            labels={'Price': 'Average Price (USD)', 'Source': 'Data Source'},
            color='Source'
        )

        # Scatter plot: price distribution by product
        scatter_fig = px.scatter(
            data,
            x='Product',
            y='Price',
            color='Source',
            title=f"{selected_category} Price Distribution",
            labels={'Price': 'Price (USD)', 'Product': 'Product'}
        )

        # Box plot: price distribution across sources
        box_fig = px.box(
            data,
            x='Source',
            y='Price',
            title=f"{selected_category} Price Range by Source",
            labels={'Price': 'Price (USD)', 'Source': 'Data Source'},
            color='Source'
        )

        return bar_fig, scatter_fig, box_fig

    def callback_to_update_graphs(self):
        @self.app.callback(
            [Output("bar-chart", "figure"),
            Output("scatter-plot", "figure"),
            Output("box-plot", "figure")],
            [Input("category-dropdown", "value")]
        )
        def update_graph(selected_category):
            return self.update_charts(selected_category)

    def run(self):
        self.callback_to_update_graphs()  # Register the callback
        self.app.run_server(debug=True)

if __name__ == '__main__':
    dashboard = DashBoard()
    dashboard.run()
