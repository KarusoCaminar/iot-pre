from sense_hat import SenseHat
from time import sleep
from datetime import datetime
import paho.mqtt.client as mqtt

sense = SenseHat()


client = mqtt.Client()
client.connect("broker.emqx.io", 1883, 60)
client.loop_start()

while True:
   var1 = """{'"ime": "%s", "city": "Madrid", "temperature": %f}"""%(datetime.now().strftime("%H:%M:%S"), sense.get_temperature())
   temp = sense.get_temperature()
   print(temp)
   if temp > 24: client.publish("/ETSIDI/666", var1)
   sleep(0.5)

client.disconnect()
client.loop_stop()