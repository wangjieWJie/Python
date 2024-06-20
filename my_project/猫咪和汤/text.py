import pyautogui
import cv2


window = cv2.imread("file/cat&soup/head.png")
locat_window = pyautogui.locateOnScreen(window, confidence=0.43)
print(locat_window)
print("\n")
center_window = pyautogui.center(locat_window)
print(center_window)
pyautogui.moveTo(center_window)