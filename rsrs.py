import pyautogui
import time

pyautogui.press ("win")
pyautogui.write("google")
pyautogui.press("enter")
time.sleep(0.3)
pyautogui.write("https://ut10-battle.undertale.com/")
pyautogui.press("enter")
time.sleep(1.5)
pyautogui.click(x=1445, y=947)
time.sleep(4)
pyautogui.press("D")

