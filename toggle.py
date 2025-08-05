from gpiozero import Button, LED
import time
from signal import pause

button = Button(26, bounce_time = 0.05)
red = LED(18)
blue = LED(27)
green = LED(22)

state = 0;

def next_state():
	global state
	if (state < 3):
		state += 1
	else:
		state = 1
	
	light(state)

def light(input):
	red.off()
	blue.off()
	green.off()
	
	if input == 0:
		red.off()
	elif input == 1:
		red.on()
	elif input == 2:
		blue.on()
	elif input == 3:
		green.on()

button.when_pressed = next_state
pause()
