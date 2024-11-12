import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
import time

class DataExtraction:

    def __init__(self):
        self.url = "https://webscraper.io/test-sites/e-commerce/ajax"
        self.driver = webdriver.Firefox()
        self.data_dir = "AjaxData"
        os.makedirs(self.data_dir, exist_ok=True)

    def extract_data(self):
        extracted_data = []
        while True:
            products = self.driver.find_elements(By.CSS_SELECTOR, "div.col-md-4") 
            for product in products:
                title = product.find_element(By.CLASS_NAME, "title").text
                price = product.find_element(By.CLASS_NAME, "price").text
                extracted_data.append({"Product": title, "Price": price})
    
            try:
                next_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.next')))
                self.driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
                time.sleep(1)  
                next_button.click()
                time.sleep(3) 
            except (ElementClickInterceptedException):
                print("No more pages to navigate or 'Next' button is not clickable.")
                break
        
        return extracted_data

    def click_button(self, category_button_selector):
        category_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, category_button_selector)))
        category_button.click()
        time.sleep(3)  
    
    def save_data_to_csv(self, data, filename):
        # Convert data to DataFrame and save as CSV
        df = pd.DataFrame(data)
        csv_path = os.path.join(self.data_dir, filename)
        df.to_csv(csv_path, index=False)
        print(f"Data saved to {csv_path}")
        
    def extract_laptops_data(self):
        self.driver.get(self.url)
        time.sleep(3)
        self.click_button('#side-menu > li:nth-child(2) > a:nth-child(1)')
        self.click_button('ul.nav:nth-child(2) > li:nth-child(1) > a:nth-child(1)')
        data = self.extract_data()
        self.save_data_to_csv(data, "laptops_data.csv")
        self.driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(1)
        
    def extract_tablets_data(self):
        self.click_button('ul.nav:nth-child(2) > li:nth-child(2) > a:nth-child(1)')
        data = self.extract_data()
        self.save_data_to_csv(data, "tablets_data.csv")
        self.driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(1)
        
    def extract_phones_data(self):
        self.click_button('#side-menu > li:nth-child(3) > a:nth-child(1)')
        self.click_button('.subcategory-link')
        data = self.extract_data()
        self.save_data_to_csv(data, 'phones_data.csv')

    def quit_browser(self):
        self.driver.quit()
    
    def run(self):
        self.extract_laptops_data()
        self.extract_tablets_data()
        self.extract_phones_data()
        self.quit_browser()

if __name__ == '__main__':
    extract = DataExtraction()
    extract.run()            