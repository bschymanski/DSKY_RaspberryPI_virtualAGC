import RPi.GPIO as GPIO           # import RPi.GPIO module  
import time
GPIO.setmode(GPIO.BCM)            # choose BCM or BOARD  
GPIO.setup(25, GPIO.OUT) # set a port/pin as an output   
GPIO.output(25, 0)       # set port/pin value to 0/GPIO.LOW/False  
time.sleep(0.5)
GPIO.output(25, 1)       # set port/pin value to 1/GPIO.HIGH/True  
time.sleep(0.2)
GPIO.output(25, 0)       # set port/pin value to 0/GPIO.LOW/False  
time.sleep(0.5)
#GPIO.output(25, 1)
#time.sleep(0.5)
GPIO.cleanup()