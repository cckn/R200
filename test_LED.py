import time
import RPi.GPIO as GPIO


# LED GPIO SET
 
 
GPIO.setmode(GPIO.BCM)

LED1 = 16
LED2 = 17

GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)

while 1:


    GPIO.output(LED1, False)
    GPIO.output(LED2, False)
    time.sleep(0.2)
    
    GPIO.output(LED1, True)
    GPIO.output(LED2, True)
    time.sleep(0.2)
    
