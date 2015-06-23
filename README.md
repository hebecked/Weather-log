# Weather-log
A python programm to LOG and display weather data from a WH2080 Weather station (e.g. Conrad etc.)


dependencies:
python2
pip2
numpy
pyusb aka python-usb
libusb
cronie aka cron tab
git
sudo


todo:
creat script to auto load from cron
coppy rsa keys from old pc to new pi for transfer
change pull script
Time format UTC or localtime?
why CEST in winter?

Instructions on how to read out a CONRAD Weatherstation
-- by Dustin hebecker --

1. connect the weatherstation to you linux PC and run "lsusb", you should find a line like:
Bus 002 Device 007: ID 1941:8021 Dream Link WH1080 Weather Station / USB Missile Launcher
If your ID does not match to 1941:8021 please change the corresponding values in the WeatherStation.py script.

2. Make sure the above mentioned dependencies are ALL installed.


More information can be found here https://hess-confluence.desy.de/confluence/display/DESYAstroparticle/Trigger-Hodoskop+Software




The data must be formated as follows:

#date       time                                        Temperature_inside   Temperature_outside  Dewp/Dewpoint/Taumpunkt    H_i/humidity_inside  H_a/Humidity_outside     Wspd/Wind_speed   Wdir/wind_direction in degree  Wdir/wind_direction_in_words   Gust Chill/whatever?     Rain/(Expand rain in last hour and last 24h)   Pressure 
#                                                        °C    °C    °C      %    %      m/s      °          m/s    °C       mm        hPa 
2010-Jan-28 02:03:00 CEST+02   20.2  -3.2  -7.3     32   76      0.0  180.0  S     -1.00  -3.2     0.00   1024.400 