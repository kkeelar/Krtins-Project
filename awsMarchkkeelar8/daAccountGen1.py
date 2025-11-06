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
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import threading
from selenium.webdriver.common.keys import Keys


import subprocess

from pullCode import main

import random


def get_passcode():
    # Call the pullCode.py script using subprocess and capture its output
    result = subprocess.run(['python', 'pullCode.py'], capture_output=True, text=True)
    passcode = result.stdout.strip()  # Get the passcode from the output
    return passcode


def billion(counter):

        for varb in (range(counter, counter + 10000)):
            
            print ("this is varb + counter: %d " % (varb+counter))

           
            try:


                url = 'https://fantasy.espn.com/games/tournament-challenge-bracket-2024/'

                # Set options for the driver
                C_options = webdriver.ChromeOptions()
                C_options.add_argument("no-sandbox")
                C_options.add_argument("--disable-gpu")
                C_options.add_argument("--window-size=800,600")
                C_options.add_argument("--disable-dev-shm-usage")
                # Set up the proxy server details
                proxy_server = "103.7.26.142"
                proxy_port = "8080"

                # Set up the WebDriver options
                options = webdriver.ChromeOptions()
                #options.add_argument(f'--proxy-server={proxy_server}:{proxy_port}')


                service = Service(executable_path="/Users/krtinkeelar/Desktop/coding projects/da code (account checker)/chromedriver")

                # Initialize the WebDriver with the specified options and executable path
                driver = webdriver.Chrome(options=C_options, service=service)

                time.sleep(1)

                driver.get(url)
            

                time.sleep(2)
                # Clicks first create account
                clickFirstCreateBracket = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                            '//*[@id="fittPageContainer"]/div/div[4]/div[4]/div/div/div[1]/div/div[2]/button')))
                driver.execute_script("arguments[0].click();", clickFirstCreateBracket)
                print ("done click create")

                time.sleep(1)
                # Clicks quick bracket #
                clickQB = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                            '//*[@id="fittPageContainer"]/div/div[5]/div[3]/div/div/div/div[2]/div/div/div/div/div[1]/div/div/button/span[1]')))
                driver.execute_script("arguments[0].click();", clickQB)
                print ("done click quikc bracket")

                # Clicks down arrow if there #
                clickDA = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                            '//*[@id="fittPageContainer"]/div/div[5]/div[5]/div/section/div[3]/div/div[1]/div/section[1]/div/div[2]')))
                if (clickDA):
                    driver.execute_script("arguments[0].click();", clickDA)
                print ("done click quikc bracket")

                time.sleep(1)
                # Clicks smart bracket #
                clickSB = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                            '//*[@id="fittPageContainer"]/div/div[5]/div[5]/div/section/div[3]/div/div[1]/div/section/div[2]/div/div/div/label[5]/span[1]')))
                driver.execute_script("arguments[0].dispatchEvent(new MouseEvent('click', { bubbles: true }));", clickSB)
                print ("done click random weighted by seed")


                time.sleep(1)
                # Clicks autofill #
                clickAF = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                            '//*[@id="fittPageContainer"]/div/div[5]/div[5]/div/section/div[3]/div/div[2]/button')))
                driver.execute_script("arguments[0].click();", clickAF)
                print ("done autofill")
                
                time.sleep(1)
                # Clicks submit #
                clickSB = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                            '//*[@id="fittPageContainer"]/div/div[5]/div[3]/div/div/div/div[2]/div/div/div/div/div[1]/div/div/button')))
                driver.execute_script("arguments[0].click();", clickSB)
                print ("done click suybmit bracket")

                time.sleep(1)
                # Enter emails
                driver.switch_to.default_content()
                WebDriverWait(driver, 5).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'//*[@id="oneid-iframe"]')))
                email_input = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="InputIdentityFlowValue"]')))
                email_input.send_keys("kkeelar8+%d@gmail.com" % (varb+counter))
                print ("done send emails")

                time.sleep(1)
                # Click Continue
                clickCont = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, 
                                                            '//*[@id="BtnSubmit"]')))
                driver.execute_script("arguments[0].click();", clickCont)
                print ("done click first cont")

                time.sleep(1)
                driver.switch_to.default_content()
                WebDriverWait(driver, 5).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'//*[@id="oneid-iframe"]')))
                firstName = WebDriverWait(driver, 8).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="InputFirstName"]')))
                firstName.send_keys('Krtin')

                time.sleep(1)
                driver.switch_to.default_content()
                WebDriverWait(driver, 5).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'//*[@id="oneid-iframe"]')))
                firstName = WebDriverWait(driver, 8).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="InputLastName"]')))
                firstName.send_keys('Keelar')

                time.sleep(1)
                # Enter passwords #
                driver.switch_to.default_content()
                WebDriverWait(driver, 5).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'//*[@id="oneid-iframe"]')))
                password_input = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password-new"]')))
                password_input.send_keys('cS#qUW865r8D')

                time.sleep(1)
                clickContF = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="BtnSubmit"]')))
                driver.execute_script("arguments[0].click();", clickContF)
                print ("done entering names and passwords")

                time.sleep(5)
                # Enter one time code #
                passcode = main()
                print (passcode)

                driver.switch_to.default_content()
                WebDriverWait(driver, 5).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'//*[@id="oneid-iframe"]')))
                password_input = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="InputRedeemOTP"]')))
                password_input.send_keys(passcode)
                clickContFF = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="BtnSubmit"]')))
                driver.execute_script("arguments[0].click();", clickContFF)
                print ("done sending code")

                     

               
                # Fill out remaining bracekts #
                for x in (range (5)): 
                    
                    
                    driver.switch_to.default_content()
                    print ("here on x")
                    time.sleep(1)
                    # Create another bracket #
                    clickCAB = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, 
                                                                '//*[@id="fittPageContainer"]/div/div[5]/div[4]/div/section/div[3]/div/button[2]')))
                    print ("here on y")
                    driver.execute_script("arguments[0].click();", clickCAB)
                    print ("done click create bracket again first time")
                    
                    time.sleep(1)
                    # Click cancel if there
                    try:
                        clickCAC = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, 
                                                        '//*[@id="fittPageContainer"]/div/div[5]/div[5]/div/section/button[2]')))
                        if (clickCAC):
                            driver.execute_script("arguments[0].click();", clickCAC)
                            print("done click cancel if there")
                            time.sleep(1)
                    except TimeoutException:
                        print("Element not found. Continuing execution.")
                    

                    #Click Quick bracket #
                    clickQB = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                            '//*[@id="fittPageContainer"]/div/div[5]/div[3]/div/div/div/div[2]/div/div/div/div/div[1]/div/div/button')))
                    driver.execute_script("arguments[0].click();", clickQB)
                    print ("done click quikc bracket secon time")


                    # Clicks down arrow if there #
                    clickDA2 = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                '//*[@id="fittPageContainer"]/div/div[5]/div[5]/div/section/div[3]/div/div[1]/div/section[1]/div/div[2]')))
                    if (clickDA2):
                        driver.execute_script("arguments[0].click();", clickDA2)
                    print ("done down arrow if there")

                
                    time.sleep(1)
                    # Clicks smart bracket #
                    clickSB = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                '//*[@id="fittPageContainer"]/div/div[5]/div[5]/div/section/div[3]/div/div[1]/div/section[1]/div[2]/div/div/div/label[5]/span[1]')))
                    driver.execute_script("arguments[0].dispatchEvent(new MouseEvent('click', { bubbles: true }));", clickSB)
                    print ("done click espn smart bracket")


                    time.sleep(1)
                    # Clicks autofill #
                    clickAF = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                '//*[@id="fittPageContainer"]/div/div[5]/div[5]/div/section/div[3]/div/div[2]/button')))
                    driver.execute_script("arguments[0].click();", clickAF)
                    print ("done autofill")
                    
                    time.sleep(1)
                    # Clicks submit #
                    clickSB2 = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                '//*[@id="fittPageContainer"]/div/div[5]/div[3]/div/div/div/div[2]/div/div/div/div/div[1]/div/div/button')))
                    driver.execute_script("arguments[0].click();", clickSB2)
                    print ("done click looping suybmit bracket")


                print ("yo chjilld out")
                driver.switch_to.default_content()
                # Create another bracket #
                clickCAB = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, 
                                                            '//*[@id="fittPageContainer"]/div/div[5]/div[4]/div/section/div[3]/div/button[2]')))
                driver.execute_script("arguments[0].click();", clickCAB)
    

                time.sleep(1)
                # Add to group #
                # Clicks join group first time #
                clickJG = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,
                                                    '//*[@id="fittPageContainer"]/div/div[2]/div/div/div/div/nav/ul/li[3]/a')))
                driver.execute_script("arguments[0].click();", clickJG)
                print ("done click suybmit bracket")

                time.sleep(1)
                # Searching for groups #
                groupSearch = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="fittPageContainer"]/div/div[5]/div[2]/div/div/section[1]/header/div[2]/div/div/input')))
                groupSearch.send_keys("Lebillionares")

                time.sleep(1)
                # Click on group #
                clickOnGroup = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, 
                                                            '//*[@id="fittPageContainer"]/div/div[5]/div[2]/div/div/section[1]/header/div[2]/div/div/div[2]/button/div')))
                driver.execute_script("arguments[0].click();", clickOnGroup)

                time.sleep(1)
                # Click on join group second time #
                clickJG1 = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, 
                                                            '//*[@id="fittPageContainer"]/div/div[5]/div[2]/div/div/div/section[1]/footer/button')))
                driver.execute_script("arguments[0].click();", clickJG1)

                time.sleep(1)
                # enters group password #
                groupPW = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,                                                     
                                     '//*[@id="fittPageContainer"]/div/div[5]/div[4]/div/section/div[2]/div/div[2]/div[2]/div/input')))
                groupPW.send_keys("Th3f!ashTh3f!ash")


                driver.switch_to.default_content()
                # joins 25 brackets into group #
                gb = 2
                for gj in (range(5)):
                    clickJoinGroup = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, 
                                                            '//*[@id="fittPageContainer"]/div/div[5]/div[4]/div/section/div[2]/div/section/div[2]/ul/li[%s]/div[2]/span' % (str(gb+gj)))))
                    print ("here 2")
                    driver.execute_script("arguments[0].click();", clickJoinGroup)

                time.sleep(1)
                # Final click join group #
                driver.switch_to.default_content()
                clickJoinGroupFinal = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, 
                                                            '//*[@id="fittPageContainer"]/div/div[5]/div[4]/div/section/div[3]/button[2]')))
                driver.execute_script("arguments[0].click();", clickJoinGroupFinal)

                
                time.sleep(2)
                print ("brackets added")



            except Exception as e:
                continue

            finally:
                 driver.quit()   


billion()
##t1 = threading.Thread(target=billion, args=(500,))
##t2 = threading.Thread(target=billion, args=(1000,))
##t3 = threading.Thread(target=billion, args=(2643,))
##t4 = threading.Thread(target=billion, args=(3643,))
##t5 = threading.Thread(target=billion, args=(4643,))
##t6 = threading.Thread(target=billion, args=(5643,))
##t7 = threading.Thread(target=billion, args=(6643,))
##t1.start()
##t2.start()
##t3.start()
##t4.start()
##t5.start()
##t6.start()
##t7.start()

