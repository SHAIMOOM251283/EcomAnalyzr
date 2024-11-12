import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException
import time

class DataExtraction:

    def __init__(self):
        self.url = "https://www.demoblaze.com/"
        self.driver = webdriver.Firefox()
        self.data_dir = "DemoBlaze"
        
        # Create directory to save CSV files
        os.makedirs(self.data_dir, exist_ok=True)

    def extract_data(self):
        extracted_data = []  # Store extracted data in a list of dictionaries
        while True:
            # Extract product data on the current page
            products = self.driver.find_elements(By.CLASS_NAME, "card-block")
            for product in products:
                title = product.find_element(By.CLASS_NAME, "card-title").text
                price = product.find_element(By.TAG_NAME, "h5").text
                extracted_data.append({"Product": title, "Price": price})
    
            try:
                # Find the 'Next' button and scroll into view using JavaScript
                next_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#next2')))
                self.driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
                time.sleep(1)  # Allow a brief pause for smooth scrolling
        
                # Now attempt to click the 'Next' button
                next_button.click()
                time.sleep(3)  # Wait for the next page to load

            except (ElementNotInteractableException):    
                print("No more pages to navigate or 'Next' button is not clickable.")
                break  # Exit loop if 'Next' button is not found or not interactable

        return extracted_data  # Return the collected data
    
    def navigate_and_extract(self, category_button_selector):
        """Navigates to a category and extracts data by calling extract_data."""
        category_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, category_button_selector)))
        category_button.click()
        time.sleep(3)  # Wait for the page to load
        
    def save_data_to_csv(self, data, filename):
        # Convert data to DataFrame and save as CSV
        df = pd.DataFrame(data)
        csv_path = os.path.join(self.data_dir, filename)
        df.to_csv(csv_path, index=False)
        print(f"Data saved to {csv_path}")

    def extract_homepage_data(self):
        self.driver.get(self.url)
        time.sleep(3)
        data = self.extract_data()
        self.save_data_to_csv(data, "all_data.csv")
        
    def extract_phones_data(self):
        self.navigate_and_extract('a.list-group-item:nth-child(2)')
        data = self.extract_data()
        self.save_data_to_csv(data, "phones_data.csv")

    def extract_laptops_data(self):
        self.navigate_and_extract('a.list-group-item:nth-child(3)')
        data = self.extract_data()
        self.save_data_to_csv(data, "laptops_data.csv")

    def extract_monitors_data(self):
        self.navigate_and_extract('a.list-group-item:nth-child(4)')
        data = self.extract_data()
        self.save_data_to_csv(data, "monitors_data.csv")
        
    def quit_browser(self):
        self.driver.quit()
    
    def run(self):
        self.extract_homepage_data()
        self.extract_phones_data()
        self.extract_laptops_data()
        self.extract_monitors_data()
        self.quit_browser()

if __name__ == '__main__':
    extract = DataExtraction()
    extract.run()
