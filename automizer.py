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
import concurrent.futures
# from flask import Flask, jsonify, request
# from flask_cors import CORS  
# from selenium.webdriver.chrome.options import Options

def downloader(url):
    website = "https://ytmp3.cc/wBa5/"
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
        input_element = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input"))
        )
        input_element.send_keys(url)
    except Exception as e:
        print(f"Error waiting for input reader: {e}")
        driver.quit()

    try:
        # Press the convert button for the user
        convert_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
        )
        convert_button.click()
    except Exception as e:
        print("Convert button never popped up")
        driver.quit()
       

    try:
        # Press the convert button for the user
        download_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='button']"))
        )
        download_button.click()
    except Exception as e:
        print("Download button never popped up")
        driver.quit()
    
    time.sleep(10)
    driver.quit()

#######################################

def playlist_downloader(playlist_url):
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    driver = webdriver.Chrome(options = options)
    driver.get(playlist_url)

 
     # Wait for the content to be present in the DOM
    input_element = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.XPATH, "//div[@id='contents' and contains(@class, ' style-scope ytd-item-section-renderer style-scope ytd-item-section-renderer')]"))
    )
    
    page = driver.page_source
    soup = BeautifulSoup(page, "html.parser")
    url_data = soup.find_all("a", class_="yt-simple-endpoint style-scope ytd-playlist-video-renderer")
    hrefs = [a["href"] for data in url_data for a in soup.find_all("a", class_="yt-simple-endpoint style-scope ytd-playlist-video-renderer")]
    
    revised_hrefs = []
    for href in hrefs:
        revised_hrefs.append("youtube.com" + href)
    
    driver.quit()
    # for href in revised_hrefs:
    #     print(href)
    
    max = 10
    with concurrent.futures.ThreadPoolExecutor(max_workers=max) as executor:
        executor.map(downloader, revised_hrefs)
    
# For testing playlist downloader
playlist_downloader("https://www.youtube.com/playlist?list=PLRBp0Fe2Gpglq-J-Hv0p-y0wk3lQk570u")


# For testing downloader
# url_array = ["https://youtu.be/Lx3MGrafykU?si=wMhmQYGRSEGpkae7",
#              "https://youtu.be/NSCZ5awmH1U?si=bnuf8JJRXmjw_tnN",
#              "https://youtu.be/ljxYE-aJD3A?si=8nszUC0PnhnwP_Dy",
#              "https://youtu.be/INsVZ3ACwas?si=X9ZfHIT4cslFM13D"]

# with concurrent.futures.ThreadPoolExecutor() as executor:
#     executor.map(downloader, url_array)
# print("Done")