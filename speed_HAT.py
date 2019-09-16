#Coded by: Chad Martin
#Creation date: 25MAR2019
#Revision 1.0

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

TRIG = 24
ECHO = 25
RIGHT = 21
LEFT = 5
STOPPING_DISTANCE = 5
DISTANCE_MAX = .5

# Initialization for Echo #
try:
	GPIO.setwarnings(False)
	GPIO.setup(TRIG,GPIO.OUT)
	GPIO.setup(ECHO,GPIO.IN)

# Initialization for Motors #
	GPIO.setup(RIGHT,GPIO.OUT) # Right Wheel 
	GPIO.setup(LEFT,GPIO.OUT) # Left Wheel

	r = GPIO.PWM(RIGHT,50) # Arguments are pin and frequency
	r.start(0) # Argument is initial duty cycle, it should be 0

	l = GPIO.PWM(LEFT,50) # Arguments are pin and frequency
	l.start(0) # Argument is initial duty cycle, it should be 0

	ratio = 1 # Wheels will start off at the same ratio

	while True:
	# start overhead for getting distance each time #
		GPIO.output(TRIG, False)

		time.sleep(.5)

		GPIO.output(TRIG, True)
		time.sleep(0.00001)
		GPIO.output(TRIG, False)

		while GPIO.input(ECHO)==0:
			pulse_start = time.time()

		while GPIO.input(ECHO)==1:
			pulse_end = time.time()

			pulse_duration = pulse_end - pulse_start

			distance = pulse_duration * 17150
			distance = round(distance, 20)
			print("DISTANCE", distance)
	# end overhead for getting distance each time #

	# start overhead for motor speed each time each time #
			duty = distance / DISTANCE_MAX
			print("DUTY", duty)

			if(distance > STOPPING_DISTANCE):
				r.ChangeDutyCycle(duty) # Change duty cycle for right wheel
				l.ChangeDutyCycle((duty * ratio)) # Change duty cycle for left wheel with ratio
			else:
				r.ChangeDutyCycle(0)
				l.ChangeDutyCycle(0)
		# end overhead for motor speed each time each time #
except: KeyboardInterrupt

finally:
    GPIO.cleanup()

