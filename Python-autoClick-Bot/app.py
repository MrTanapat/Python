import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode, Key

TOGGLE_KEY = KeyCode(char="t")

clicking = False
mouse = Controller()


def clicker():
    while True:
        if clicking:
            mouse.click(Button.left, 1)
        time.sleep(0.01)


def toggle_event(key):
    global clicking
    if key == TOGGLE_KEY:
        clicking = not clicking
    elif key == Key.esc:
        return False


clicking_thread = threading.Thread(target=clicker)
clicking_thread.start()

with Listener(on_press=toggle_event) as listener:
    listener.join()
