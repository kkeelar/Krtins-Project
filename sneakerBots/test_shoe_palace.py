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

url = 'https://www.shoepalace.com/checkpoint'





def test_captcha():
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

    #Solve Captcha

    #Click I am not a robot
    driver.switch_to.default_content()
    link = None
    while not link:
        try:
            
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


    print("STEP 1")
    urllib.request.urlretrieve(src, os.getcwd()+"//sample.mp3")
    print("STEP 2")
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
            print ("done switching in")
            WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@title='recaptcha challenge']")))
            print("done")
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//button[text()="Verify"]'))).click()
        except NoSuchElementException:
            print ("Waiting to find hearing button")
            time.sleep(0.1)


    print ("done locating")



    
test_captcha()
