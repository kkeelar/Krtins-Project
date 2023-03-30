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

    url = 'https://fantasy.espn.com/tournament-challenge-bracket/2022/en/game'

    for index in range(1000):
        url = 'https://fantasy.espn.com/tournament-challenge-bracket/2022/en/game'
    
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


        # Clicks create bracket #
        link = None
        while not link:
            try:
                create = driver.find_element_by_xpath('//*[@id="main-container"]/div[1]/section[1]/div/div[4]/div[1]/a')
                create.click()
                print("done")
                break
            except NoSuchElementException:
                time.sleep(0.1)

        # Clicks sign up #
        link = None
        while not link:
            try:
                
                driver.switch_to.default_content()
                WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'//*[@id="disneyid-iframe"]')))
                print ('sgs')
                sign_up_btn = driver.find_element_by_xpath('//*[@id="did-ui-view"]/div/section/section/form/section/div[5]/a')
                driver.execute_script("arguments[0].click();", sign_up_btn)
                print("done")
                break
            except NoSuchElementException:
                time.sleep(0.1)


        # Signs in #

        # First Name #
        link = None
        while not link:
            try:
                driver.switch_to.default_content()
                WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'//*[@id="disneyid-iframe"]')))
                first_name WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="did-ui-view"]/div/section/section/form/section[1]/div[1]/div[1]/label/span[2]/input')))
                first_name.send_keys('Krtin')
                print("done")
                break
            except NoSuchElementException:
                time.sleep(0.1)

        time.sleep(1)
                
        # Last Name #
        link = None
        while not link:
            try:    
                driver.switch_to.default_content()
                WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'//*[@id="disneyid-iframe"]')))
                last_name = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="did-ui-view"]/div/section/section/form/section[1]/div[1]/div[2]/label/span[2]/input')))
                last_name.send_keys('Keelar')
                print("done")
                break
            except NoSuchElementException:
                time.sleep(0.1)

        time.sleep(1)
        

        varb = index+6
        use_varb = str(varb)
        # Email #
        link = None
        while not link:
            try:
                driver.switch_to.default_content()
                WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'//*[@id="disneyid-iframe"]')))
                email = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="did-ui-view"]/div/section/section/form/section[1]/div[2]/div/label/span[2]/input')))
                email.send_keys('kkeelar%d@gmail.com' % varb)
                print("done")
                break
            except NoSuchElementException:
                time.sleep(0.1)


        time.sleep(1)
        

        # Password #
        link = None
        while not link:
            try:
                driver.switch_to.default_content()
                WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'//*[@id="disneyid-iframe"]')))
                password = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="did-ui-view"]/div/section/section/form/section[1]/div[4]/div[1]/label/span[2]/input')))
                password.send_keys('Th3f!ash')
                print("done")
                break
            except NoSuchElementException:
                time.sleep(0.1)
        

        

        # Logs in with already made account #
        link = None
        while not link:
            try:
                email_input = driver.find_element_by_xpath('//*[@id="did-ui-view"]/div/section/section/form/section/div[1]/div/label/span[2]/input')
                email_input.send_keys('kkeelar1@gmail.com')
                print("done")
                break
            except NoSuchElementException:
                time.sleep(0.1)










solve_captcha()
