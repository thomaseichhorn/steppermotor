import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode ( GPIO.BOARD )
steps = 0

# input
if ( len ( sys.argv ) == 1 ) :
	print ( "Please input step count!" )
	sys.exit ( )
elif ( len ( sys.argv ) == 2 ) :
	steps = int ( sys.argv[1] )
else :
	print ( "Couldn't read step count!" )
	sys.exit ( )

# Raspi pinout
DIR = 33
PUL = 35

left = GPIO.HIGH
right = GPIO.LOW

GPIO.setwarnings ( False )
GPIO.setup ( DIR, GPIO.OUT )
GPIO.setup ( PUL, GPIO.OUT )

# Set dir
if steps > 0 :
	GPIO.output ( DIR, right )
else :
	GPIO.output ( DIR, left )

for i in range ( abs ( steps ) ) :

	# Modulate
	GPIO.output ( PUL, GPIO.HIGH )
	time.sleep ( 0.0001875 )

	#print ( i )

	GPIO.output ( PUL, GPIO.LOW )
	time.sleep ( 0.0001875 )

#

