import pyautogui
import time
import keyboard
import win32api, win32con

# https://lagged.com/en/g/magic-tiles

time.sleep(3)
print("started")
# RGB: ( 47,  47,  55)
# X:  429 Y:  522 RGB: ( 21,  49,  86)
#Tile 1 Position: X:  300 Y:  800 RGB: ( 47,  47, 55)
#Tile 2 Position: X:  425 Y:  800 RGB: (  0,   0,   0)
#Tile 3 Position: X:  535 Y:  800 RGB: ( 79,  82, 116)
#Tile 4 Position: X:  650 Y:  800 RGB: ( 80,  83, 116)


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1) #This pauses the script for 0.1 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(300, 800)[1] in range(40,55):
        click(300, 800)
    if pyautogui.pixel(425, 800)[1] in range(40,55):
        click(425, 800)
    if pyautogui.pixel(535, 800)[1] in range(40,55):
        click(535, 800)
    if pyautogui.pixel(650, 800)[1] in range(40,55):
        click(650, 800)
