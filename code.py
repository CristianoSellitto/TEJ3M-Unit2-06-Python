# Created by: Cristiano S
# Created on: March 2023
#
# Uses a distance sensor to find the distance of an object in centimeters

import time
import board
import adafruit_hcsr04

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.GP2, echo_pin=board.GP3)

while True:
    try:
        print(sonar.distance)
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)
