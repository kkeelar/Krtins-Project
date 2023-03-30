import os
import random



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

url = 'https://www.footlocker.com/checkout'

maos_dic = {
    "fullname": "Michael Mao",
    "f_name": "Michael",
    "l_name": "Mao",
    "email": "kkeelar@gmail.com",
    "phone": 4704135954,
    "address": "9425 Prestwick Club Drive",
    "zip code": 30097,
    "city": "Duluth",
    "credit_card": 379593269671035,
    "cvv": 1673,
    "date_cc": "10/24",

}
    
    
    




def buy_shoe():
    #driver = webdriver.Chrome(executable_path=r'C:\Users\kkeel\webdrivers\chromedriver.exe')
    options = webdriver.ChromeOptions()
    options.add_argument("no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=800,600")
    options.add_argument("--disable-dev-shm-usage")
    #options.set_headless()
    driver = webdriver.Chrome(options=options, executable_path=r'C:\Users\kkeel\webdrivers\chromedriver.exe')
    driver.get(url)    
    page1 = driver.page_source
    soup = bs4.BeautifulSoup(page1, "lxml")
    table = soup.find('div', attrs = {'id':'__init__'})




    #First Name Function
    link = None
    while not link:
        try:
            send_info_fname = driver.find_element_by_xpath('//input[@name="firstName"]')
            break
        except NoSuchElementException:
            time.sleep(0.1)
    send_info_fname.send_keys(maos_dic["f_name"])

    #Last Name Function
    link = None
    while not link:
        try:
            send_info_lname = driver.find_element_by_xpath('//input[@name="lastName"]')
            break
        except NoSuchElementException:
            time.sleep(0.1)
    send_info_lname.send_keys(maos_dic["l_name"])

    #Send Email
    link = None
    while not link:
        try:
            print ("step 4")
            send_email = driver.find_element_by_xpath('//input[@name="email"]')
            send_email.send_keys("kkeelar@gmail.com")
            break
        except NoSuchElementException:
            print("waiting")
            time.sleep(0.1)

    #Phone Function
    link = None
    while not link:
        try:
            send_info_phone = driver.find_element_by_xpath('//input[@name="phone"]')
            break
        except NoSuchElementExcception:
            time.sleep(0.1)
    send_info_address.send_keys(maos_dic["phone"])

    #Save and Continue
    link = None
    while not link:
        try:
            save = driver.find_element_by_xpath('//button[text()="Save & Continue"]')
            break
        except NoSuchElementExcception:
            time.sleep(0.1)
    save.click()

    #Send Address
    link = None
    while not link:
        try:
            send_info_add = driver.find_element_by_xpath('//input[@name="line1"]')
            break
        except NoSuchElementExcception:
            time.sleep(0.1)
    send_info_add.send_keys(maos_dic["address"])

    
    #Zip code Function
    link = None
    while not link:
        try:
            send_info_zipcode = driver.find_element_by_xpath('//input[@name="postalCode"]')
            break
        except NoSuchElementException:
            time.sleep(0.1)
    send_info_zipcode.send_keys(maos_dic["zip code"])


    #City send function
    link = None
    while not link:
        try:
            send_info_loc = driver.find_element_by_xpath("//input[@name='town']")
            break
        except NoSuchElementException:
            time.sleep(0.1)
    send_info_loc.send_keys(maos_dic["city"])

    #City Function
    link = None
    while not link:
        try:
            send_info_loc = driver.find_element_by_xpath("//option[text()='Georgia']")
            break
        except NoSuchElementException:
            time.sleep(0.1)
    send_info_loc.click()

    #Save and Continue
    link = None
    while not link:
        try:
            save_1 = driver.find_element_by_xpath('//button[text()="Save & Continue"]')
            break
        except NoSuchElementExcception:
            time.sleep(0.1)
    save_1.click()
    
    







buy_shoe()














    
