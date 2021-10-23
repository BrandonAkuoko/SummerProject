# !/usr/bin/python3
# Brandon Akuoko
# October 21, 2021

import os
import subprocess
import os.path as p
from pathlib import Path
#import netifaces

code = ""


home = os.path.expanduser("~")

while code != "quit":
    os.system("clear")
    print("\t\033[92m" + "Shortcut Creater" + "\33[0m")
    print("\n Enter Selection:\n")
    print("\t1 - Create a shortcut in your home directory.")
    print("\t2 - Remove a shortcut from your home directory.")
    print("\t3 - Run shsortcut report.\n")
    code = input("Please enter a " + "\033[92m" + "number " + "\33[0m" +"or " + "\033[92m" + "'quit'" + "\33[0m" + " to quit the program: ")

    # put in a separate function if you get the chance
#Creating the link if the file exist
    if code == "quit":
        print("Quitting Program")
        os.system("sleep 3")
        os.system("clear")
    if code == "1":
        global path
        os.system("clear")
        short = input("Please enter the file name to create a shortcut: ")
        try:
           for root, dirs, files in os.walk(short, topdown= True):
               for file in files:
                   if file == short:
                       path = p.join(root, file)
        except FileNotFoundError:
            print("Seaching, please wait...\n")
            print("Sorry, couldn't find " + '\033[31m' + short + '\033[0m' + "!\n Returning to Main Menu") 
            os.system("sleep 3")
        choice = input("Found "+ '\033[92m' + str(path) + '\033[0m' + ". Select Y/y to create shortcut. ")

        if choice == "Y" or choice == "y":
            print("Creating Shortcut, please wait.\n")
            if check_link(short):
                print("Symlink already exist, returning to Main menu")
                break
            os.symlink(path, home + "/" + short)
            print("Shortcut created. Returning to Main Menu")
            break
        else:
            print("\nYou entered an invalid option\n")
    
#Removing the link if there is one present 
    if code == "2":
        os.system("clear")
        remove = input("Please enter the shortcut you wish to remove:\t")
        try:
           for root, dirs, files in os.walk(short, topdown= True):
               for file in files:
                   if file == short:
                       path = p.join(root, file)
        except FileNotFoundError:
            print("Seaching, please wait...\n")
            print("Sorry, couldn't find " + '\033[31m' + short + '\033[0m' + "!\n Returning to Main Menu") 
        os.system("sleep 3")
        while(1):
            choice = input("Are you sure you want to remove " + '\033[92m' + remove + '\033[0m' + "? Select Y/y to confirm.")
            if choice == "Y" or choice == "y":
                print("Removing link, please wait...\n")
                os.unlink(path)
                os.system("sleep 2")
                print("Link removed, returning to Main Menu")
                os.system("sleep 3")
                break
            else:
                print("\nYou entered an invalid option!\n")
    
# Running the shortcut report 
    if code == "3":
        os.system("clear")
        print("\033[92m" + "Shortcut Report" + "\033[0m" + "\n\n")
        print("Your current directory is " + '\033[93m' + home + "\033[0m" + ".\n\n")
        symlink(home)
        print("The number of symbolic links is " + '\033[93m' + str(len(lPaths)) + "\033[0m" + ".\n")
        print('\033[93m' + "Symbolic Link" + "\033[0m" + '\t\t' + '\033[93m' + "Target Path" + '\033[0m')

        for space in lPaths:
            print(space[0] + '\t\t' + space[1])
        print('\n')
        enter = input("To return to the Main Menu hit ENTER.")

               

def check_link(choice):
	for folder, subfolder, file in os.walk("/"):
		for f in file:
			filep = os.path.join(folder, f)
			if f == choice:
				if os.path.islink(filep):
					return True
	return False


def symlink(directory):
    global lPaths
	lPaths = []
	for folder, subfolder, file in os.walk(directory) :
		# Get files
		for f in file :
			link = p.join(folder, f)
            global link
			links = []
			if p.islink(link):
				links.append(f)
				links.append(os.readlink(link))
				lPaths.append(links)