# -------------------------------------------------- { Import Arduino Alvik Library } -------------------------------------------------- #

from arduino import * # Import All Classes, Functions & Variables.
from arduino_alvik import ArduinoAlvik # Imports Specific Arduino Alvik Class.

# -------------------------------------------------- { MicroPython Local Variables } --------------------------------------------------- #

# Assign Arduino Alvik Class to Variable.
Alvik = ArduinoAlvik()

AlvikLEDColors = [
    # Red, Blue & Green LED.
    (1, 0, 0), # RGB: 255, 0, 0.
    (0, 0, 1), # RGB: 0, 0, 255.
    (0, 1, 0), # RGB: 0, 255, 0.
    
    # Purple, Yellow & Cyan LED.
    (1, 0, 1), # RGB: 255, 0, 255.
    (1, 1, 0), # RGB: 255, 255, 0.
    (0, 1, 1), # RGB: 0, 255, 255.
]

BaseSpeed = 10
ButtonPressed = 0

# -------------------------------------------------- { Handle Arduino Alvik Controls } ------------------------------------------------- #

def ArduinoAlvikControls():
    global ButtonPressed
    global BaseSpeed
    
    if Alvik.get_touch_ok():
        ButtonPressed = 1 # Turn On.
        
    elif Alvik.get_touch_cancel():
        Alvik.set_wheels_speed(0, 0) # Stop Wheels.
        
        # Disable(s) Both Arduino Alvik LEDs.
        Alvik.right_led.set_color(0, 0, 0) # RGB: 0, 0, 0 (Black LED).
        Alvik.left_led.set_color(0, 0, 0) # RGB: 0, 0, 0 (Black LED).
        
        ButtonPressed = 0 # Turn Off.
        
    elif Alvik.get_touch_up():
        BaseSpeed + 1
        
    elif Alvik.get_touch_down():
        BaseSpeed - 1
        

# -------------------------------------------------- { Stay Within Black Lines } ------------------------------------------------------- #

def StayWithinBorders():
    # Retrieve(s) Reading from Infrared (IR) Sensor.
    IRLeft, IRCenter, IRRight = Alvik.get_line_sensors()
    delay(10) # Add 10ms Delay.
    
    # Print the Retrieved Value(s) in the Shell.
    print("Left: ", IRLeft, " | ", "Center: ", IRCenter, " | ", "Right: ", IRRight)
    
    # If IRLeft, IRCenter & IRRight is < 70 Degrees.
    if IRLeft < 70 and IRCenter < 70 and IRRight < 70:
        Alvik.set_wheels_speed(BaseSpeed, BaseSpeed) # Drive Forward.
        
        # Disable(s) Both Arduino Alvik LEDs.
        Alvik.right_led.set_color(0, 0, 0) # RGB: 0, 0, 0 (Black LED).
        Alvik.left_led.set_color(0, 0, 0) # RGB: 0, 0, 0 (Black LED).
        
    elif IRLeft > 70: # 
        Alvik.set_wheels_speed(5, -100) # Quickly Turn Right.
        Alvik.right_led.set_color(*AlvikLEDColors[0]) # RGB: 255, 0, 0 (Red LED).
        Alvik.left_led.set_color(*AlvikLEDColors[0]) # RGB: 255, 0, 0 (Red LED).
        
    elif IRRight > 70:
        Alvik.set_wheels_speed(-100, 5) # Quickly Turn Left.
        Alvik.right_led.set_color(*AlvikLEDColors[0]) # RGB: 255, 0, 0 (Red LED).
        Alvik.left_led.set_color(*AlvikLEDColors[0]) # RGB: 255, 0, 0 (Red LED).

    else:
        # Stop Arduino Alvik Entirely.
        Alvik.set_wheels_speed(0, 0)
        
# -------------------------------------------------- { Perform Alvik Dance } ----------------------------------------------------------- #
    
def PerformDance():
    # Make a Spin Turn.
    Alvik.set_wheels_speed(-50, 50)
    
    for AlvikLEDColor in AlvikLEDColors:
        Alvik.right_led.set_color(*AlvikLEDColor)
        Alvik.left_led.set_color(*AlvikLEDColor)
        delay(500) # Add 500ms Delay.
        
# -------------------------------------------------- {  } -------------------------------------------------- #

def Setup():
    Alvik.begin()
    delay(1000)

# -------------------------------------------------- {  } -------------------------------------------------- #
    
def Loop():
    ArduinoAlvikControls()
    
    if ButtonPressed == 1:
        StayWithinBorders()
    
# -------------------------------------------------- {  } -------------------------------------------------- #

def CleanUp():
    Alvik.stop()
    
# -------------------------------------------------- {  } -------------------------------------------------- #

start(Setup, Loop, CleanUp)





