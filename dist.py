from gpiozero import DistanceSensor

distSens = DistanceSensor(echo=17, trigger=4)

while True:
	print(distSens.distance)


