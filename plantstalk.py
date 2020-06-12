#!/usr/bin/python

import signal
import Adafruit_DHT
import Adafruit_BMP.BMP085 as BMP085

from influxdb import InfluxDBClient
from RepeatedTimer import RepeatedTimer

## BMP180 Sensor ##
bmp_sensor = BMP085.BMP085()

## DHT22 Sensor ##
dht_sensor_1 = Adafruit_DHT.DHT22
dht_sensor_2 = Adafruit_DHT.DHT22
gpio_input_pin_1 = 19
gpio_input_pin_2 = 20

## InfluxDB ##
influx_host_ip = '192.168.178.55'
influx_host_port = 8086
influx_db = 'plantstalk'
json_body = [
    {
        "measurement": "plantstalk",
        "fields": {
            "temperature_1": 0.0,
            "humidity_1": 0.0,
            "temperature_2": 0.0,
            "humidity_2": 0.0,
            "pressure": 0.0,
        }
    }
]

def measure():
    humidity1, temperature1 = Adafruit_DHT.read_retry(dht_sensor_1, gpio_input_pin1)
    humidity2, temperature2 = Adafruit_DHT.read_retry(dht_sensor_2, gpio_input_pin2)
    pressure = bmp_sensor.read_pressure()
    if not humidity or not temperature1 or not temperature2:
        return measure()
    return humidity1, temperature1, humidity2, temperature2,  pressure

def send_measurements(client, humidity1, temperature1, humidity2, temperature2, pressure):
    json_body[0]['fields']['temperature_1'] = temperature1
    json_body[0]['fields']['pressure'] = pressure
    if 0 <= humidity1 <= 100:
        json_body[0]['fields']['humidity_1'] = humidity1
    else:
        json_body[0]['fields'].pop('humidity_1', 0)

    if 0 <= humidity2 <= 100:
        json_body[0]['fields']['humidity_2'] = humidity_2
    else:
        json_body[0]['fields'].pop('humidity_2', 0)

    ret = client.write_points(json_body)

def measurements(client):
    h1, t1, h2, t2, p = measure()
    send_measurements(client, h1, t1, h2, t2, p)

def main():
    client = InfluxDBClient(influx_host_ip, influx_host_port, influx_db)
    client.switch_database(influx_db)

    measurements_timer = RepeatedTimer(10, measurements, client)

    while(True):
        signal.pause()

if __name__ == '__main__':
    main()
