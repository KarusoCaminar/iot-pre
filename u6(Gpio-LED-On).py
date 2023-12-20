from gpiozero import LED
led = LED(21)
while True:
    led.on()
