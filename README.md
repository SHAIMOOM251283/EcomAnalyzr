# EcomAnalyzr

EcomAnalyzr is a comprehensive e-commerce data analysis project that automates data extraction from multiple e-commerce platforms, processes and cleans the data, visualizes it with various insights, and hosts an interactive dashboard for real-time exploration. This project leverages Python’s `Selenium` for web scraping, `Plotly` for data visualization, and `Dash` for creating a user-friendly dashboard interface.

## Features
- **Automated Web Scraping**: Extracts e-commerce product data, including laptops, phones, tablets, and monitors from multiple sources.
- **Data Cleaning & Processing**: Consolidates data, cleans pricing fields, and prepares datasets for analysis.
- **Insightful Visualizations**: Provides comparative visualizations of product prices across sources.
- **Interactive Dashboard**: A `Dash`-based interactive dashboard for dynamic data exploration.

## Project Structure
1. **ecommerce_ajax_extraction.py**: Scrapes product data from a test e-commerce site using AJAX and saves it as CSV files.
2. **demoblaze_extraction.py**: Scrapes product data from the DemoBlaze site, similar to the AJAX scraper, and saves it to the project directory.
3. **data_visualization.py**: Cleans and processes the data, then generates visualizations including bar charts, scatter plots, and box plots for price insights.
4. **price_insight_dashboard.py**: Hosts an interactive dashboard where users can explore product prices by category and source.

## Installation

### Step 1: Clone the Repository

You have multiple options to clone the repository based on your preference:

#### Option 1: Using the Terminal
1. Open a terminal window.
2. Run the following commands:

   ```bash
   git clone https://github.com/SHAIMOOM251283/EcomAnalyzr.git
   cd EcomAnalyzr
   ```

#### Option 2: Using VS Code's Git Integration
1. Open **Visual Studio Code**.
2. Press `Ctrl + Shift + P` (or `Cmd + Shift + P` on macOS) to open the Command Palette.
3. Type **Git: Clone** and select it.
4. Enter the repository URL:

   ```
   https://github.com/SHAIMOOM251283/EcomAnalyzr.git
   ```

5. Choose a local folder to clone the repository into, then select **Open** to load the repository in VS Code.

#### Option 3: Using VS Code's Integrated Terminal
1. Open **VS Code**.
2. Open the integrated terminal by pressing `Ctrl + ` (backtick) or by navigating to **Terminal > New Terminal**.
3. Run the following commands in the integrated terminal:

   ```bash
   git clone https://github.com/SHAIMOOM251283/EcomAnalyzr.git
   cd EcomAnalyzr
   ```

### Step 2: Set Up the Python Environment and Install Dependencies

Ensure you have Python installed (preferably version 3.8 or later).

1. **Create a Virtual Environment** (recommended for isolated dependencies):
   
   ```bash
   python -m venv .venv
   ```

2. **Activate the Virtual Environment**:
   - **Linux/macOS**:
     ```bash
     source .venv/bin/activate
     ```
   - **Windows**:
     ```bash
     .venv\Scripts\activate
     ```

3. **Install Required Packages**:
   
   Run the following command to install all necessary packages:

   ```bash
   pip install pandas plotly dash selenium
   ```

### Step 3: Verify Installation in VS Code

1. **Open the Project Folder**:
   - In VS Code, go to `File > Open Folder`, and select the `EcomAnalyzr` directory.

2. **Select Python Interpreter**:
   - Press `Ctrl + Shift + P` (or `Cmd + Shift + P` on macOS) to open the Command Palette.
   - Type **Python: Select Interpreter** and select the interpreter from the `.venv` directory created in Step 2.

### Step 4: Set up WebDriver:
   - Ensure you have [geckodriver](https://github.com/mozilla/geckodriver/releases) installed and added to your system’s PATH for Firefox. 

## Usage

1. **Data Extraction**:
   - To start data extraction, run `demoblaze_extraction.py` and `ecommerce_ajax_extraction.py`. These scripts will fetch data for laptops, tablets, and phones and save them as CSV files in `DemoBlaze` and `AjaxData` directories.

   ```bash
   python demoblaze_extraction.py
   python ecommerce_ajax_extraction.py
   ```

2. **Data Visualization**:
   - To view static visualizations, execute `data_visualization.py`. This will display average price comparisons, individual product price distributions, and price ranges across sources.

   ```bash
   python data_visualization.py
   ```

3. **Run Dashboard**:
   - For an interactive experience, launch the `price_insight_dashboard.py` script to explore data dynamically via the Dash dashboard.

   ```bash
   python price_insight_dashboard.py
   ```

   - Access the dashboard in your web browser at `http://127.0.0.1:8050`.

## Visualizations
The project includes the following types of visualizations:
- **Average Price Comparison**: Bar chart displaying average prices across different sources for each category.
![Bar Chart](https://github.com/SHAIMOOM251283/EcomAnalyzr/blob/main/BarChart.png)
- **Individual Product Prices**: Scatter plot showing individual product prices categorized by source.
![Scatter Plot](https://github.com/SHAIMOOM251283/EcomAnalyzr/blob/main/ScatterPlot.png)
- **Price Range Distribution**: Box plot illustrating price distribution across sources for each product category.
![Box Plot](https://github.com/SHAIMOOM251283/EcomAnalyzr/blob/main/BoxPlot.png)

## Project Highlights
- **Web Scraping**: Automated data extraction using `Selenium` to handle AJAX and standard page loads.
- **Data Cleaning and Transformation**: Consolidating data from multiple sources and preparing it for visualization.
- **Data Visualization**: Creating insightful plots with `Plotly` to aid in comparative analysis.
- **Dashboard Development**: Building a user-friendly, interactive interface with `Dash` to empower users to analyze data visually.

### Dashboard Functionality Demonstration
Watch the video below to see the dashboard in action:
[![Watch the Dashboard Functionality Screencast](https://img.shields.io/badge/Watch%20Video-Click%20Here-blue)](https://github.com/SHAIMOOM251283/EcomAnalyzr/blob/main/DashboardScreencast.mp4)

## Future Improvements
- Expand data extraction to include more categories and platforms.
- Add more interactive components to the dashboard, such as filtering by price range.
- Implement machine learning for price prediction or product trend analysis.

## License
This project is licensed under the MIT License.
