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

    url = 'https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp'

    for index in range(1000):
        url = 'https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp'
    
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


        # First Name #
        link = None
        while not link:
            try:
                first_name = driver.find_element_by_xpath('//*[@id="firstName"]')
                first_name.send_keys('Krtin')
                print("done")
                break
            except NoSuchElementException:
                time.sleep(0.1)

        # Last Name #
        link = None
        while not link:
            try:
                last_name = driver.find_element_by_xpath('//*[@id="lastName"]')
                last_name.send_keys('Keelar')
                print("done")
                break
            except NoSuchElementException:
                time.sleep(0.1)

        varb = index+10
        # Email #
        link = None
        while not link:
            try:
                email = driver.find_element_by_xpath('//*[@id="username"]')
                email.send_keys('kkeelar%d' % varb)
                print("done")
                break
            except NoSuchElementException:
                time.sleep(0.1)


        # Password #
        link = None
        while not link:
            try:
                password = driver.find_element_by_xpath('//*[@id="passwd"]/div[1]/div/div[1]/input')
                password.send_keys('Th3f!ash')
                print("done")
                break
            except NoSuchElementException:
                time.sleep(0.1)

        # Password Confirm #
        link = None
        while not link:
            try:
                password = driver.find_element_by_xpath('//*[@id="confirm-passwd"]/div[1]/div/div[1]/input')
                password.send_keys('Th3f!ash')
                print("done")
                break
            except NoSuchElementException:
                time.sleep(0.1)


solve_captcha()
