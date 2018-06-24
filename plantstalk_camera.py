#!/usr/bin/python

import ephem
import time

from datetime import datetime, timedelta
from pytz import timezone
from picamera import PiCamera
from time import sleep

from RepeatedTimer import RepeatedTimer

# Berlin Timezone
berlin      = ephem.city("Berlin")
berlin_tz = timezone('Europe/Berlin')

def take_image():
    with PiCamera(resolution = (2592, 1944)) as camera:
        sleep(2)
        name = datetime.now().strftime('plants_%Y-%m-%d_%H-%M.jpg')
        camera.capture(name)

def get_sunrise():
    now = datetime.now()
    return ephem.localtime(berlin.next_rising(ephem.Sun(), start="{}/{}/{}".format(now.year, now.month, now.day)))

def get_sunset():
    now = datetime.now()
    return ephem.localtime(berlin.next_setting(ephem.Sun(), start="{}/{}/{}".format(now.year, now.month, now.day)))

def main():
    camera_timer = RepeatedTimer(60, take_image)

    while(True):
        if get_sunrise() < datetime.now() < get_sunset():
            camera_timer.start()
        else:
            camera_timer.stop()

        time.sleep(60)

if __name__ == '__main__':
    main()
