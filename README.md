
# Plantstalk

Some scripts to use the raspberrypi camera for shooting images of basically anything, (e.g. a terrarium).

## Example images:

![At daytime](example_images/day.png "At daytime")


![At night](example_images/night.png "At night")


## Installation

* Change the path where to store the pictures in the plantstalk script
* Put something like this in your crontab: `0 0 * * * /home/pi/bin/plantstalk.sh`

## convert pictures to video like this:
```
cat *.png | ffmpeg -f image2pipe -i - 2017-04-13.mkv
```

