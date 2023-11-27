from mss import mss
import Capture
import numpy as np
import Detection
import time
import keyboard
import pydirectinput

if __name__ == '__main__':
    screen, game_window = Capture.setup_monitor("Cookie Clicker")
    screenshot = np.array(screen.grab(game_window))
    location_to_click = Detection.click_object("Assets/cookie.png", screenshot)
    while True:
        if keyboard.is_pressed('v'):  # Check if 'V' is pressed
            print("Terminating program.")
            break
        pydirectinput.moveTo(x=location_to_click[0], y=location_to_click[1])
        pydirectinput.click()
