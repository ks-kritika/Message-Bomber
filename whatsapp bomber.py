import pyautogui
import time
count=int(input("HOW MANY LINES? "))
while count:
    time.sleep(0)
    pyautogui.typewrite("This is the message box !!!!")
    pyautogui.press("enter")
    count-=1
