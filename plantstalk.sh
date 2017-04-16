#!/bin/bash

DATE=$(date +%Y-%m-%d)
mkdir /mnt/Bilder/RaspiTerrarium/$DATE
raspistill -o /mnt/Bilder/RaspiTerrarium/$DATE/plants_%04d.png -e png -tl 20000 -t 86400000
