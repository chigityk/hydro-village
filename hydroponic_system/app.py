from gpiozero import LED, Button
from time import sleep
import hydrogui

def h20On():
    print('Switch Pressed')
    if GPIO.input (40) :
        GPIO.output (40,GPIO.LOW)
    else:  
        GPIO.output(40, GPIO.HIGH)