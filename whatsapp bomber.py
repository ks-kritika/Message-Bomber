import pyautogui
import time
count=int(input("HOW MANY LINES? "))
while count:
    time.sleep(0)
    pyautogui.typewrite("I LOVE YOU !!!!")
    pyautogui.press("enter")
    count-=1
