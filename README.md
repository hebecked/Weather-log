# Weather-log
A python program to LOG and display weather data from a WH2080 Weather station (e.g. Conrad etc.) in periodic intervals. 
For the lower level device handling a library by Jim Easterbrook is used.
The program is written by Dustin Hebecker


Instructions on how to read out a CONRAD Weatherstation or any WH2080 compatible station
-- by Dustin hebecker --

1. connect the weatherstation to you linux PC and run "lsusb", you should find a line like:
Bus XXX Device XXX: ID 1941:8021 Dream Link WH1080 Weather Station / USB Missile Launcher
If your ID does not match to 1941:8021 please change the corresponding values in the WeatherStation.py script.

2. Make sure the  dependencies are ALL installed:
python2
pip2
numpy
pyusb (aka python-usb)
libusb
cronie (any version of cron(tab))
git
sudo


More information can be found here https://hess-confluence.desy.de/confluence/display/DESYAstroparticle/Trigger-Hodoskop+Software


The data is formated as follows:

date       time                                        Temperature_inside   Temperature_outside  Dewp/Dewpoint/Taumpunkt    H_i/humidity_inside  H_a/Humidity_outside     Wspd/Wind_speed   Wdir/wind_direction in degree  Wdir/wind_direction_in_words   Gust Chill/whatever?     Rain/(Expand rain in last hour and last 24h)   Pressure 
                                                        °C    °C    °C      %    %      m/s      °          m/s    °C       mm        hPa 
2010-Jan-28 02:03:00 CEST+02   20.2  -3.2  -7.3     32   76      0.0  180.0  S     -1.00  -3.2     0.00   1024.400 


TODO:
create debugging and nicening script to auto load from cron