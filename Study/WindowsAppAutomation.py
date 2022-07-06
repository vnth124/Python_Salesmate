import pyautogui
from win32api import GetSystemMetrics
import os
print("SalesMate + Backup Manu Test")
print("Create a Database Backup directory called SMP")

path="C:/SMP"
if not os.path.exists(path):
    os.makedirs(path)


#get the width and height of the monitor
width= GetSystemMetrics(0)
height=GetSystemMetrics(1)
#click on the botton left to launch the start menu
print("click on the botton left to launch the start menu")
pyautogui.click(1,height)

print("Select the SalesMate + Application")
pyautogui.typewrite("SalesMate +")
print("Press Enter Key to Launch SalesMate + Application and Wait for 10 Sec")
pyautogui.press("enter",1,10)
#Sometimes SalesMate + might take 10 seconds to load it . So 10 sec delay
print("Press Enter Key again to close the Tip Of the Day Dialog")
pyautogui.press("enter")

print("Now alt and f shortcut key in  Salesmate to invoke the File Root menu")
pyautogui.press(['alt','f'])
print("Now press 'b' to invoke the Bacuup Folder Dialog")
pyautogui.press("b")

print("Go to C Drive")
pyautogui.press("o",1,1)
print("Now press Right arrow Key to Expand the Tree")
pyautogui.press("right",1,1)
print("Go to SMP Folder")
pyautogui.typewrite("smp")
print("Press Enter Key to Backup Data")
pyautogui.press("enter",1,2)
print("Press Enter Again to Close the OK Button")
pyautogui.press("enter")

print("Adding a new customer")
print("Now alt and c shortcut key in  Salesmate to invoke the File Root menu")
pyautogui.press(['alt','c'])
print("Now press 'a' to add new customer")
pyautogui.press("a")
pyautogui.press("enter")
pyautogui.press("enter")
pyautogui.typewrite("Amazon")
pyautogui.press("enter")
pyautogui.typewrite("Google")
pyautogui.press("enter")
pyautogui.typewrite("Mr")
pyautogui.press("enter")
pyautogui.typewrite("US")
pyautogui.press("enter")
pyautogui.typewrite("7025421105")
pyautogui.press("enter")
pyautogui.typewrite("Amazon@gmail.com")
pyautogui.press("enter")
pyautogui.press("enter")
pyautogui.press("enter")
pyautogui.press("enter")
pyautogui.press("enter")
pyautogui.press("enter")
pyautogui.press("esc")
pyautogui.press("enter")
pyautogui.press("enter")
pyautogui.press("esc")

