import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
pin_ldr = 4
pin_led = 17
GPIO.setup(pin_ldr, GPIO.IN)
GPIO.setup(pin_led, GPIO.OUT)



while True:
    input_value = GPIO.input(pin_ldr)
    print(input_value)
    if(input_value==1):
        GPIO.output(pin_led, GPIO.HIGH)
        time.sleep(1) 
    else:
        GPIO.output(pin_led, GPIO.LOW)
        time.sleep(1)
