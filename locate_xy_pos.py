import pyautogui
import keyboard
import time
while True:
    # Get the current mouse position
    x, y = pyautogui.position()

    # Display the mouse position
    print(f"Mouse position: X={x}, Y={y}")

    # Check for user input to quit
    if keyboard.is_pressed('q'):
        print("Quitting...")
        break

    time.sleep(1)