import pyautogui
import time

  #abrir o google chorume
  

pyautogui.press ("win")
pyautogui.write("google")
pyautogui.press("enter")
time.sleep(0.3)
pyautogui.write("http://127.0.0.1:5500/index05.html")
pyautogui.press("enter")
time.sleep(0.5)
pyautogui.click(x=1408, y=741)
pyautogui.write("jeleia")
pyautogui.press("tab")
pyautogui.write("jeleia64@gmail.com")
pyautogui.press("tab")
pyautogui.write("1234567891011121314151617181920")
pyautogui.press("tab")
pyautogui.press("space")
pyautogui.press("right")
pyautogui.press("tab")
pyautogui.press("enter")