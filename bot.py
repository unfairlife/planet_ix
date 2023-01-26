from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from PIL.ImageOps import grayscale
import pyautogui
import time
import keyboard
import numpy as np
from random import randint
from accounts import accounts

import time
meta_accounts = [
        "",
        ""]

EXTENSION_PATH = r'C:\Users\Mateus\Documents\Python\MetaMask 10.24.1.0.crx'

for contas in (meta_accounts):
    #print(contas)
    opt = Options()
    opt.add_extension(EXTENSION_PATH)

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opt)

    driver.switch_to.window(driver.window_handles[0])

    #Get Started

    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='app-content']/div/div[2]/div/div/div/ul/li[1]/button"))).click()

    #Import Wallet
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='app-content']/div/div[2]/div/div/div/div/button[1]"))).click()
    #sleep(100)
    #Donate Data. No thanks!
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='app-content']/div/div[2]/div/div/div/div[2]/form/div[3]/label/input"))).click()

    #time.sleep(100)
    #Passwords
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='app-content']/div/div[2]/div/div/div/div[2]/form/div[1]/label/input"))).send_keys("ENDlessc@ve1")
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='app-content']/div/div[2]/div/div/div/div[2]/form/div[2]/label/input"))).send_keys("ENDlessc@ve1")

    #Seed phrase
    #seven lunch used midnight quality fresh sleep little siren choice artwork then
    #WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, ""))).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='app-content']/div/div[2]/div/div/div/div[2]/form/button"))).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='app-content']/div/div[2]/div/div/div/div[5]/button[1]"))).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='popover-content']/div/div/section/div[1]/div/div/label/input"))).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='popover-content']/div/div/section/div[2]/div/button[2]"))).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='app-content']/div/div[2]/div/div/div/div[2]/button"))).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='app-content']/div/div[2]/div/div/div/div[2]/button"))).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='app-content']/div/div[2]/div/div/div/div[2]/button"))).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='app-content']/div/div[1]/div/div[2]/div/div/span"))).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div[3]/button"))).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='app-content']/div/div[3]/div/div[2]/div[2]/div/div[2]/div[9]/div[2]/button"))).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='popover-content']/div/div/section/div/div/div[2]/div/button[2]"))).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='tippy-tooltip-12']/div/div[2]/div/div[1]/button/i"))).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='popover-content']/div/div/section/div/div/button[1]"))).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='popover-content']/div/div/section/div[3]/button"))).click()




    #Add account that already exists using private key
    #Button to access menu
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='app-content']/div/div[1]/div/div[2]/button"))).click()

    #Import account
    #WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, ""))).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='app-content']/div/div[3]/button[2]"))).click()


    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='private-key-box']"))).send_keys(contas)
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='app-content']/div/div[3]/div/div/div[2]/div[2]/div[2]/button[2]"))).click()


    driver.get('https://missioncontrol.planetix.com/connect')
    driver.set_window_size(1366, 768)
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='app']/main/div[4]/div/div[2]/button[1]"))).click()

    #sleep(1000)

    ## METAMASK ##
    #main_page = driver.current_window_handle

    sleep(1)
    parent = driver.window_handles[0]
    chwnd = driver.window_handles[2]
    driver.switch_to.window(chwnd)
    sleep(1)
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div[3]/div[2]/button[2]"))).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='app-content']/div/div[2]/div/div[2]/div[2]/div[2]/footer/button[2]"))).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='app-content']/div/div[2]/div/div[3]/button[2]"))).click()
    ########### ENDMETAMASK ##########
    driver.switch_to.window(parent)
    sleep(8)
    driver.get("https://missioncontrol.planetix.com/mission-control")
    #Close the new window, if that window no more required
    #driver.close();
    sleep(13)

    print("Rodar o search pela imagem agora")


    #Get the trash
    for i in range(6):
        pyautogui.click(795,305)
    for i in range(6):
        pyautogui.click(905,464)
    for i in range(6):
        pyautogui.click(811,641)
    for i in range(6):
        pyautogui.click(585,646)
    for i in range(6):
        pyautogui.click(488,460)
    for i in range(6):
        pyautogui.click(601,310)
    #CLAIM ====
    sleep(1)
    pyautogui.click(1237, 710)
    #CONFIRM ====
    sleep(2)
    pyautogui.click(909,745)
    #METAMASK WILL OPEN THE GAS
    #Swith to metamask
    wait = WebDriverWait(driver, 12)
    gas = "//*[@id='app-content']/div/div[2]/div/div[5]/div[2]/div/div/div/div[2]/div[2]/div[1]/div/h6[1]/div/div[2]/span[2]"
    original_window = driver.current_window_handle
    sleep(10)
    # driver.switch_to.window(driver.window_handles[0])
    #driver.switch_to.window(driver.window_handles[2])
    sleep(10)
    print("Excutei a troca pra metamask")

    try:
        if (len(driver.find_elements(By.XPATH, "//*[contains(text(),'$0.01')]")) >0 or
            len(driver.find_elements(By.XPATH, "//*[contains(text(),'$0.02')]")) >0 or
            len(driver.find_elements(By.XPATH, "//*[contains(text(),'$0.03')]")) >0 or   
            len(driver.find_elements(By.XPATH, "//*[contains(text(),'$0.05')]")) >0):

            print('Valor pagavel, eu clicaria na metamask')
            #WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='app-content']/div/div[2]/div/div[5]/div[3]/footer/button[2]"))).click()

        else:
            print('Not In Stock')
    except:
        print('Something went wrong')
        pass
    #
    sleep(5)
    driver.close()
    #SWITCH BACK TO MAIN -
    #driver.switch_to.window(driver.window_handles[0])

    sleep(10)
