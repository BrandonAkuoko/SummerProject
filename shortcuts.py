# !/usr/bin/python3
# Brandon Akuoko
# October 21, 2021

import os
import subprocess
import os.path as p
from pathlib import Path

def code1():
        os.system("clear")
        home = p.expanduser("~")
        short = input("Please enter the file name to create a shortcut: ")
        try:
           pathfind,status = find_file(short) # should check and see if the file exist, if it does not then the excepetion should handle it
        except:
            print("Seaching, please wait...\n")
            print("Sorry, couldn't find " + '\033[31m' + short + '\033[0m' + "!\n Returning to Main Menu") 
            os.system("sleep 3")
            status = False # should never get to the while loop in this case
        while(status == True): # makes sure that this is executed if the status is true
            choice = input("Found "+ '\033[92m' + str(pathfind) + '\033[0m' + ". Select Y/y to create shortcut. ") # confirms the file was found
            if choice == "Y" or choice == "y":
                print("Creating Shortcut, please wait.\n")
                if check_link(short): # check to see if the link exist 
                    print("Symlink already exist, returning to Main menu")
                    #exit(1)
                print(pathfind) # want to check what is in here
                os.symlink(pathfind, home + "/" + short) # creates the symlink
                print("Shortcut created. Returning to Main Menu")
                status = False # status set to false ends loop
                #exit(1)
            else:
                print("\nYou entered an invalid option\n") # option bad try again

def code2():
    os.system("clear")
    remove = input("Please enter the shortcut you wish to remove:\t") # Removes the file 
    try:
        pathfind,status = find_file(remove) # two variables 
    except FileNotFoundError: #error handler 
        print("Seaching, please wait...\n")
        print("Sorry, couldn't find " + '\033[31m' + remove + '\033[0m' + "!\n Returning to Main Menu") 
    os.system("sleep 3")
        #break # subject to change
    while(1): # yes loop 
        choice = input("Are you sure you want to remove " + '\033[92m' + remove + '\033[0m' + "? Select Y/y to confirm.")
        if choice == "Y" or choice == "y":
            print("Removing link, please wait...\n")
            os.unlink(pathfind)
            os.system("sleep 2")
            print("Link removed, returning to Main Menu")
            os.system("sleep 3")
            #exit(1)
            break
        else:
            print("\nYou entered an invalid option!\n")

def code3():
    os.system("clear")
    home = p.expanduser('~') # home dir
    print("\033[92m" + "Shortcut Report" + "\033[0m" + "\n\n")
    print("Your current directory is " + '\033[93m' + home + "\033[0m" + ".\n\n")
    temp = sym_links(home) # checks to see if its a present symlink
    print("The number of symbolic links is " + '\033[93m' + str(len(temp)) + "\033[0m" + ".\n")
    print('\033[93m' + "Symbolic Link" + "\033[0m" + '\t\t' + '\033[93m' + "Target Path" + '\033[0m')
    for space in temp:
        print(space[0] + '\t\t' + space[1])
    print('\n')
    enter = input("To return to the Main Menu hit ENTER.")

def check_link(choice):
    for folder, subfolder, file in os.walk("/"):
		for f in file:
			filep = p.join(folder, f)
			if f == choice:
				if p.islink(filep):
					return True
    return False

def find_file(text):
    global pathfind
    for root, dirs, files in os.walk('/'): #walks through the system to find the file
        for file in files:
            if file == text: # if the file is found 
                pathfind = p.join(root, file) # path is joined
                return pathfind,True # when the file is found function returns true
    print("Seaching, please wait...\n")
    print("Sorry, couldn't find " + '\033[31m' + text + '\033[0m' + "!\n Returning to Main Menu")
    os.system("sleep 3") 

def sym_links(dir):
    global pathlist
    pathlist = []
    #home = p.expanduser('~')
    for root, dirs, files in os.walk(dir):
        for file in files:
            global lpath
            lpath = p.join(root, file)
            sl = []
            if p.islink(lpath): # if the link is already symlinked
                sl.append(file) # appends the file
                sl.append(os.readlink(lpath)) # also adds the file path to the list
                pathlist.append(sl)
    return pathlist # returns the list of paths and the links

def main():
    code = ""
    while code != "quit":
        os.system("clear")
        #Straight template text
        print("\t\033[92m" + "Shortcut Creater" + "\33[0m")
        print("\n Enter Selection:\n")
        print("\t1 - Create a shortcut in your home directory.")
        print("\t2 - Remove a shortcut from your home directory.")
        print("\t3 - Run shsortcut report.\n")
        code = input("Please enter a " + "\033[92m" + "number " + "\33[0m" +"or " + "\033[92m" + "'quit'" + "\33[0m" + " to quit the program: ")

    #How to kill the loop
        if code == "quit":
            print("Quitting Program")
            os.system("sleep 3")
            os.system("clear")
    #Adding shortcut 
        if code == "1":
            code1()   
    #Removing the link if there is one present 
        if code == "2":
            code2()
    #Running the shortcut report 
        if code == "3":
            code3()

main()     
