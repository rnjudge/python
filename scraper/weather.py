#!/usr/bin/python

import sys
from lxml import html
import requests
import urllib2
from bs4 import BeautifulSoup


# Make sure there is a location zip code to check 
argcheck = len(sys.argv) - 1
if argcheck < 1:
        print "You must provide a zipcode to check"
        exit()
elif argcheck > 1:
        print "There are too many zipcodes. Please only list one"
        exit() 
	#TODO: collect info from terminal to re-enter only one zipcode instead of exiting
else:
        zip = sys.argv[1]


page = urllib2.urlopen('https://weather.com/weather/hourbyhour/l/'+zip)
# soup contains the HTML of the page
soup = BeautifulSoup(page, 'html.parser')

weather = soup.find("td", attrs={"class": "temp"}).text
feels = soup.find("td", attrs={"class": "feels"}).text
city_banner = soup.find("div", attrs={"class": "locations-title"}).text
# Parse just the location and zip code from the locations-title:
# We want everything before the ')'
# TODO figure out how to save ')' from being cut
location = city_banner.split(")")[0]
time = soup.find("div", attrs={"class": "observation-timestamp"}).text

print "The current weather in",location + ") at",time + " is",weather + " but feels like",feels
