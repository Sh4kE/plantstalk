
# Plantstalk

Some scripts to use the raspberrypi camera for shooting images of basically anything, (e.g. a terrarium).

## Example images:

![At daytime](example_images/daytime.png "At daytime")


![At night](example_images/nighttime.png "At night")

## convert pictures to video like this:
```
cat *.png | ffmpeg -f image2pipe -i - 2017-04-13.mkv
```

