# Learning-Raspberry-Pi

## blink
Blinks an LED on and off at 1 second intervals

## button
Turns an LED on when a button is pushed and off when it is pushed a second time

## toggle
Turns a sequence of LEDs on/off. When the button is pressed, it is supposed to turn on the first led. When it is pressed again, it turns on the second (and the first off) when it is pressed a third time, the third led turns on (and first and second off).

## app
Flask web server for controlling Pi remotely.
/ home page returns a string /n
/push-button checks if the button is pushed and returns the state /n
/led/int/state/int turns the selected LED on or off
