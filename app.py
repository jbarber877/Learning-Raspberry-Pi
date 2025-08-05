from flask import Flask
from gpiozero import Button, LED

btn = Button(26, bounce_time = 0.05)
red = LED(18)
blue = LED(27)
green = LED(22)

app = Flask(__name__)

@app.route('/')
def index():
	return("Hello from Flask")

@app.route("/push-button")
def check_btn_state():
	if btn.is_pressed:
		return "Button is pressed"
	else:
		return "Button is not pressed"
		
@app.route("/led/<int:led_number>/state/<int:state>")
def switch_led(led_number, state):
	red.off()
	blue.off()
	green.off()	
	
	if state == 1:
		match led_number:
			case 1:
				red.on()
			case 2:
				blue.on()
			case 3:
				green.on()
			case _:
				print("Not a valid LED")
		
	else: # state = 0
			match led_number:
				case 1:
					red.off()
				case 2:
					blue.off()
				case 3:
					green.off()
				case _:
					print("Not a valid LED")
					
	return("LED should be turned on/off")
					

				


app.run(host = '0.0.0.0')
