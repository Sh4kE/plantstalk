#!/usr/bin/python

import signal
import Adafruit_DHT
import Adafruit_BMP.BMP085 as BMP085

from influxdb import InfluxDBClient
from RepeatedTimer import RepeatedTimer

## BMP180 Sensor ##
bmp_sensor = BMP085.BMP085()

## DHT22 Sensor ##
dht_sensor = Adafruit_DHT.DHT22
gpio_input_pin = 19

## InfluxDB ##
influx_host_ip = '192.168.178.29'
influx_host_port = 8086
influx_db = 'plantstalk'
json_body = [
    {
        "measurement": "plantstalk",
        "fields": {
            "temperature": 0.0,
            "humidity": 0.0,
            "pressure": 0.0,
        }
    }
]

def measure():
    humidity, temperature = Adafruit_DHT.read_retry(dht_sensor, gpio_input_pin)
    pressure = bmp_sensor.read_pressure()
    if not humidity or not temperature:
        return measure()
    return humidity, temperature, pressure

def send_measurements(client, humidity, temperature, pressure):
    json_body[0]['fields']['temperature'] = temperature
    json_body[0]['fields']['pressure'] = pressure
    if 0 <= humidity <= 100:
        json_body[0]['fields']['humidity'] = humidity
    else:
        json_body[0]['fields'].pop('humidity', 0)
    ret = client.write_points(json_body)

def measurements(client):
    humidity, temperature, pressure = measure()
    send_measurements(client, humidity, temperature, pressure)

def main():
    client = InfluxDBClient(influx_host_ip, influx_host_port, influx_db)
    client.switch_database(influx_db)

    measurements_timer = RepeatedTimer(10, measurements, client)

    while(True):
        signal.pause()

if __name__ == '__main__':
    main()
