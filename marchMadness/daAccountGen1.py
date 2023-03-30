import os
import random
from os import path


from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import threading

import random








def billion(emailLine):

        change = 0
        

        with  open ("emailsList.txt") as f1:
            lines = []

            for line in f1:
                lines.append(line)
    
        
    
    
        for emailIndex in (range(len(lines))):

            url = 'https://fantasy.espn.com/tournament-challenge-bracket/2023/en/'

            # Set OPTS for the driver #
            options = webdriver.ChromeOptions()
            options.add_argument("no-sandbox")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=800,600")
            options.add_argument("--disable-dev-shm-usage")
            #options.add_argument("--headless")
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            driver = webdriver.Chrome(options=options, executable_path=r'C:\Users\kkeel\webdrivers\chromedriver.exe')
            time.sleep(1)
            driver.get(url)


            # Clicks create bracket #
            link = None
            while not link:
                try:
                    clickCreateEntry = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/section/section/div[1]/section[1]/div/div[3]/div[1]/a')))
                    time.sleep(3)
                    driver.execute_script("arguments[0].click();", clickCreateEntry)
                    break
                except TimeoutException:
                    time.sleep(0.1)



            # Checks get started #
            link = False
            while (link is False):
                try:
                    checkUsed = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/section/section/div[1]/section[1]/div/div[3]/a')))
                    time.sleep(3)
                    driver.execute_script("arguments[0].click();", checkUsed)
                    break
                except TimeoutException:
                    link = True
        


                                
            time.sleep(1)
            # Clicks sign up #
            link = None
            while not link:
                try:
                    driver.switch_to.default_content()
                    WebDriverWait(driver, 8).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'//*[@id="disneyid-iframe"]')))
                    clickSignUp = WebDriverWait(driver, 8).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="did-ui-view"]/div/section/section/form/section/div[5]/a')))
                    driver.execute_script("arguments[0].click();", clickSignUp)
                    break
                except TimeoutException:
                    time.sleep(0.1)

            time.sleep(1)
            # Inputs first name #
            link = None
            while not link:
                try:
                    driver.switch_to.default_content()
                    WebDriverWait(driver, 5).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'//*[@id="disneyid-iframe"]')))
                    firstName = WebDriverWait(driver, 8).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/section/section/form/section[1]/div[1]/div[1]/label/span[2]/input')))
                    firstName.send_keys('Krtin')
                    break
                except TimeoutException:
                    time.sleep(0.1)

            time.sleep(1)
            # Inputs last name #
            link = None
            while not link:
                try:
                    driver.switch_to.default_content()
                    WebDriverWait(driver, 8).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'//*[@id="disneyid-iframe"]')))
                    lastName = WebDriverWait(driver, 7).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/section/section/form/section[1]/div[1]/div[2]/label/span[2]/input')))
                    lastName.send_keys('Keelar')
                    break
                except TimeoutException:
                    time.sleep(0.1)
            time.sleep(1)    
            def email_kicker(driver, emailIndex):
                    driver.switch_to.default_content()
                    WebDriverWait(driver, 5).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'//*[@id="disneyid-iframe"]')))
                    email = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/section/section/form/section[1]/div[2]/div/label/span[2]/input')))
                    time.sleep(1)
                    email.send_keys(lines[emailIndex+emailLine])
                    time.sleep(1)
                    driver.switch_to.default_content()
                    WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'//*[@id="disneyid-iframe"]')))
                    password = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="did-ui-view"]/div/section/section/form/section[1]/div[4]/div[1]/label/span[2]/input')))
                    time.sleep(1)
                    password.send_keys('cS#qUW865r8D')
                
            email_kicker(driver, emailIndex)
            
            
            time.sleep(1)    
            # Clicks sign up 4real #
            link = None
            while not link:
                try:
                    driver.switch_to.default_content()
                    WebDriverWait(driver, 5).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'//*[@id="disneyid-iframe"]')))
                    clickSignUp4Real = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="did-ui-view"]/div/section/section/form/section[6]/div/button')))
                    driver.execute_script("arguments[0].click();", clickSignUp4Real)
                    break
                except NoSuchElementException:
                    time.sleep(0.1)

            time.sleep(1)
            # Checks if email is taken #
            link = False
            while (link is False):
                try:
                    checkUsed = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="notification-create-error-email"]/div/div')))
                    driver.switch_to.default_content()
                    WebDriverWait(driver, 5).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'//*[@id="disneyid-iframe"]')))
                    emailClearer = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/section/section/form/section[1]/div[2]/div/label/span[2]/input')))
                    emailClearer.clear()
                    emailIndex += 1
                    email_kicker(driver, emailIndex)
                except TimeoutException:
                    link = True

            print (lines[emailIndex+emailLine])

            # Stores working accounts #
            with open('accountsList.txt', 'a') as file:
                file.write((lines[emailIndex+emailLine+change]))
                file.write('\n')

            driver.quit()

            
            change += 1
            print ('account made')

        


t1 = threading.Thread(target=billion, args=(651,))
##t2 = threading.Thread(target=billion, args=(1643,))
##t3 = threading.Thread(target=billion, args=(2643,))
##t4 = threading.Thread(target=billion, args=(3643,))
##t5 = threading.Thread(target=billion, args=(4643,))
##t6 = threading.Thread(target=billion, args=(5643,))
##t7 = threading.Thread(target=billion, args=(6643,))
t1.start()
##t2.start()
##t3.start()
##t4.start()
##t5.start()
##t6.start()
##t7.start()
