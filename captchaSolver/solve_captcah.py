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


url = 'https://www.google.com/recaptcha/api2/demo'


def solve_captcha():
    def delay():
        time.sleep(2)
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





    link = None
    while not link:
        try:
            frames = driver.find_elements_by_tag_name("iframe")
            driver.switch_to.frame(frames[0])
            driver.find_element_by_class_name("recaptcha-checkbox-border").click()
            break
        except NoSuchElementException:
            time.sleep(0.1)

   


    link = None
    while not link:
        try:
            driver.switch_to.default_content()
            WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//iframe[@title="recaptcha challenge"]')))
            print ("done with stepp 1")            
            driver.find_element_by_xpath('/html/body/div/div/div[3]/div[2]/div[1]/div[1]/div[2]/button').click()
            print ("done with steo 2")
            break
        except NoSuchElementException:
            time.sleep(0.1)

    
  

    link = None
    while not link:
        try:
            driver.switch_to.default_content()
            frames_2 = driver.find_elements_by_tag_name("iframe")
            driver.switch_to.frame(frames_2[-1])
            driver.find_element_by_xpath("/html/body/div/div/div[3]/div/button").click()

            break
        except NoSuchElementException:
            time.sleep(0.1)
    


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
    delay()

    driver.find_element_by_id("recaptcha-demo-submit").click()

##    link = None
##    while not link:
##        try:
##            driver.switch_to.default_content()
##            frames = driver.find_elements_by_tag_name("iframe")
##            driver.switch_to.frame(frames[0])
##        except NoSuchElementException:
##            print ("Waiting to find hearing button")
##            time.sleep(0.1)
##
##
##    print ("done locating")
##    driver.find_element_by_id("recaptcha-audio-button").click()




solve_captcha()
