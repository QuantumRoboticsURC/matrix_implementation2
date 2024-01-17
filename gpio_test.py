import Jetson.GPIO as GPIO
import time



pin_1 = 27 # 31 works ok
pin_2 = 19

value = input("give me a value: ")

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin_1, GPIO.OUT)
GPIO.setup(pin_2, GPIO.OUT)

while value != "-1":

    if value == "00":    
        GPIO.output(pin_1, GPIO.LOW)
        GPIO.output(pin_2, GPIO.LOW) 
    elif value == "01":
        GPIO.output(pin_1, GPIO.HIGH)
        GPIO.output(pin_2, GPIO.LOW)
    elif value == "10":
        GPIO.output(pin_1, GPIO.LOW)
        GPIO.output(pin_2, GPIO.HIGH)
    elif value == "11":
        GPIO.output(pin_1, GPIO.HIGH)
        GPIO.output(pin_2, GPIO.HIGH)
    value = input("give me a value: ")


GPIO.output(pin_1, GPIO.LOW)
GPIO.output(pin_2, GPIO.LOW) 

GPIO.cleanup()
