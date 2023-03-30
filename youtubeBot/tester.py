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

import random
       

def finder():


        with  open ('made_accounts.txt') as f1:
            lines = []

            for line in f1:
                lines.append(line)

        url = 'https://fantasy.espn.com/tournament-challenge-bracket/2022/en/game'

    
        # Set OPTS for the driver #
        options = webdriver.ChromeOptions()
        options.add_argument("no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=800,600")
        options.add_argument("--disable-dev-shm-usage")    
        driver = webdriver.Chrome(options=options, executable_path=r'C:\Users\kkeel\webdrivers\chromedriver.exe')
        driver.get(url)    
        
        driver.maximize_window()


        driver.refresh()

        time.sleep(3)

        # Clicks login #
        link = None
        while not link:
            try:
                driver.switch_to.default_content()
                log_in = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="global-header"]/div[2]/ul/li[2]/a')))
                driver.execute_script("arguments[0].click();", log_in)    
                break
            except NoSuchElementException:
                time.sleep(0.1)


        time.sleep(1)

        # Email #
        #changer = 0
        link = None
        while not link:
            try:
                driver.switch_to.default_content()
                WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'//*[@id="disneyid-iframe"]')))
                email = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="did-ui-view"]/div/section/section/form/section/div[1]/div/label/span[2]/input')))
                changer = 0
                email.send_keys(lines[index+changer])
                print (lines[index+changer])
                time.sleep(3)
                driver.switch_to.default_content()
                WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'//*[@id="disneyid-iframe"]')))

                time.sleep(1)
                
                # Puts in password #
                driver.switch_to.default_content()
                WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'//*[@id="disneyid-iframe"]')))
                password = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="did-ui-view"]/div/section/section/form/section/div[2]/div/label/span[2]/input')))
                password.send_keys('Th3f!ash')

                time.sleep(1)
                
                # Clicks log in #
                driver.switch_to.default_content()
                WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'//*[@id="disneyid-iframe"]')))
                log_in = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="did-ui-view"]/div/section/section/form/section/div[3]/button')))
                driver.execute_script("arguments[0].click();", log_in)    
                

                # Checks if account worked #
                check = driver.find_elements_by_xpath('//*[@id="did-ui-view"]/div/section/div/div/div')
                while (len(check) == 1):
                    
                    changer = changer + 1
                    print ("Found error")
                    email.send_keys(Keys.CONTROL, 'a')
                    email.send_keys(Keys.BACKSPACE)
                    email.send_keys(lines[index+changer])
                    print (lines[index+changer])
                    time.sleep(3)

                    # Clicks log in again #
                    driver.switch_to.default_content()
                    WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'//*[@id="disneyid-iframe"]')))
                    log_in = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="global-header"]/div[2]/ul/li[2]/a')))
                    driver.execute_script("arguments[0].click();", log_in)

                    time.sleep(3)
                    check = driver.find_elements_by_xpath('//*[@id="notification-create-error-email"]/div/div')

                print ("this email has an account")
                real_accounts = []
                real_accounts.append(lines[index+changer])
                print (len(real_accounts))

                break
            except NoSuchElementException:
                time.sleep(0.1)

        time.sleep(3)
        # Finds points #
        num_of_brackets = driver.find_elements_by_xpath('//a[@class="entry-details-entryname"]')

        points_list = []
        print (len(num_of_brackets))
        odd = 1
        for x in range(len(num_of_brackets)):
                driver.switch_to.default_content()
                points = driver.find_elements_by_xpath('//*[@id="main-container"]/div[1]/section[1]/div/div/section/table/tbody/tr[%d]/td[5]' % odd).text
                points_list.append(points)
                odd = odd + 2                     
                break
        
        time.sleep(1)
        
        pct_list = []
        odd_1 = 1
        for x in range(len(num_of_brackets)):
                driver.switch_to.default_content()
                pct = driver.find_elements_by_xpath('/html/body/div[5]/section/section/div[1]/section[1]/div/div/section/table/tbody/tr[%d]/td[6]' % odd_1).tex                       
                pct_list.append(pct)
                odd_1 = odd_1 + 2                     
                break
        
        time.sleep(1)
        
       
        max_list = []
        odd_3 = 1
        for x in range(len(num_of_brackets)):
                driver.switch_to.default_content()
                max_txt = driver.find_elements_by_xpath('/html/body/div[5]/section/section/div[1]/section[1]/div/div/section/table/tbody/tr[1]/td[7]' % odd_3).tex                       
                max_list.append(max_txt)
                odd_3 = odd_3 + 2                     
                break
        
        time.sleep(1)


        for x in range(len(num_of_brackets)):
            print ("Points: ", points_list[x], "PERCENTAGE: ", pct_list[x], "Max Score: ", max_list[x])

 
        



finder()


