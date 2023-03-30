import os
import random
from os import path


from selenium import webdriver
import time
import bs4
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.chrome.options import Options

import speech_recognition as sr
import ffmpy
import requests
import urllib
import pydub
from pydub import AudioSegment








def solve_captcha():


    email_list = []

    for index in range(1000):
        url = 'https://www.gmailnator.com/?_ga=2.189985385.355790114.1647274766-867144290.1647274766'
    
        # Set OPTS for the driver #
        options = webdriver.ChromeOptions()
        options.add_argument("no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=800,600")
        options.add_argument("--disable-dev-shm-usage")    
        driver = webdriver.Chrome(options=options, executable_path=r'C:\Users\kkeel\webdrivers\chromedriver.exe')
        driver.get(url)    
        page1 = driver.page_source
        soup = bs4.BeautifulSoup(page1, "lxml")
        table = soup.find('div', attrs = {'id':'__init__'})

        driver.maximize_window()


        for x in range(1):
            # First Name #
            link = None
            while not link:
                try:
                    email = driver.find_element_by_xpath('/html/body/section/div[1]/div/div/div[2]/div/div[1]').get_attribute("innerText")
                    email_list.append(email)
                    print("done")
                    break
                except NoSuchElementException:
                    time.sleep(0.1)

            # First Name #
            link = None
            while not link:
                try:
                    gen_new = driver.find_element_by_xpath('//*[@id="generate_button"]')
                    gen_new.click()
                    print("done")
                    break
                except NoSuchElementException:
                    time.sleep(0.1)


        print (email_list)

       


solve_captcha()
