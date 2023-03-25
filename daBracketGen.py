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
          
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            driver = webdriver.Chrome(options=options, executable_path=r'C:\Users\kkeel\webdrivers\chromedriver.exe')
            time.sleep(1)
            driver.get(url)

            time.sleep(1)
            # Clicks create New bracket #
            link = None
            while not link:
                try:
                    clickCreateEntry = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/section/section/div[1]/section[1]/div/div[4]/div[1]/a')))
                    time.sleep(1)
                    driver.execute_script("arguments[0].click();", clickCreateEntry)
                    break
                except TimeoutException:
                    time.sleep(0.1)

            time.sleep(1)
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
                    time.sleep(1)
                    driver.switch_to.default_content()
                    WebDriverWait(driver, 5).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'//*[@id="disneyid-iframe"]')))
                    clickSignUp4Real = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="did-ui-view"]/div/section/section/form/section[6]/div/button')))
                    driver.execute_script("arguments[0].click();", clickSignUp4Real)
               
            email_kicker(driver, emailIndex)
           
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

#            print (lines[emailIndex+emailLine])

            # Stores working accounts #
            with open('accountsList.txt', 'a') as file:
                file.write((lines[emailIndex+emailLine+change]))
                file.write('\n')

            change += 1

            time.sleep(1)
            # Clicks Cancel new name #
            link = None
            while not link:
                try:
                    driver.switch_to.default_content()
                    WebDriverWait(driver, 5).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'//*[@id="disneyid-iframe"]')))
                    clickCancel = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="did-ui-view"]/div/section/section/form/section/div[4]/button[2]')))
                    driver.execute_script("arguments[0].click();", clickCancel)
                    break
                except TimeoutException:
                    time.sleep(0.1)
           
            def makingBrackets(driver):
               
                driver.switch_to.default_content()
               
                time.sleep(1)
                # Clicks autofill bracket #
                link = None
                while not link:
                    try:
                        clickAFA = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="bracketForm"]/div[3]/button[1]')))
                        driver.execute_script("arguments[0].click();", clickAFA)
                        break
                    except TimeoutException:
                        time.sleep(0.1)

                time.sleep(1)
                driver.switch_to.default_content()
                # Clicks autofill bracket weighted by seed #
                link = None
                while not link:
                    try:
                        clickAutoFillWeighted = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="importBrackets"]/ul/li[4]/label/div[1]')))
                        time.sleep(3)
                        driver.execute_script("arguments[0].click();", clickAutoFillWeighted)
                        break
                    except TimeoutException:
                        time.sleep(0.1)

               
                time.sleep(1)
                # Clicks "Autofill Brakcet Button" #
                link = None
                while not link:
                    try:
                        clickAutoFill4Real = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="importBrackets"]/div[2]/button')))
                        driver.execute_script("arguments[0].click();", clickAutoFill4Real)
                        break
                    except TimeoutException:
                        time.sleep(0.1)


               
                time.sleep(1)
                # Clicks Submit Pciks #
                link = None
                while not link:
                    try:
                        clickSubmit = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="formSubmit"]')))
                        driver.execute_script("arguments[0].click();", clickSubmit)
                        break
                    except TimeoutException:
                        time.sleep(0.1)

                       
                time.sleep(1)
                # Clicks create another bracket #
                link = None
                while not link:
                    try:
                        clickCAB = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="success"]/div[2]/a')))
                        driver.execute_script("arguments[0].click();", clickCAB)
                        break
                    except TimeoutException:
                        time.sleep(0.1)


            # Makes 25 Brackets #
            for x in range(24):
                makingBrackets(driver)
           

            time.sleep(1)
           # driver.switch_to.default_content()
##            # Clicks create cancelIDK #
##            link = None
##            while not link:
##                try:
##                    clickCancelIDK = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[13]')))
##                    driver.execute_script("arguments[0].click();", clickCancelIDK)
##                    break
##                except TimeoutException:
##                    time.sleep(0.1)
##            
           
            #time.sleep(1)
            def AddToGroups(driver):

                # Clicks creat or join gorup #
                link = None
                while not link:
                    try:
                        clickJoin0 = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="global-nav-secondary"]/div/ul[2]/li[4]/a/span[1]')))
                        driver.execute_script("arguments[0].click();", clickJoin0)
                        break
                    except TimeoutException:
                        time.sleep(0.1)

           
                # Clicks creat or join gorup #
                link = None
                while not link:
                    try:
                        clickJoin1 = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="global-nav-secondary"]/div/ul[2]/li[4]/div/ul/li/a')))
                        driver.execute_script("arguments[0].click();", clickJoin1)
                        break
                    except TimeoutException:
                        time.sleep(0.1)

                time.sleep(1)
                # Searches for LeBillionares #
                link = None
                while not link:
                    try:
                        searchGroup = WebDriverWait(driver, 8).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="search_values"]')))
                        searchGroup.send_keys('LeBillionares')
                        break
                    except TimeoutException:
                        time.sleep(0.1)

                time.sleep(2)
                # Clicks search group #
                link = None
                while not link:
                    try:
                        clickSearch = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="groupFind"]/input')))
                        driver.execute_script("arguments[0].click();", clickSearch)
                        break
                    except TimeoutException:
                        time.sleep(0.1)

                time.sleep(2)
                # Clicks group #
                link = None
                while not link:
                    try:
                        clickGroupIt = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main-container"]/div[1]/section[1]/div[2]/div[3]/div/div[2]/table/tbody/tr[1]/td[1]/a')))
                        driver.execute_script("arguments[0].click();", clickGroupIt)
                        break
                    except TimeoutException:
                        time.sleep(0.1)

                time.sleep(2)
                # Clicks join group actaully #
                link = None
                while not link:
                    try:
                        clickJoin4Real = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="toggle_groupJoin"]')))
                        driver.execute_script("arguments[0].click();", clickJoin4Real)
                        break
                    except TimeoutException:
                        time.sleep(0.1)

                time.sleep(2)
                z = 1
                # Adds all brackets to group #
                for y in range(24):
                   
                    clickAddAll = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main-container"]/div[1]/section[1]/div/div[2]/form/div/table/tbody/tr[%d]/td[3]/label' % z)))
                    driver.execute_script("arguments[0].click();", clickAddAll)
                    z += 2

                #driver.switch_to.default_content()
                time.sleep(2)
                # Enters passwords #
                link = None
                while not link:
                    try:
                        groupPW = WebDriverWait(driver, 8).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main-container"]/div[1]/section[1]/div/div[2]/form/div/table/tbody/tr[49]/td/input[1]')))
                        groupPW.send_keys('Th3f!ashTh3f!ash')
                        break
                    except TimeoutException:
                        time.sleep(0.1)


               
               
                time.sleep(1)
                # Clicks join group actaully again #
                link = None
                while not link:
                    try:
                        clickJoin4Real2 = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main-container"]/div[1]/section[1]/div/div[2]/form/div/table/tbody/tr[49]/td/input[2]')))
                        driver.execute_script("arguments[0].click();", clickJoin4Real2)
                        print ("Joined properly")
                        print(change)
                        break
                    except TimeoutException:
                        time.sleep(0.1)

           
            AddToGroups(driver)
            driver.quit()



   
t1 = threading.Thread(target=billion, args=(0,))
t2 = threading.Thread(target=billion, args=(2000,))

t1.start()
t2.start()
