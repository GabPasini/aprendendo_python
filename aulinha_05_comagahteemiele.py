import pyautogui

  #abrir o google chorume
  
refazer = 0  

pyautogui.hotkey("win","r")
pyautogui.press ("enter")
pyautogui.write("color 2")
pyautogui.press("enter")
pyautogui.press("f11")
while refazer == 0:
   pyautogui.write("tree")
   pyautogui.press("enter")

