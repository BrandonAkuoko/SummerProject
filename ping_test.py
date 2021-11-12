#! /usr/bin/python3
# Brandon Akuoko
# September 16, 2021

import subprocess
import os
import netifaces

code = ""

while code != "quit":
	os.system("clear")
	print("\t Ping Test Troubleshooter")
	print("\n Enter Selection\n")
	print("\t1 - Test Connectivity to your gateway")
	print("\t2 - Test remote connectivity.")
	print("\t3 - Test for DNS resolution")
	print("\t4 - Display gateway IP address \n")

	code  = input("Enter a number (1-4) or Q/q to quit the program ")
	if code == "1":
		# If the input is 1 then the user will ping the default gateway 
		os.system("clear")
		print("Testing connectivity to your gateway...\n")
		os.system("sleep 4")
		test = subprocess.run(["ping","-c","1","192.168.2.254"],stdout = subprocess.DEVNULL)
		os.system("clear")
		print("Running test...\n")
		os.system("sleep 4")
		if test.returncode == 0:
			print("Ping was successful")
			os.system("sleep 3")
		else:
			print("Ping was unsuccess")
			os.system("sleep 4")
	elif code == "2":
		# if the user inputs 2 then the user will ping RIT's DNS
		os.system("clear")
		print("Testing remote connectivity...\n")
		os.system("sleep 4")
		test = subprocess.run(["ping", "-c", "1", "129.21.3.17"],stdout = subprocess.DEVNULL)
		if test.returncode == 0:
			print("Connectivity was successful")
			os.system("sleep 3")
		else:
			print("Connectivity was not successful")
			os.system("sleep 4")
	elif code == "3":
		#If the user inputs 3 then the user will ping the google url
		os.system("clear")
		print("Testing DNS connectivity...\n")
		os.system("sleep 4")
		test = subprocess.run(["ping", "-c", "1", "www.google.com"],stdout = subprocess.DEVNULL)
		if test.returncode == 0:
			print("DNS connectivity was successful")
			os.system("sleep 4")
		else:
			print("DNS connectivity was not successful")
			os.system("sleep 4")
	elif code == "4":
		# If the user inputs 4 then the users gateway IP will be displayed
		os.system("clear")
		gateway = netifaces.gateways()
		gateway = gateway["default"][netifaces.AF_INET][0]
		print("\nYour gateway IP address is " + gateway + ".")
		os.system("sleep 5")
		os.system("clear")
	elif code == "Q" or code == "q":
		#The user will quit the program
		os.system("clear")
		print("Good bye")
		code = "quit"
	else:
		# Any other input will run an invalid command print
		print("Invalid command")
		os.system("clear")

