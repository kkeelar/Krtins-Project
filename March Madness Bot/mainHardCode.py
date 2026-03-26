
import sys
import os




from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import undetected_chromedriver as uc

import time

from pullHardCode import main as get_passcode
import random
from selenium_stealth import stealth




def resource_path(relative_path):
    if getattr(sys, '_MEIPASS', False):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.abspath(relative_path)


def get_app_dir():
    """Returns the directory where the app is running"""
    if getattr(sys, 'frozen', False):
        # Running in PyInstaller bundle
        return sys._MEIPASS  # For data inside bundle (not for progress.txt)
    return os.path.dirname(os.path.abspath(__file__))  # For running normally

def get_progress_path():
    """Path to progress.txt next to exe/app"""
    return os.path.join(os.path.dirname(sys.executable), "progress.txt")  # For exe/app

def save_progress(x):
    path = get_progress_path()
    with open(path, "w") as file:
        file.write(str(x))

def load_progress():
    path = get_progress_path()
    try:
        with open(path, "r") as file:
            return int(file.read())
    except FileNotFoundError:
        return 30000  # Default start if not exists


def rerun(driver, path, info):
    driver.switch_to.default_content()      
    try:
        button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, path)))
        driver.execute_script("arguments[0].scrollIntoView(true);", button)  # Scroll to button
        time.sleep(0.5)  # Let page adjust
        driver.execute_script("arguments[0].click();", button)  # Safe click
        #print("done with:", info)
    except Exception as e:
        print("Failed to click", info)
        

def rerunSimple(driver, path, info): 
    click = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, path)))
    driver.execute_script("arguments[0].click();", click)
    #print ('done create', info)

def infoInput(driver): 
    driver.switch_to.default_content()
    WebDriverWait(driver, 5).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'//*[@title="Account"]')))
    firstName = WebDriverWait(driver, 8).until(EC.element_to_be_clickable((By.XPATH, '//*[@class="input-InputFirstName form-control"]')))
    firstName.send_keys('Krtin')
    lastName = WebDriverWait(driver, 8).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="InputLastName"]')))
    lastName.send_keys('Keelar')
    password = WebDriverWait(driver, 8).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password-new"]')))
    password.send_keys('2308tnonwjg!!3qe')

    


def passCode(driver, emailBase, emailRealPassword): 
    # Try to detect the passcode input field (without crashing if it's not there)
    try:
        driver.switch_to.default_content()
        WebDriverWait(driver, 3).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//*[@id="oneid-iframe"]')))
        passcode_input = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="otp-code-input-0"]')))
        #print("Passcode prompt detected!")

        # Fetch passcode only if prompt is there
        time.sleep(5)
        passcode = get_passcode(emailBase, emailRealPassword)
        #print(f"Passcode: {passcode}")

        # Enter passcode
        passcode_input.send_keys(passcode)
        clickPassCodeCont = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Continue"]')))
        driver.execute_script("arguments[0].click();", clickPassCodeCont)
        #print("Submitted passcode.")

    except TimeoutException:
        print("No passcode prompt, continuing...")
      



def main(start):

    data = { 
         'createBracketBig': '//*[@class="Button Button--lg Button--default Button--dark ChuiButton ChuiButton--promoted ChuiButton--primary WelcomeScreenHero-button css-zwdj77"]', 
         'firstQuick': '//*[text()="Quick Bracket"]',
         'firstDown': '//*[text()="Easy Options"]',          
         'firstSmart': '//*[text()="Smart Bracket"]', 
         'firstAuto': '//*[@id="fittPageContainer"]/div/div/div[5]/div[5]/div/section/div[3]/div/div[2]/div/button',
         'firstSubmit': '//*[@id="fittPageContainer"]/div/div/div[5]/div[3]/div/div/div/div/div[3]/div/div/div/div/div[1]/div/div/button', 
         'createAccount': '//*[text()="Continue"]',
         'agree': '//*[text()="Agree & Continue"]',
         'submitText': '//*[text()="Submit Bracket"]',
         "LOOOOOPING": "---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------",
         'loopQuickBracket': '//*[@id="fittPageContainer"]/div/div/div[5]/div[3]/div/div/div/div/div[3]/div/div/div/div/div[1]/div/div/button',
         'loopDownArrow': '//*[@id="fittPageContainer"]/div/div/div[5]/div[5]/div/section/div[3]/div/div[1]/div/section[1]/div/div[2]', 
         'loopSmart': '//*[@id="fittPageContainer"]/div/div/div[5]/div[5]/div/section/div[3]/div/div[1]/div/section[1]/div[2]/div/div/div/label[1]/span[1]', 
         'loopAuto': '//*[@id="fittPageContainer"]/div/div/div[5]/div[5]/div/section/div[3]/div/div[2]/div/button',
         'loopSubmit': '//*[@id="fittPageContainer"]/div/div/div[5]/div[3]/div/div/div/div/div[3]/div/div/div/div/div[1]/div/div/button',
         'loopCreateAntBetter': '//*[text()="Create Another Bracket"]',
         "GROOUP": '-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------',
         'loopGroupLink': '//*[@id="fittPageContainer"]/div/div/div[2]/div/div/div/div/nav/ul/li[3]/a', 
         'loopGroupSearch': '//*[@class="Input Input--dark"]', 
         'loopGroupAns': '//*[@class="GroupSearch-name"]',
         'joinGroupOne': '//*[@id="fittPageContainer"]/div/div/div[5]/div[3]/div/div/div/div/section[1]/footer/button',
         'loopAddToGroup': '//*[@id="fittPageContainer"]/div/div/div[5]/div[3]/div/div/div[1]/div/section[1]/footer/button[2]', 
         'joinGroup': '//*[@id="fittPageContainer"]/div/div/div[5]/div[5]/div/section/div[3]/div/button[2]',
         'groupPass': '//*[@id="fittPageContainer"]/div/div/div[5]/div[5]/div/section/div[2]/div[2]/div[2]/div/input',
         'cancel': '//*[text()="Cancel"]'
    }


    emailPasswords = {
        'kkeelar1': 'nijl sqmp gmwj eefo',
        'kkeelar2': 'qbch zqea zssj pkqj',
        'kkeelar3': 'zqfy vwuc vjew fwdu',
        'kkeelar4': 'jccn akhj wyiu nbzw',
        'kkeelar5': 'vuaa fhgn mpoe rfwy',
        'kkeelar6': 'mudu iqlj tfhx kfcv',
        'kkeelar7': 'veqy vwgr ycgn qkw',
        #'kkeelar11': 'spbs znvf joiz pygb',
        'kkeelar8': 'afay qnyx hhcg ewgv',
        'kkeelar12': 'gopj pfkp pzqp cikw'
    }

    emailKeys = ['kkeelar2', 'kkeelar3', 'kkeelar4', 'kkeelar5', 'kkeelar6', 'kkeelar7', 'kkeelar8', 'kkeelar1', 'kkeelar12']


    
    for x in range(start, 1000000000000000000000000000000000000000000000000):

        driver = None
    
        try: 
            # Use chromedriver dynamically
            options = uc.ChromeOptions()
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-blink-features=AutomationControlled")
            
            driver = uc.Chrome(options=options, driver_executable_path=resource_path("chromedriver"))

            

            driver.get("https://fantasy.espn.com/games/tournament-challenge-bracket-2025/?gad_source=1&gclid=Cj0KCQjw7dm-BhCoARIsALFk4v8DUdlDsNeGkbX2awHNhRQ3LGW1wdZB5iuTnUqMEWBp5xcrrShmcD0aAhaFEALw_wcB")
            # Hide navigator.webdriver
            driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
                        # Fake plugins and languages
            driver.execute_script("""
                Object.defineProperty(navigator, 'plugins', {
                    get: () => [1, 2, 3, 4, 5],
                });
                Object.defineProperty(navigator, 'languages', {
                    get: () => ['en-US', 'en'],
                });
            """)

                        # Prevent WebRTC IP leak
            driver.execute_cdp_cmd("Network.enable", {})
            driver.execute_cdp_cmd("Network.setExtraHTTPHeaders", {
                "headers": {
                    "User-Agent": driver.execute_script("return navigator.userAgent;")
                }
            })
            driver.execute_cdp_cmd(
                "Network.setBypassServiceWorker",
                {"bypass": True}
            )


            driver.set_window_size(random.randint(1024, 1920), random.randint(768, 1080))

            # Apply stealth
            stealth(driver,
                languages=["en-US", "en"],
                vendor="Google Inc.",
                platform="MacIntel",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True,
            )

            driver.delete_all_cookies()
            driver.execute_script("window.localStorage.clear();")
            driver.execute_script("window.sessionStorage.clear();")
            driver.execute_script("window.indexedDB.databases().then(dbs => dbs.forEach(db => window.indexedDB.deleteDatabase(db.name)));")


            
            # Click create bracket # 
            time.sleep(1)
            rerun(driver, data['createBracketBig'], 'first create')

            # First click quick picks #
            time.sleep(1)
            rerun(driver, data['firstQuick'], 'first quick pick')

            time.sleep(1)
            rerun(driver, data['firstDown'], "first down arrow")

            # first smart create# 
            time.sleep(1)
            rerun(driver, data['firstSmart'], 'click first smart')

            # Click Autofill # 
            time.sleep(1)
            rerun(driver, data['firstAuto'], 'click first auto')

            # Click first submit #
            time.sleep(3)
            rerun(driver, data['submitText'], 'click first submit')

            # Send email Info #
            time.sleep(1)
            driver.switch_to.default_content()
            WebDriverWait(driver, 5).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'//*[@id="oneid-iframe"]')))
            email = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="InputIdentityFlowValue"]')))

            emailBase = random.choice(emailKeys)
            emailRealPassword = emailPasswords[emailBase]
    
            emailInput = "mariane42@veum.com"
            email.send_keys(emailInput)
            print (emailBase, emailRealPassword)

            # First email cont button #
            time.sleep(2)
            rerunSimple(driver, data['createAccount'], 'email continue')

            time.sleep(1)
            # Account info input #
            infoInput(driver)

            # FInish account cont button #
            time.sleep(1)
            rerunSimple(driver, data['agree'], 'create account full')
            
            time.sleep(1)
            # If passcode prompt comes up, run that code and send it #
            passCode(driver, emailBase, emailRealPassword)

            time.sleep(1)
            driver.switch_to.default_content()
            
            n = 10
            for i in range(n):

                time.sleep(1)
                rerun(driver, data['loopCreateAntBetter'], 'loop create anothter')

                time.sleep(1)
                rerun(driver, data['cancel'], "cnacle import")

                if (i == n-1): 
                    break
                time.sleep(1)
                rerun(driver, data['first quick'], 'loop quick brakcet')
                
                time.sleep(1)
                rerun(driver, data['firstDown'], 'loop down arrow')

                time.sleep(1)
                rerun(driver, data['firstSmart'], 'loop smart bracket')


                time.sleep(1)
                rerun(driver, data['loopAuto'], 'loop auto fill')

                time.sleep(1)
                rerun(driver, data['submitText'], 'loop submit')
            

            driver.switch_to.default_content()
            time.sleep(1)
            rerun(driver, data['loopGroupLink'], 'click group add')

            time.sleep(1)
            groupSearch = WebDriverWait(driver, 8).until(EC.element_to_be_clickable((By.XPATH, '//*[@class="Input Input--dark"]')))
            groupSearch.send_keys('LeBillionares')

            time.sleep(1)
            rerun(driver, data['loopGroupAns'], 'click on group')

            time.sleep(1)
            rerun(driver, data['joinGroupOne'], 'click join afgter searching')

            for y in range(n-1): 
                path = f'//*[@id="fittPageContainer"]/div/div/div[5]/div[5]/div/section/div[2]/section/div[2]/ul/li[{y+2}]/div[2]/span'
                rerun(driver, path, f'added entry {y+2}  to group')

            time.sleep(1)
            groupSearch = WebDriverWait(driver, 8).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="fittPageContainer"]/div/div/div[5]/div[5]/div/section/div[2]/div[2]/div[2]/div/input')))
            groupSearch.send_keys('Th3f!ashTh3f!ash')

            time.sleep(1)
            rerun(driver, data['joinGroup'], 'joinGroup')
 
        except Exception as e:
            print(f"ERROR on ATTEMEPTTTTT {x}", e)
            continue
        finally:
            time.sleep(5)
            if driver:
                driver.quit()
        print("Added", n, "brackets!")
        save_progress(x)

        
      
            
# main loop
if __name__ == "__main__":
    start_number = load_progress()
    print("STARTING FROM:", start_number)
    main(start_number)
