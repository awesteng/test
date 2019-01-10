from gpiozero import TrafficLights
from time import sleep

lights = TrafficLights(2, 3, 4)

lights.green.on()

while True:
    sleep(.9000)
    lights.green.off()
    lights.amber.on()
    sleep(.1000)
    lights.amber.off()
    lights.red.on()
    sleep(.7000)
    
    lights.red.off()
    lights.amber.on()
    sleep(.1000)
    lights.green.on()
    lights.amber.off()
    lights.red.off()
