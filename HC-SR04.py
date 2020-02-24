#-------------------------------------------------------------------------
#
#		Name: 		Eng. William R. Fröhlich
#
#		Project: 	HC-SR04 - Ultrasonic
#
#		Date: 		2019.03.23
#
#-------------------------------------------------------------------------

# Import Library
import RPi.GPIO as GPIO
import time

# Define the pin
GPIO.setmode(GPIO.BOARD)

Trigger = 10
Echo = 12

# Define the Variable
GPIO.setup(Trigger,GPIO.OUT)
GPIO.setup(Echo,GPIO.IN)

print "Sensor Ultrasonico"

try:
	while(True):
		#Start the Trigger in Low
		GPIO.output(Trigger,False)
		time.sleep(1)
		
		#Send the pulse - 1us
		GPIO.output(Trigger,True)
		time.sleep(0.00001)
		#Desabilita o Trigger
		GPIO.output(Trigger,False)
		
		#Start the Time
		inicio=time.time()
		
		#While wait...
		while GPIO.input(Echo)==0:
			inicio=time.time()
						
		#When receive...
		while GPIO.input(Echo)==1:
			final=time.time()
						
		#Elapsed Time
		tempo_transcorrido=final-inicio
				
		#Distance
		distancia=(tempo_transcorrido*34000)/2
		
		print "Distancia=%.1f cm"%distancia
		
except KeyboardInterrupt:
		GPIO.cleanup()
				
