import os
import random


from fp.fp import FreeProxy

from selenium.webdriver.common.proxy import Proxy, ProxyType

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

f1 = 'proxynova_proxies.txt'
f2 = 'proxynova_ports.txt'

def proxy_ret():


    even = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,100]
    usable_proxies = []
    usable_proxies1 = []

    usable_ports = []
    usable_ports1 = []

    f_1 = open(f1)
    proxies = f_1.readlines()
    for x in proxies:
        usable_proxies.append(x)

    for x in range(len(usable_proxies)):
        usable_proxies1.append(usable_proxies[x].strip('\n'))

 

    f_2 = open(f2)
    ports = f_2.readlines()
    for x in ports:
        usable_ports.append(x)

    for x in range(len(usable_ports)):
        usable_ports1.append(usable_ports[x].strip('\n'))

    final_proxies = []
  
    for x in range(len(usable_proxies1)):
        y = (usable_proxies1[x] + ":" + usable_ports1[x])
        final_proxies.append(y)



    print (final_proxies)
  
    

    for x in (even):
        for y in (final_proxies):
                
            url = 'https://b-ok.cc/s/Medical%20Textbooks'
            options = webdriver.ChromeOptions()
            options.add_argument("no-sandbox")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=800,600")
            options.add_argument("--disable-dev-shm-usage")
            e = (str(y))
            print (e)
            options.add_argument('--proxy-server=http://45.65.225.161:8080')
            capabilities = options.to_capabilities()
            driver = webdriver.Chrome(options=options, executable_path=r'C:\Users\kkeel\webdrivers\chromedriver.exe')
            driver.get(url)    
            page1 = driver.page_source
            soup = bs4.BeautifulSoup(page1, "lxml")
            table = soup.find('div', attrs = {'id':'__init__'})
            
            book_click = driver.find_element_by_xpath('//*[@id="searchResultBox"]/div[%d]/div/table/tbody/tr/td[2]/table/tbody/tr[1]/td/h3/a' % x).click()
            try:
                download_pdf = driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/div/div/div/div[2]/div[2]/div[1]/div[1]/div/a').click()
            except NoSuchElementException:
                print('no download')

            print (x)

            time.sleep(1)

            try:
                book_title = driver.find_element_by_xpath('//h1[@itemprop="name"]').text
                print (book_title)
            except NoSuchElementException:
                print ('no title')
                

            
            time.sleep(1)
            try:
                book_description = driver.find_element_by_xpath('//*[@id="bookDescriptionBox"]').text
                print (book_description)
            except NoSuchElementException:
                
                print ('no description')
                
            
            time.sleep(1)    
            try:
                publisher = driver.find_element_by_xpath('//div[@class="bookProperty property_publisher"]').text
                print (publisher)
            except NoSuchElementException:
                print ('no publisher')
            
            time.sleep(1)
            try:
                year = driver.find_element_by_xpath('//div[@class="bookProperty property_year"]').text
                #print (year)
            except NoSuchElementException:
                print ('no year')
            
            time.sleep(1)
            try:
                book_edition = driver.find_element_by_xpath('//div[@class="bookProperty property_edition"]').text
                #print (book_edition)
            except NoSuchElementException:
                print ('no book edition')
            
            
            
            time.sleep(1)
            try:
                categories = driver.find_element_by_xpath('//div[@class="bookProperty property_categories_new"]').text
                print (categories)
            except NoSuchElementException:
                print ('no categories')



            driver.quit()
            
        
    
##    for x in range (1, 13):
##        text = driver.find_element_by_xpath(' //*[@id="tbl_proxy_list"]/tbody[1]/tr[%d]/td[1]/abbr' % x).text
##        proxies.append(text)
##
##    for x in range (14, 37):
##        text = driver.find_element_by_xpath(' //*[@id="tbl_proxy_list"]/tbody[1]/tr[%d]/td[1]/abbr' % x).text
##        proxies.append(text)
##
##    for x in range (1, 13):
##        text1 = driver.find_element_by_xpath('//*[@id="tbl_proxy_list"]/tbody[1]/tr[%d]/td[2]' % x).text
##        ports.append(text1)
##
##    for x in range (14, 37):
##        text1 = driver.find_element_by_xpath('//*[@id="tbl_proxy_list"]/tbody[1]/tr[%d]/td[2]' % x).text
##        ports.append(text1)
##
##    for x in range (1, 13):
##        text2 = driver.find_element_by_xpath('//*[@id="tbl_proxy_list"]/tbody[1]/tr[%d]/td[4]/small' % x).text
##        proxy_speed.append(text2)
##
##    for x in range (14, 37):
##        text2 = driver.find_element_by_xpath('//*[@id="tbl_proxy_list"]/tbody[1]/tr[%d]/td[4]/small' % x).text
##        proxy_speed.append(text2)
##
##    for x in range (1, 13):
##        text3 = driver.find_element_by_xpath('//*[@id="tbl_proxy_list"]/tbody[1]/tr[%d]/td[5]/span[1]' % x).text
##        up_time.append(text3)
##
##    for x in range (14, 37):
##        text3 = driver.find_element_by_xpath('//*[@id="tbl_proxy_list"]/tbody[1]/tr[%d]/td[5]/span[1]' % x).text
##        up_time.append(text3)
##
##    for x in range (1, 13):
##        text4 = driver.find_element_by_xpath('//*[@id="tbl_proxy_list"]/tbody[1]/tr[%d]/td[6]/a' % x).text
##        country.append(text4)
##
##    for x in range (14, 37):
##        text4 = driver.find_element_by_xpath('//*[@id="tbl_proxy_list"]/tbody[1]/tr[%d]/td[6]/a' % x).text
##        country.append(text4)
##
##    for x in range (1, 13):
##        text5 = driver.find_element_by_xpath('//*[@id="tbl_proxy_list"]/tbody[1]/tr[%d]/td[7]/span' % x).text
##        anonymity.append(text5)
##
##    for x in range (14, 37):
##        text5 = driver.find_element_by_xpath('//*[@id="tbl_proxy_list"]/tbody[1]/tr[%d]/td[7]/span' % x).text
##        anonymity.append(text5)
##    
##
##    f_1 = open(f1, 'r+')
##    f_2 = open(f2, 'r+')
##    f_3 = open(f3, 'r+')
##    f_4 = open(f4, 'r+')
##    f_5 = open(f5, 'r+')
##    f_6 = open(f6, 'r+')
##
##
##    f_1.truncate()
##    f_2.truncate()
##    f_3.truncate()
##    f_4.truncate()
##    f_5.truncate()
##    f_6.truncate()
##
##
##    f_1 = open(f1, 'w')
##    f_2 = open(f2, 'w')
##    f_3 = open(f3, 'w')
##    f_4 = open(f4, 'w')
##    f_5 = open(f5, 'w')
##    f_6 = open(f6, 'w')
##    
##    
##    for x in (proxies):
##        f_1.write(x)
##        f_1.write('\n')
##
##    for x in (ports):
##        f_2.write(x)
##        f_2.write('\n')
##
##    for x in (proxy_speed):
##        f_3.write(x)
##        f_3.write('\n')
##
##    for x in (up_time):
##        f_4.write(x)
##        f_4.write('\n')
##
##    for x in (country):
##        f_5.write(x)
##        f_5.write('\n')
##
##    for x in (anonymity):
##        f_6.write(x)
##        f_6.write('\n')

        
proxy_ret()
