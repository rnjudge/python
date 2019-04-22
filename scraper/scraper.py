#!/usr/bin/python

import sys
from lxml import html
import requests

argcheck = len(sys.argv) - 1 
if argcheck < 1:
	print "You must provide a website to scrape"
	exit()
elif argcheck > 1:
	print "There are too many websites to scrape. Please only list one"
	exit() # exit for now. #TODO: collect info from terminal to re-enter only onewebsite
else:
	# sys.argv[1] is the website you want to scrape
	site = sys.argv[1]

print site
