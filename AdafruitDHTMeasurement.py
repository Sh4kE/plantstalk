#!/usr/bin/python

import Adafruit_DHT

sensor = Adafruit_DHT.DHT22
gpio_input_pin = 19

humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio_input_pin)

if humidity is not None and temperature is not None:
    print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
else:
    print('Failed to get reading. Try again!')
    sys.exit(1)
