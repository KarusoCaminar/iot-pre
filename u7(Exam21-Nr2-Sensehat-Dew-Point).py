from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

flash = lambda: print("FLASH")

while True:
    humidity = 100#sense.get_humidity()
    temp = sense.get_temperature()
    dew = temp - (100-humidity)/5
    if temp==dew: flash()
    print(dew)
    sleep(0.5)
    
    

