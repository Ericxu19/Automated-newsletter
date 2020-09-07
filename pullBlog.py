import json
import pickle
import time

import bs4
import colorama
import requests
from colorama import Back, Fore

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import json
import re

from datetime import date

import pdfkit 

# Initialize Colorama       
colorama.init(autoreset=True)

# Setup Selenium Webdriver
CHROMEDRIVER_PATH = r"/usr/local/share/chromedriver"
options = Options()
options.headless = True
# Disable Warning, Error and Info logs
# Show only fatal errors
options.add_argument("--log-level=3")
driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options=options)


# Get upto which problem it is already scraped from track.conf file


# Load chapters list that stores chapter info
# Store chapter info


def download(url, name):  
    print("fetching with url " + f" {url} ")
    
    try:

        driver.get(url)
        # Wait 20 secs or until div with id initial-loading disappears
        element = WebDriverWait(driver, 20).until(
            EC.invisibility_of_element_located((By.ID, "initial-loading"))
        )
        # Get current tab page source
        html = driver.page_source
        soup = bs4.BeautifulSoup(html, "html.parser")

        
        blog = soup.find("div", {"class": "blog-item-inner-wrapper"}) 
        if blog:
            b= []
            b.append(soup.find("div", {"class": "blog-item-title"}).text )
            b.append(soup.find("h4").text)
            b.append(blog)
            name.append(b)
            """
            with open("out.html", "ab") as f:
                f.write(blog.encode())
                f.write('<hr style="height:2px;border:none;color:#333;background-color:#333;">'.encode())
    """   
    except Exception as e:
        print(Back.RED + f" Failed Writing!!  {e} ")
        driver.quit()

def pullBlog():
    month = 8
    #month = date.today().month
    BASE_URL = "https://"

    # Load JSON from API
    
    name = []

    try: 
        for i in range(32):
             
            url = BASE_URL + str(month) + "-" + str(i)
             

             # Download each file as html
            download(url, name)
            
             

    finally:
        # Close the browser after download
        driver.quit()
    return name