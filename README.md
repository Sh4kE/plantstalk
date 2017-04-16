

# Installation

* Change the path where to store the pictures in the plantstalk script
* Put something like this in your crontab:
    0 0 * * * /home/pi/bin/plantstalk.sh

# convert pictures to video like this:
```
cat *.png | ffmpeg -f image2pipe -i - 2017-04-13.mkv
```

