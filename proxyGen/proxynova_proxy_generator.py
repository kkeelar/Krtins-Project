import os
import random

from selenium.webdriver.common.proxy import Proxy, ProxyType

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


f1 = 'proxynova_proxies.txt'
f2 = 'proxynova_ports.txt'

def proxy_ret():
    ChromeDriverManager().install()
    url = 'https://www.proxynova.com/proxy-server-list'
    options = webdriver.ChromeOptions()
    options.add_argument("no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=800,600")
    options.add_argument("--disable-dev-shm-usage")
    
    capabilities = options.to_capabilities()

    ser = Service(r"C:\Users\kkeel\webdrivers\chromedriver.exe")
    op = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=ser, options=op)
    driver.get(url)    
    page1 = driver.page_source

    proxies = []
    ports = []
    
    for x in range (1, 13):
        text = driver.find_element_by_xpath(' //*[@id="tbl_proxy_list"]/tbody[1]/tr[%d]/td[1]/abbr' % x).text
        proxies.append(text)

    for x in range (14, 37):
        text = driver.find_element_by_xpath(' //*[@id="tbl_proxy_list"]/tbody[1]/tr[%d]/td[1]/abbr' % x).text
        proxies.append(text)

    for x in range (1, 13):
        text1 = driver.find_element_by_xpath('//*[@id="tbl_proxy_list"]/tbody[1]/tr[%d]/td[2]' % x).text
        ports.append(text1)

    for x in range (14, 37):
        text1 = driver.find_element_by_xpath('//*[@id="tbl_proxy_list"]/tbody[1]/tr[%d]/td[2]' % x).text
        ports.append(text1)

    
    

    f_1 = open(f1, 'r+')
    f_2 = open(f2, 'r+')


    f_1.truncate()
    f_2.truncate()


    f_1 = open(f1, 'w')
    f_2 = open(f2, 'w')
    
    
    for x in (proxies):
        f_1.write(x)
        f_1.write('\n')

    for x in (ports):
        f_2.write(x)
        f_2.write('\n')

        

        
proxy_ret()
