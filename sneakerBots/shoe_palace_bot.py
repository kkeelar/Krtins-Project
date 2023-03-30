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

url = 'https://www.shoepalace.com/collections/launches/products/air-jordan-6-retro-electric-green-mens-lifestyle-shoe-black-green-limit-one-per-customer?variant=39636556710094&ranMID=42094&ranEAID=UaHsEw9e5Q8&ranSiteID=UaHsEw9e5Q8-_aDefAIGynYZ4XsJclOpEg'

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

    
    #print (soup.prettify())

##    #Close pop up func
##    link = None
##    while not link:
##        try:
##            print ("step 1")
##            close_pop_up = driver.find_element_by_xpath('//button[@class="closeButtonWhite lastFocusableElement"]')
##            break
##        except NoSuchElementException:
##            time.sleep(0.1)
##    close_pop_up.click()


    #Shoe Options Function
    link = None
    while not link:
        try:
            print("step 2")
            shoe_options = driver.find_element_by_xpath('//div[@data-value="8.5"]')
            break
        except NoSuchElementException:
            time.sleep(0.1)
    shoe_options.click()

##    #Close pop up func
##    link = None
##    while not link:
##        try:
##            print ("step 1")
##            close_pop_up = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//button[@class="closeButtonWhite lastFocusableElement"]')))
##            break
##        except NoSuchElementException:
##            time.sleep(0.1)
##    close_pop_up.click()


    


    #Add to Cart Function
    link = None
    while not link:
        try:
            add_to_cart = driver.find_element_by_xpath('//button[@class="ffg productForm-submit js-productForm-submit"]')
            break
        except NoSuchElementException:
            time.sleep(0.1)
    add_to_cart.click()

    
    #Continue to Checkout Function
    link = None
    while not link:
        try:
            continue_to_checkout = driver.find_element_by_xpath('//button[@class="button cart-checkout"]')
            break
        except NoSuchElementException:
            time.sleep(0.1)
    continue_to_checkout.click()


    #Email Function
    link = None
    while not link:
        try:
            send_info_email = driver.find_element_by_xpath('//input[@placeholder="Email"]')
            break
        except NoSuchElementException:
            time.sleep(0.1)
    send_info_email.send_keys(maos_dic["email"])

    #First Name Function
    link = None
    while not link:
        try:
            send_info_fname = driver.find_element_by_xpath('//input[@placeholder="First name"]')
            break
        except NoSuchElementException:
            time.sleep(0.1)
    send_info_fname.send_keys(maos_dic["f_name"])


    time.sleep(1)

    #Last Name Function
    link = None
    while not link:
        try:
            send_info_lname = driver.find_element_by_xpath('//input[@placeholder="Last name"]')
            break
        except NoSuchElementException:
            time.sleep(0.1)
    send_info_lname.send_keys(maos_dic["l_name"])
    
    #Address Function
    link = None
    while not link:
        try:
            send_info_address = driver.find_element_by_xpath('//input[@placeholder="Address"]')
            break
        except NoSuchElementExcception:
            time.sleep(0.1)
    send_info_address.send_keys(maos_dic["address"])

    #City Function
    link = None
    while not link:
        try:
            send_info_city = driver.find_element_by_xpath('//input[@placeholder="City"]')
            break
        except NoSuchElementException:
            time.sleep(0.1)
    send_info_city.send_keys(maos_dic["city"])

    #Zip code Function
    link = None
    while not link:
        try:
            send_info_zipcode = driver.find_element_by_xpath('//input[@placeholder="ZIP code"]')
            break
        except NoSuchElementException:
            time.sleep(0.1)
    send_info_zipcode.send_keys(maos_dic["zip code"])

    #Phone Function
    link = None
    while not link:
        try:                    
            send_info_phone_number = driver.find_element_by_xpath('//input[@placeholder="Phone"]')
            break
        except NoSuchElementException:
            time.sleep(0.1)
    send_info_phone_number.send_keys(maos_dic["phone"])

    #Shipping Function
    link = None
    while not link:
        try:
            continue_to_shipping = driver.find_element_by_xpath('//button[@class="step__footer__continue-btn btn"]')
            break
        except NoSuchElementException:
            time.sleep(0.1)
    continue_to_shipping.click()

    #Continue to Payment Function
    link = None
    while not link:
        try:
            continue_to_payment = driver.find_element_by_xpath('//button[@class="step__footer__continue-btn btn"]')
            break
        except NoSuchElementException:
            time.sleep(0.1)
    continue_to_payment.click()

    #Credit Card Function
    link = None
    while not link:
        try:
            print("STEP 0")
            WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@class='card-fields-iframe']")))
            send_info_cc = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='number' and @id='number']")))
            break
        except NoSuchElementException:
            print ("waiting")
            time.sleep(0.5)
    send_info_cc.send_keys("1234")
    send_info_cc.send_keys("5678")
    send_info_cc.send_keys("9123")
    send_info_cc.send_keys("4567")

    driver.switch_to.default_content()
    #Send Name Function
    link = None
    while not link:
        try:
            frames = WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@title='Field container for: Name on card']")))
            #driver.switch_to.frame(frames[1])
            print ("Done switching back")
            send_info_cc_name = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Name on card']")))
            print ("Done locating")
            break
        except NoSuchElementException:
            print ("waiting")
            time.sleep(0.5)
    send_info_cc_name.send_keys("Michael Mao")

    #Send Date Function
    driver.switch_to.default_content()
    link = None
    while not link:
        try:
            frames = WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@title='Field container for: Expiration date (MM / YY)']")))
            #driver.switch_to.frame(frames[1])
            print ("Done switching back")
            send_info_cc_date = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Expiration date (MM / YY)']")))
            print ("Done locating")
            break
        except NoSuchElementException:
            print ("waiting")
            time.sleep(0.5)
    send_info_cc_date.send_keys("1")
    send_info_cc_date.send_keys("2")
    send_info_cc_date.send_keys("3")
    send_info_cc_date.send_keys("4")


    #Send CVV function
    driver.switch_to.default_content()
    link = None
    while not link:
        try:
            frames = WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@title='Field container for: Security code']")))
            #driver.switch_to.frame(frames[1])
            print ("Done switching back")
            send_info_cc_ccv = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Security code']")))
            print ("Done locating")
            break
        except NoSuchElementException:
            print ("waiting")
            time.sleep(0.5)

    

    send_info_cc_ccv.send_keys("1234")


buy_shoe()
