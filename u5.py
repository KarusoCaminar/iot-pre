from sense_hat import SenseHat
sense = SenseHat()

while True:
    for event in sense.stick.get_events():
        if event.direction=="up" and event.action=="pressed":
            print("Joystickhoch")