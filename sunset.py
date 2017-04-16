#!/usr/bin/python

import ephem

from datetime import datetime
from pytz import timezone

#Make an observer
berlin      = ephem.city("Berlin")
berlin_tz = timezone('Europe/Berlin')
utc_tz = timezone("UTC")

#Location of Berlin, Germany (Osloer Str. 77)
berlin.lon  = str(13.37)      #Note that lon should be in string format
berlin.lat  = str(52.56)      #Note that lat should be in string format

sunrise=berlin.previous_rising(ephem.Sun()) #Sunrise
noon   =berlin.next_transit   (ephem.Sun(), start=sunrise) #Solar noon
sunset =berlin.next_setting   (ephem.Sun()) #Sunset

print("sunrise (UTC): %s" % sunrise)
print("   noon (UTC): %s" % noon)
print(" sunset (UTC): %s" % sunset)

datetime_sunrise = ephem.localtime(sunrise)
datetime_noon = ephem.localtime(noon)
datetime_sunset = ephem.localtime(sunset)

print()

sunrise_local = datetime_sunrise.replace(tzinfo=berlin_tz)
noon_local = datetime_noon.replace(tzinfo=berlin_tz)
sunset_local = datetime_sunset.replace(tzinfo=berlin_tz)

print("sunrise (Berlin): %s" % sunrise_local.ctime())
print("   noon (Berlin): %s" % noon_local.ctime())
print(" sunset (Berlin): %s" % sunset_local.ctime())

#We relocate the horizon to get twilight times
#berlin.horizon = '-6' #-6=civil twilight, -12=nautical, -18=astronomical
#beg_twilight=berlin.previous_rising(ephem.Sun(), use_center=True) #Begin civil twilight
#end_twilight=berlin.next_setting   (ephem.Sun(), use_center=True) #End civil twilight

#print("begin twilight: %s" % beg_twilight)
#print("  end twilight: %s" % beg_twilight)
