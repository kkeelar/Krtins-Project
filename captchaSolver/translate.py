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




def translate():


    sound = AudioSegment.from_mp3("s_audio_2.mp3")
    
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

    print (key)


translate()
