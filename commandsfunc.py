import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

class ClickMouse(threading.Thread):
    def __init__(self, delay, button, stop_key, start_key):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.stop_key = stop_key
        self.start_key = start_key
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False


    def run(self):
        with Listener(on_press=self.on_press) as listener:
            while self.program_running:
                while self.running:
                    mouse.click(self.button)
                    time.sleep(self.delay)
                time.sleep(0.1)
            listener.stop()

    def on_press(self, key):
        if key == self.stop_key:
            self.stop_clicking()

        elif key == self.start_key:
            self.start_clicking()

mouse = Controller()
click_thread = ClickMouse(delay=0.001, button=Button.left,
                           stop_key=KeyCode(char='z'),
                          start_key=KeyCode(char='x'))