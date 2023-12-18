from sense_hat import SenseHat
from time import sleep
sense = SenseHat()
humidity = sense.get_humidity()
print("Humidity: %s %%rH" % humidity)

temp = sense.get_temperature()
print("Temperature: %s C" % temp)

pressure = sense.get_pressure()
print("Pressure: %s Millibars" % pressure)

while True:
    temp = sense.get_temperature()
    print("Temperature: %s C" % temp)
    sleep(5)
    