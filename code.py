import time
import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
import board
import digitalio


btn1_pin = board.GP7
btn2_pin = board.GP8
btn3_pin = board.GP9
btn4_pin = board.GP18
btn5_pin = board.GP20
btn6_pin = board.GP19

btn1 = digitalio.DigitalInOut(btn1_pin)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.DOWN

btn2 = digitalio.DigitalInOut(btn2_pin)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.DOWN

btn3 = digitalio.DigitalInOut(btn3_pin)
btn3.direction = digitalio.Direction.INPUT
btn3.pull = digitalio.Pull.DOWN

btn4 = digitalio.DigitalInOut(btn4_pin)
btn4.direction = digitalio.Direction.INPUT
btn4.pull = digitalio.Pull.DOWN

btn5 = digitalio.DigitalInOut(btn5_pin)
btn5.direction = digitalio.Direction.INPUT
btn5.pull = digitalio.Pull.DOWN

btn6 = digitalio.DigitalInOut(btn6_pin)
btn6.direction = digitalio.Direction.INPUT
btn6.pull = digitalio.Pull.DOWN

keyboard = Keyboard(usb_hid.devices)

while True:
    if btn1.value:
        keyboard.send(Keycode.CONTROL, Keycode.SHIFT, Keycode.M) #Toggle mute
        time.sleep(0.1)
    if btn2.value:
        keyboard.send(Keycode.CONTROL, Keycode.SHIFT, Keycode.O) #Toggle video
        time.sleep(0.1)
    if btn3.value:
        keyboard.send(Keycode.ALT, Keycode.SHIFT, Keycode.J) #Join meeting from outlook reminder
        time.sleep(0.1)
    if btn4.value:
        keyboard.send(Keycode.CONTROL, Keycode.SHIFT, Keycode.S) #Accept call with audio only
        time.sleep(0.1)
    if btn5.value:
        keyboard.send(Keycode.CONTROL, Keycode.SHIFT, Keycode.A) #Accept call with audio/video
        time.sleep(0.1)
    if btn6.value:
        keyboard.send(Keycode.CONTROL, Keycode.SHIFT, Keycode.H) #Disconnect from call
        time.sleep(0.1)
    time.sleep(0.1)

