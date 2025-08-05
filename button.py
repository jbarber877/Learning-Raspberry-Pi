from gpiozero import Button, LED
import time
from signal import pause

button = Button(26)
led = LED(18)


#while True:
#	time.sleep(0.01)
#	if (button.is_pressed):
#		led.on()#	time.sleep(1)
#	else:
#		led.off()


button.when_pressed = led.on
button.when_released = led.off
pause()
