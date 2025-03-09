from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time

# from flask import Flask, jsonify, request
# from flask_cors import CORS  
# from selenium.webdriver.chrome.options import Options

website = "https://ytmp3.cc/wBa5/"
url = input("Enter the youtube link you want to convert: ")
# print(url)

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
driver = webdriver.Chrome(options = options)
driver.get(website)

try:
    # Wait for the input to be present in the DOM
    input_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input"))
    )
    input_element.send_keys(url)
except Exception as e:
    print(f"Error waiting for input reader: {e}")
    driver.quit()


try:
    # Press the convert button for the user
    convert_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    )
    convert_button.click()
except Exception as e:
    print("Ass nigga")
    driver.quit()

try:
    # Press the convert button for the user
    download_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='button']"))
    )
    download_button.click()
except Exception as e:
    print("Ass nigga")
    driver.quit()

time.sleep(5)