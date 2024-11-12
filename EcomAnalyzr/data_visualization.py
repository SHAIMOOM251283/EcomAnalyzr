import pandas as pd
import os
import plotly.express as px

class DataVisualization:

    def __init__(self):
        self.demoblaze_dir = "DemoBlaze"
        self.ajaxdata_dir = "AjaxData"
        self.categories = ["laptops", "phones"]

    def load_all_data(self):
        laptops_data = pd.DataFrame()
        phones_data = pd.DataFrame()

        # Iterate through each category and load data
        for category in self.categories:
            # Load data for Demoblaze and AjaxData directly
            demoblaze_path = os.path.join(self.demoblaze_dir, f"{category}_data.csv")
            ajaxdata_path = os.path.join(self.ajaxdata_dir, f"{category}_data.csv")
            
            # Load data from files if they exist
            demoblaze_data = pd.read_csv(demoblaze_path) if os.path.exists(demoblaze_path) else pd.DataFrame()
            ajaxdata_data = pd.read_csv(ajaxdata_path) if os.path.exists(ajaxdata_path) else pd.DataFrame()
            
            # Add source columns
            demoblaze_data["Source"] = "DemoBlaze"
            ajaxdata_data["Source"] = "AjaxData"

            # Concatenate data from both sources
            combined = pd.concat([demoblaze_data, ajaxdata_data], ignore_index=True)

            # Assign the combined data to the appropriate variable
            if category == "laptops":
                laptops_data = combined
            elif category == "phones":
                phones_data = combined

        return laptops_data, phones_data
    
    def clean_all_data(self, laptops_data, phones_data):
        # Clean the price column and add category labels
        laptops_data['Price'] = laptops_data['Price'].replace('[\$,]', '', regex=True).astype(float)
        phones_data['Price'] = phones_data['Price'].replace('[\$,]', '', regex=True).astype(float)
        
        laptops_data['Category'] = 'Laptops'
        phones_data['Category'] = 'Phones'
        
        # Concatenate both dataframes
        combined_data = pd.concat([laptops_data, phones_data], ignore_index=True)
        return combined_data
    
    def calculate_avg_prices(self, combined_data):
        # Calculate the average prices by category and source
        avg_prices = combined_data.groupby(['Category', 'Source'])['Price'].mean().reset_index()
        return avg_prices

    def plot_avg_prices(self, avg_prices):
        fig = px.bar(
            avg_prices,
            x='Category',
            y='Price',
            color='Source',
            barmode='group',
            title='Average Price Comparison of Laptops and Phones across Sources',
            labels={'Price': 'Average Price (USD)', 'Category': 'Product Category'}
        )
        fig.show()

    def plot_individual_prices(self, combined_data):
        fig = px.scatter(
            combined_data,
            x='Category',
            y='Price',
            color='Source',
            title='Individual Product Prices by Category and Source',
            labels={'Price': 'Price (USD)', 'Category': 'Product Category'},
            hover_data=['Product']  # Display product name on hover
        )
        fig.show()

    def plot_price_distribution(self, combined_data):
        fig = px.box(
            combined_data,
            x='Category',
            y='Price',
            color='Source',
            title='Price Distribution of Laptops and Phones across Sources',
            labels={'Price': 'Price (USD)', 'Category': 'Product Category'}
        )
        fig.show()
    
    def run(self):
        # Load and clean data
        laptops_data, phones_data = self.load_all_data()
        combined_data = self.clean_all_data(laptops_data, phones_data)

        # Calculate average prices
        avg_prices = self.calculate_avg_prices(combined_data)

        # Plot the results
        self.plot_avg_prices(avg_prices)
        self.plot_individual_prices(combined_data)
        self.plot_price_distribution(combined_data)

# Main Execution
if __name__ == "__main__":
    Data_Viz = DataVisualization()
    Data_Viz.run()