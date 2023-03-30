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

url = 'https://www.footaction.com/product/nike-air-tailwind-79-mens/87754012.html'

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



##    #Kill Ad
##    for x in range (0, 25):
##        try:
##            print("step 1")
##            kill_ad = driver.find_element_by_xpath('//button[@class="closeButtonRed lastFocusableElement"]').click()
##            break
##        except NoSuchElementException:
##            print("Waiting")
##            time.sleep(1)
##    print("done killing ad")

   
    #Shoe Size
    link = None
    while not link:
        try:
            button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//span[text()="11.0"]')))
            driver.execute_script("arguments[0].click();", button)
            break
        except NoSuchElementException:
            time.sleep(0.1)

    #Add To Cart
    link = None
    while not link:
        try:
            add_to_cart = driver.find_element_by_xpath('//button[@class="Button ProductDetails-form__action"]')
            driver.execute_script("arguments[0].click();", add_to_cart)
            break
        except NoSuchElementException:
            time.sleep(0.1)
            



    #Solve Captcha

    #Click I am not a robot
    driver.switch_to.default_content()
    link = None
    while not link:
        try:
            WebDriverWait(driver, 200).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@title='Captcha Entry']")))
            WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@title='reCAPTCHA']")))
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//div[@class="recaptcha-checkbox-border"]'))).click()
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
            break
        except NoSuchElementException:
            time.sleep(0.1)
    src = driver.find_element_by_id("audio-source").get_attribute("src")
    print (src)
    print ("os. cwd", os.getcwd())
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
    link = None
    while not link:
        try:
            driver.switch_to.default_content()
            WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@title='Captcha Entry']")))
            WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@title='recaptcha challenge']")))
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//button[text()="Verify"]'))).click()
        except NoSuchElementException:
            time.sleep(0.1)



    #View Cart
    link = None
    while not link:
        try:
            view_cart = driver.find_element_by_xpath('//a[text()="View Cart"]')
            driver.execute_script("arguments[0].click();", view_cart)
            break
        except NoSuchElementException:
            time.sleep(0.1)
            
    #Guest Checkout
    link = None
    while not link:
        try:
            guest_checkout = driver.find_element_by_xpath('//a[text()="Guest Checkout"]')
            driver.execute_script("arguments[0].click();", guest_checkout)
            break
        except NoSuchElementException:
            time.sleep(0.1)

    
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
    send_info_phone.send_keys(maos_dic["phone"])

    #Save and Continue
    link = None
    while not link:
        try:
            save = driver.find_element_by_xpath('//button[text()="Save & Continue"]')
            driver.execute_script("arguments[0].click();", save)
            break
        except NoSuchElementExcception:
            time.sleep(0.1)
    
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

    time.sleep(0.75)
    #City Function
    link = None
    while not link:
        try:
            send_info_loc = driver.find_element_by_xpath("//option[text()='Georgia']")
            driver.execute_script("arguments[0].click();", send_info_loc)
            break
        except NoSuchElementException:
            time.sleep(0.1)
    
    time.sleep(0.71)
    #Save and Continue
    link = None
    while not link:
        try:
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//button[text()="Save & Continue"]'))).click()
            break
        except NoSuchElementExcception:
            time.sleep(0.1)

    #Credit Card Function
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

    
    #Send month Function
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

    #Send year Function
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

    #Send CVV function
    time.sleep(2)
    driver.switch_to.default_content()
    link = None
    while not link:
        try:
            WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'//*[@id="adyenContainer"]/div/div[1]/div[2]/div[3]/span/iframe')))
            send_info_cc = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='encryptedSecurityCode']")))
            break
        except NoSuchElementException:
            time.sleep(0.5)
    send_info_cc_ccv.send_keys("1234")


    #Save and Continue
    link = None
    while not link:
        try:
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//button[text()="Place Order"]'))).click()
            break
        except NoSuchElementExcception:
            time.sleep(0.1)
    

    

buy_shoe()
