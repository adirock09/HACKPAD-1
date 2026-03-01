import board
import digitalio
import usb_hid
import time
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)

# Setup buttons
pins = [board.GP26, board.GP27, board.GP28, board.GP29]
buttons = []

for pin in pins:
    btn = digitalio.DigitalInOut(pin)
    btn.direction = digitalio.Direction.INPUT
    btn.pull = digitalio.Pull.UP
    buttons.append(btn)

# Key mapping
keymap = [
    Keycode.A,        # GP26
    Keycode.B,        # GP27
    Keycode.C,        # GP28
    Keycode.D         # GP29
]

previous_state = [True, True, True, True]

while True:
    for i, button in enumerate(buttons):
        if button.value != previous_state[i]:
            previous_state[i] = button.value

            if not button.value:  # pressed (LOW)
                kbd.press(keymap[i])
            else:  # released
                kbd.release(keymap[i])

    time.sleep(0.01)