from PIL.ImageOps import grayscale
import pyautogui
import time
import keyboard
import numpy as np
from random import randint

starter = int(0)
time.sleep(2)

#Main
def new_map():
    #Connect Wallet Button click
    if pyautogui.locateOnScreen('newmap_button.jpg', grayscale=True, confidence=0.8) != None:
        newmap__button = pyautogui.locateOnScreen('newmap_button.jpg', confidence=0.8)
        newmap_Button_x, newmap_Button_y = pyautogui.center(newmap__button)
        #print("Connect Wallet Button position: X:", newmap_Button_x, "Y:", newmap_Button_y)
        pyautogui.click(newmap_Button_x, newmap_Button_y)
        time.sleep(3)


