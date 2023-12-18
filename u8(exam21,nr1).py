from sense_hat import SenseHat
from time import sleep
from datetime import datetime 
sense = SenseHat()

while True:
    print("""{'time': '%s', "city": "Madrid", "temperature": %f}"""%(datetime.now().strftime("%H:%M:%S"), sense.get_temperature()))
    sleep(1)