from arduino import *
from arduino_alvik import ArduinoAlvik

Alvik = ArduinoAlvik()

def PerformDance():
    AlvikLEDColors = [
        (1, 0, 0), # Red LED Light.
        (0, 0, 1), # Blue LED Light.
        (0, 1, 0), # Green LED Light.
        (1, 0, 1), # Magenta LED Light.
        (1, 1, 0), # Yellow LED Light.
        (0, 1, 1), # Cyan LED Light.
        (0, 0, 0), # Black LED Light.
    ]
    
    for AlvikLEDColor in AlvikLEDColors:
        Alvik.right_led.set_color(*AlvikLEDColor)
        Alvik.left_led.set_color(*AlvikLEDColor)
        delay(10)
    
    Alvik.set_wheels_speed(10, -10)
    Alvik.set_wheels_speed(-50, 50)
    delay(2600)

def Setup():
    Alvik.begin()
    delay(1000)
    
def Loop():
    PerformDance()

def CleanUp():
    Alvik.stop()
    

start(Setup, Loop, CleanUp)

