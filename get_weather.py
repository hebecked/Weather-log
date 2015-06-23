#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
# A script by Dustin Hebecker

import WeatherStation
import time
import numpy as np
import os.path
import argparse
import fileinput
import sys

parser = argparse.ArgumentParser(description='This script is meant for the analysis of WLS absorbtion measurements.')
parser.add_argument('-ci', '--check-integrity', dest='CHECK', action='store_true', help='Check whether the output file contains all Data sets that are still left in the memory of the weather Station.', default=False)
parser.add_argument('-c', '--current', dest='CURRENT', action='store_true', help='Append current conditions to output file.', default=False)
parser.add_argument('-s', '--show', dest='SHOW', action='store_true', help='Show current conditions on standard output', default=False)
parser.add_argument('-p', '--path', dest='PATH', action='store', type="str", help='Defines where the log file is/will be stored. only valid with -ci and/or -c', default="weather.txt")

args = parser.parse_args()

if args.CURRENT or args.SHOW:

	wind_dirs=['N','NNE','NE','ENE','E','ESE','SE','SSE','S','SSW','SW','WSW','W','WNW','NW','NNW']

	ws = WeatherStation.weather_station()
	weather = ws.get_data(ws.current_pos(), True)

	ws_time = time.strptime(ws.get_fixed_block(['date_time'],True), "%Y-%m-%d %H:%M")
	pc_time = time.localtime()
	pc_month = time.strftime("%b");

	#compare times, print warning if offset is too big
	diff_time=np.fabs(time.mktime(pc_time)-time.mktime(ws_time))
	if( diff_time > 600 ):
		print "Warning:\nThe time difference between weather station and computer exceeds reasonable limits!!!"

	"Needs to adapt for summer and wintertime"

	weather_str = ( str(pc_time.tm_year) + "-" + str(pc_month) + "-" + str(pc_time.tm_mday).zfill(2) + " " + str(pc_time.tm_hour).zfill(2) + ":" + str(pc_time.tm_min).zfill(2) + ":" + str(pc_time.tm_sec).zfill(2) + " " + "CEST+2" + "   " + 
					str(weather['temp_in']) + " " + str(weather['temp_out']) + " " + str(WeatherStation.dew_point(weather['temp_out'],weather['hum_out'])) + " " + str(weather['hum_in']) + " " + str(weather['hum_out']) + " " + str(weather['wind_ave']) +
					" " + str(weather['wind_dir']) + " " + str(wind_dirs[int(weather['wind_dir']*16./360.)]) + " " + str(weather['wind_gust']) + " " + str(WeatherStation.wind_chill(weather['temp_out'], weather['wind_ave'])) + " " + str(weather['rain']) +
					" " + str(weather['abs_pressure']) + "\n"
				   )

	legend1 = "#date       time               T_i   T_a  Dewp    H_i  H_a     Wspd   Wdir  Wdir   Gust Chill     Rain   Pressure\n"
	legend2 = "#                              °C    °C    °C      %    %      m/s      °          m/s    °C       mm        hPa\n"
	if args.CURRENT:
		if not os.path.isfile(args.PATH):
			FILE = open(args.PATH,"w")
			FILE.write(legend1)
			FILE.write(legend2)
		else:
			FILE = open(args.PATH,"a")
		FILE.write(weather_str)
		FILE.close()

	if args.SHOW:
		print legend1
		print legend2
		print weather_str



if args.CHECK:
	sys.exit(0)# temporary solution until cross reference with logged data is implemented

	with open(args.PATH) as FILE:
	    lines = FILE.readlines()
	    if (len(lines) > 5):
	    	# get time line 12 len(lines)/2 len(lines)/2-1 and get minimal difference
	    	#get check interval of weather station
	    	#calculat how many matchin values should be stored.
	    	#read max values last entries from log
	    	# check if all consistent if not fetch corresponding values from station log and insert


	    	'''stile: 


	for line in fileinput.input('1.txt', inplace=1):
	 print line,
	 if line.startswith('foo1 bar3'):
	     print 'foo bar'
	'''
	#
