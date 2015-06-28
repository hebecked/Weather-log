#! /usr/bin/env python

from distutils.core import setup
import os

setup(name='Weather-log',
      version='1.0',
      url='https://github.com/hebecked/Weather-log',
      download_url="git clone https://github.com/hebecked/Weather-log",

      description='A simple weather logger for (WH2080) weather stations',
      long_description='',
      author='Dustin Hebecker',
      author_email="dustin.hebecker@desy.de",
      license="GPL",

      install_requires=['numpy','pyusb'],

      scripts=['bin/get_weather'], #'bin/schedule_weather_log'], #stand alone scripts (binarys will be placed in python executable folder)
      packages=['WeatherStation'], # folders with __init__.py that provides "package explanation string" (only packages that are to be imported)
      #py_modules=['foo'], # if there are only single files
      )


