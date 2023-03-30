import os
import random

from fp.fp import FreeProxy

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



maos_dic = {
    "fullname": "Michael Mao",
    "f_name": "Michael",
    "l_name": "Mao",
    "email": "kkeelar@gmail.com",
    "phone": 4704135954,
    "address": "9425 Prestwick Club Drive",
    "zip code": 30097,
    "city": "Duluth",
}
    
    




def buy_shoe():

    url = 'https://www.footlocker.com/product/~/Q5397101.html'
    #PROXY = "20.47.108.204:8888"
    options = webdriver.ChromeOptions()
    options.add_argument("no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=800,600")
    options.add_argument("--disable-dev-shm-usage")
    #options.add_argument('--proxy-server=35.245.80.206:80')
    #options.add_argument('--proxy-server=%s' % PROXY)
    driver = webdriver.Chrome(options=options, executable_path=r'C:\Users\kkeel\webdrivers\chromedriver.exe')
    driver.get(url)    
    driver.maximize_window()
    

    #Shoe Size
    link = None
    while not link:
        try:
            button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//button[@aria-label="Size: 07.5"]')))
            driver.execute_script("arguments[0].click();", button)
            print ("STEP 1 DONE")
            break
        except NoSuchElementException:
            time.sleep(0.1)

    time.sleep(1)
    
    #Add To Cart
    link = None
    while not link:
        try:
            add_to_cart = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="ProductDetails"]/ul/li[2]/button')))
            driver.execute_script("arguments[0].click();", add_to_cart)
            print ("STEP 2 DONE")
            break
        except NoSuchElementException:
            time.sleep(0.1)



    # Check if captcha asked #
    time.sleep(1)

    check = driver.find_elements_by_xpath('//*[@id="modalCaptchaDisplayHeading"]')
    if (len(check) == 1):

        print ("CAPTCHA FOUND")

        #Solve Captcha

        #Click I am not a robot
        driver.switch_to.default_content()
        link = None
        while not link:
            try:
                WebDriverWait(driver, 200).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@title='Captcha Entry']")))
                WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@title='reCAPTCHA']")))
                WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="recaptcha-anchor"]/div[1]'))).click()
                print ("CAPTCHA STEP 1 DONE")
                break
            except NoSuchElementException:
                time.sleep(0.1)

        #Click Hearing Challenge
        driver.switch_to.default_content()
        link = None
        while not link:
            try:
                WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@title='Captcha Entry']")))
                WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@title='recaptcha challenge']")))
                WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//button[@title="Get an audio challenge"]'))).click()
                print ("CAPTCHA STEP 2 DONE")
                break
            except NoSuchElementException:
                time.sleep(0.1)

        #Click Play button
        driver.switch_to.default_content()
        link = None
        while not link:
            try:
                WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@title='Captcha Entry']")))
                WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@title='recaptcha challenge']")))
                WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//button[text()="PLAY"]'))).click()
                print ("CAPTCHA STEP 3 DONE")
                break
            except NoSuchElementException:
                time.sleep(0.1)
        src = driver.find_element_by_id("audio-source").get_attribute("src")
        urllib.request.urlretrieve(src, os.getcwd()+"//sample.mp3")
        sound = AudioSegment.from_mp3("sample.mp3")
        sound.export("sample.wav", format="wav")
        sample_audio = sr.AudioFile("sample.wav")
        r = sr.Recognizer()
        with sample_audio as source:
            r.adjust_for_ambient_noise(source)
            sample_audio = r.record(source)
        key = r.recognize_google(sample_audio, language='en-US')
        driver.find_element_by_id("audio-response").send_keys(key.lower())
        driver.find_element_by_id("audio-response").send_keys(Keys.ENTER)
        driver.switch_to.default_content()
        driver.find_element_by_id("recaptcha-demo-submit").click()
        print ("CAPTCHA STEP 4 DONE")

        # Clicks verify #
        link = None
        while not link:
            try:
                driver.switch_to.default_content()
                WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@title='Captcha Entry']")))
                WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@title='recaptcha challenge']")))
                WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//button[text()="Verify"]'))).click()
                print ("CAPTCHA ALL DONE")
            except NoSuchElementException:
                time.sleep(0.1)




    # Clicks View Cart #
    link = None
    while not link:
        try:
            view_cart = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//a[text()="View Cart"]')))
            driver.execute_script("arguments[0].click();", view_cart)
            print ("VIEW CART DONE")
            break
        except NoSuchElementException:
            time.sleep(0.1)
            
    # Clicks Guest Checkout #
    link = None
    while not link:
        try:
            guest_checkout = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//a[text()="Guest Checkout"]')))
            driver.execute_script("arguments[0].click();", guest_checkout)
            print ("GUEST CHECKOUT DONE")
            break
        except NoSuchElementException:
            time.sleep(0.1)

    
    # First Name Function #
    link = None
    while not link:
        try:
            send_info_fname = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,'//input[@name="firstName"]')))
            break
        except NoSuchElementException:
            time.sleep(0.1)
    send_info_fname.send_keys(maos_dic["f_name"])
    print ("SENT FIRST NAME DONE")

    # Last Name Function #
    link = None
    while not link:
        try:
            send_info_lname = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,'//input[@name="lastName"]')))
            break
        except NoSuchElementException:
            time.sleep(0.1)
    send_info_lname.send_keys(maos_dic["l_name"])
    print ("LAST FIRST NAME DONE")

    # Send Email #
    link = None
    while not link:
        try:
            send_email = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,'//input[@name="email"]')))
            break
        except NoSuchElementException:
            print("waiting")
            time.sleep(0.1)
    send_email.send_keys("kkeelar@gmail.com")
    print ("EMAIL DONE")

    # Phone Function #
    link = None
    while not link:
        try:
            send_info_phone = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,'//input[@name="phone"]')))
            break
        except NoSuchElementExcception:
            time.sleep(0.1)
    send_info_phone.send_keys(maos_dic["phone"])
    print ("PHONE DONE")

    # Save and Continue #
    link = None
    while not link:
        try:
            save = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,'//button[text()="Save & Continue"]')))
            driver.execute_script("arguments[0].click();", save)
            print ("SAVE AND CONTINUE DONE")
            break
        except NoSuchElementExcception:
            time.sleep(0.1)
    
    # Send Address #
    link = None
    while not link:
        try:
            send_info_add = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,'//*[@id="ShippingAddress_text_line1"]')))
            break
        except NoSuchElementExcception:
            time.sleep(0.1)
    send_info_add.send_keys(maos_dic["address"])
    print ("ADDRESS DONE")

    
    # Zip code Function #
    link = None
    while not link:
        try:
            send_info_zipcode = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,'//*[@id="ShippingAddress_text_postalCode"]')))
            break
        except NoSuchElementException:
            time.sleep(0.1)
    send_info_zipcode.send_keys(maos_dic["zip code"])
    print ("ZIP CODE DONE")


    # City send function #
    link = None
    while not link:
        try:
            send_info_loc = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,'//*[@id="ShippingAddress_text_town"]')))
            break
        except NoSuchElementException:
            time.sleep(0.1)
    send_info_loc.send_keys(maos_dic["city"])
    print ("CITY DONE")

    time.sleep(1)

    # State Function #
    link = None
    while not link:
        try:
            send_info_loc = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,'//*[@id="ShippingAddress_select_region"]/option[13]')))
            driver.execute_script("arguments[0].click();", send_info_loc)
            print ("STATE DONE")
            break
        except NoSuchElementException:
            time.sleep(0.1)
    
    # Save and Continue #
    link = None
    while not link:
        try:
            secnd_save_cont = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="step2"]/div[2]/div[2]/button')))
            driver.execute_script("arguments[0].click();", secnd_save_cont)
            print ("SAVE AND CONTINUE 2nd DONE")
            break
        except NoSuchElementExcception:
            time.sleep(0.1)

    # Credit Card Function #
    driver.switch_to.default_content()
    link = None
    while not link:
        try:
            WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'//*[@id="adyenContainer"]/div/div[1]/div[1]/span/iframe')))
            send_info_cc = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='encryptedCardNumber']")))
            break
        except NoSuchElementException:
            time.sleep(0.5)
    send_info_cc.send_keys("1234")
    send_info_cc.send_keys("5678")
    send_info_cc.send_keys("9123")
    send_info_cc.send_keys("4567")
    print ("CREDIT CARD DONE")

    
    # Send month Function #
    driver.switch_to.default_content()
    link = None
    while not link:
        try:
            WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'//*[@id="adyenContainer"]/div/div[1]/div[2]/div[1]/span/iframe')))                                                                                       
            send_info_cc_month = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='encryptedExpiryMonth']")))
            break
        except NoSuchElementException:
            time.sleep(0.5)
    send_info_cc_month.send_keys("0")
    send_info_cc_month.send_keys("1")
    print ("CREDIT CARD MONTH DONE")

    # Send year Function #
    driver.switch_to.default_content()
    link = None
    while not link:
        try:
            WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'//*[@id="adyenContainer"]/div/div[1]/div[2]/div[2]/span/iframe')))
            send_info_cc_year = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='encryptedExpiryYear']")))
            break
        except NoSuchElementException:
            time.sleep(0.5)
    send_info_cc_year.send_keys("2")
    send_info_cc_year.send_keys("2")
    print ("CREDIT CARD YEAR DONE")

    # Send CVV function #
    time.sleep(1)
    driver.switch_to.default_content()
    link = None
    while not link:
        try:
            WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'//*[@id="adyenContainer"]/div/div[1]/div[2]/div[3]/span/iframe')))
            send_info_cc_ccv = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="encryptedSecurityCode"]')))
            break
        except NoSuchElementException:
            time.sleep(0.5)
    send_info_cc_ccv.send_keys("1234")
    print ("CREDIT CARD CVV DONE")


    # Save and Continue #
    link = None
    while not link:
        try:
            finish_order = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//button[text()="Place Order"]')))
            driver.execute_script("arguments[0].click();", finish_order)
            break
        except NoSuchElementExcception:
            time.sleep(0.1)


buy_shoe()
