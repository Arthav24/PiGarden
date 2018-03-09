import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pins = [14,15,18,23,24] 
GPIO.setup(pins, GPIO.OUT)

#relay attachments:
#14 is garden valve
#15 is seed plot valve
#18 is bigger seed plot valve
#23 is outdoor valve
#24 is main pump motor

for components in pins[0:4]:
	GPIO.output(pin, GPIO.LOW)
	#opens all for valves
time.sleep(5)
GPIO.output(pins[5], GPIO.LOW)
#turns on the main motor pump

c=0
while (c<=3):
	avgsensorG
	avgsensorSP
	avgsensorBSP
	avgsensorO
	
	if (str(avgsensorG)='1'):
		w="Garden"
		GPIO.output(pins[0], GPIO.HIGH)
		c=c+1

	elif (str(avgsensorSP)='1'):
		w="seed plot"
		GPIO.output(pins[1], GPIO.HIGH)
		c=c+1

	elif (str(avgsensorBSP)='1'):
		w="bigger seed plot"
		GPIO.output(pins[2], GPIO.HIGH)
		c=c+1

	elif (str(avgsensorO)='1'):
		w="outdoors"
		GPIO.output(pins[3], GPIO.HIGH)
		c=c+1
		

GPIO.cleanup()
print "Shutdown All relays"
