#!/usr/bin/python


import sys
from lxml import html
import requests
import urllib2
from bs4 import BeautifulSoup

sList=[]
# Put address into a list so we can add + between spaces
adrList=raw_input("Please enter starting address   ").split()
sList.append("+".join(adrList)+',+')
# Do the same thing with city value in case there are two names
cityList=raw_input("Enter starting City   ").split()
sList.append("+".join(cityList)+",+")
# zip and state only have one entry
sList.append(raw_input("Enter starting State   ")+'+')
sList.append(raw_input("Enter starting Zip   ")+'/')
s_location=''.join(sList)

eList=[]
# Put address into a list so we can add + between spaces
adrList=raw_input("Please enter ending address   ").split()
eList.append("+".join(adrList)+',+')
# Do the same thing with city value in case there are two names
cityList=raw_input("Enter ending City   ").split()
eList.append("+".join(cityList)+",+")
# zip and state only have one entry
eList.append(raw_input("Enter ending State   ")+'+')
eList.append(raw_input("Enter ending Zip   "))
e_location=''.join(eList)


try:
    page = urllib2.urlopen('https://www.google.com/maps/dir/'+s_location+e_location)
except urllib2.HTTPError:
    print("seems like there is an error with one of your locations")
    exit()
else:
    # soup contains the HTML of the page
    soup = BeautifulSoup(page, 'html.parser')

# We have a working html file at this point
commute_time = soup.find("div", attrs={"span": "section-directions-trip-duration"})

#TODO this is returning 'None'
print("The fastest route according to google is ",commute_time)
