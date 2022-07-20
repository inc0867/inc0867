import pyautogui
import os

#pip install pyautogui
#pip install pillow

a = 1
i = 0

while a == 1:
    image = pyautogui.screenshot()
    i += 1
    i = str(i)
    filename = i + "görüntü.jpg"

    image.save(filename)
    i = int(i)
