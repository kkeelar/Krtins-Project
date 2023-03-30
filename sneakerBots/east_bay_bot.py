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

url = 'https://www.eastbay.com/product/new-balance-4040v5-tpu-mid-mens/PM4040K5.html'

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




    

    #Shoe Size
    link = None
    while not link:
        try:
            print("step 2")
            shoe_size = driver.find_element_by_xpath('//span[text()="10.5"]')
            driver.execute_script("arguments[0].click();", shoe_size)
            break
        except NoSuchElementException:
            print("waiting")
            time.sleep(0.1)
    


    #Add To Cart
    link = None
    while not link:
        try:
            print ("step 3")
            add_to_cart = driver.find_element_by_xpath('//button[@class="Button Button ProductDetails-form__action"]')
            driver.execute_script("arguments[0].click();", add_to_cart)
            break
        except NoSuchElementException:
            print("waiting")
            time.sleep(0.1)
    

    #Solve Captcha

    #Click I am not a robot
    driver.switch_to.default_content()
    link = None
    while not link:
        try:
            print ("step 4")
            WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@title='Captcha Entry']")))
            print ("done switching in")
            WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@title='reCAPTCHA']")))
            print("done")
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//div[@class="recaptcha-checkbox-border"]'))).click()
            break
        except NoSuchElementException:
            print ("loading")
            time.sleep(0.1)
    print ("done with clicking I am not a robot")

    #Click Hearing Challenge
    driver.switch_to.default_content()
    link = None
    while not link:
        try:
            print ("step 5")
            WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@title='Captcha Entry']")))
            print ("done switching in")
            WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@title='recaptcha challenge']")))
            print("done")
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//button[@title="Get an audio challenge"]'))).click()
            break
        except NoSuchElementException:
            print ("loading")
            time.sleep(0.1)
    print ("done with audio button click")


    #Click Play button
    driver.switch_to.default_content()
    link = None
    while not link:
        try:
            print ("step 6")
            WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@title='Captcha Entry']")))
            print ("done switching in")
            WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@title='recaptcha challenge']")))
            print("done")
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//button[text()="PLAY"]'))).click()
            break
        except NoSuchElementException:
            print ("loading")
            time.sleep(0.1)
    print ("done play button")




    src = driver.find_element_by_id("audio-source").get_attribute("src")
    print (src)
    print ("os. cwd", os.getcwd())

    time.sleep(5)
    print("STEP 1")
    urllib.request.urlretrieve(src, os.getcwd()+"//sample.mp3")
    print("STEP 2")
    #AudioSegment.ffmpeg = "C:/Users/kkeel/AppData/Local/Programs/Python/Python39/Lib/site-packages"
    #sound = pydub.AudioSegment.from_mp3(os.getcwd()+"\sample.mp3", format="mp3")
    sound = AudioSegment.from_mp3("sample.mp3")
    
    print("STEP 3")
    sound.export("sample.wav", format="wav")
    print("STEP 4")
    sample_audio = sr.AudioFile("sample.wav")
    print("STEP 5")

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
            print ("step 6")
            WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@title='Captcha Entry']")))
            print ("done switching in")
            WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@title='recaptcha challenge']")))
            print("done")
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//button[text()="Verify"]'))).click()
        except NoSuchElementException:
            print ("Waiting to find hearing button")
            time.sleep(0.1)


    print ("done locating")
    #driver.find_element_by_id("recaptcha-audio-button").click()

    

    

    
    #Continue to Checkout Function
    link = None
    while not link:
        try:
            continue_to_checkout = driver.find_element_by_xpath('//button[@class="btn ajaxcart__checkout"]')
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

    time.sleep(2)
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
    time.sleep(2)
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
    time.sleep(2)
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
