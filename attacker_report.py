# !/usr/bin/python3
# Brandon Akuoko
# November 10, 2021

import os
import datetime as d
import re
from geoip import IPInfo, geolite2


os.system("clear") # Clears the terminal
date = d.datetime.now() # Gets the current date when this command is called
holder = {} # dictionaries best use for this because the keys cannot be repeated
print("\33[92m" + "Attacker Report - " + "\33[0m" + date.strftime("%B %d, %Y") + '\n') # Header for the attack report 
print("\33[91m" + "COUNT\t\tIP ADDRESS\t\tCOUNTRY" + "\33[0m" + '\n') #secondary header

with open("/home/student/scripts/script04/syslog.log") as file: # Reads the syslog 
    lines = file.readlines() # reads line for line in the syslog
    for line in lines:
        ip = re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})') # declaring the regex pattern for IP addresses
        if len(ip) != 0:
            temp = ip[0]
            if temp in holder: # if the ip is present in the holder
                holder[temp] += 1 # increases its count in the key 
            else:
                holder[temp] = 1 # only one log was notified by this ip
holder = sorted(holder.items(), key = lambda temp: temp[1], reverse=False) # sorts in ascending order
for temp in holder:
    if temp[1] >= 10: # Has to track for 10 or more fails
        lookup = geolite2.lookup(temp[1]) # is going to connect the ip to the country
        print(temp[1], '\t', temp[0], '\t', lookup.country)
