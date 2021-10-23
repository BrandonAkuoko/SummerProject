#! /usr/bin/python3
# Script 3
# Tyler Padrao
# Octover 22nd, 2021

# Imports
import sys
import netifaces
import os
import subprocess
import time
import socket
import os.path
from pathlib import Path
from time import sleep

# Style class for text colors - ANSI codes
class style() :
	RED = '\033[31m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	UNDERLINE = '\033[04m'
	RESET = '\033[0m'

# Function for creating a shortcut in home directory
def create_shortcut() :
	# Clear window
	os.system('cls' if os.name == 'nt' else 'clear')
	# Get user's choice of file they want to create shortcut for
	choice = input("Please enter the file name to create a shortcut:\t")
	# Flag for while loop
	flag1 = True
	# Home path
	home = os.path.expanduser("~")
	# Check if file is valid
	if check_file(choice, "/") == True :
		# While flag is True
		while flag1 == True :
			# Input for Y/y and notify user of file path found
			choice1 = input("Found " + style.GREEN + str(filePath) + style.RESET + ". Select Y/y to create shortcut. " )
			# If choice is Y or y
			if choice1 == "y" or choice1 == "Y" :
				# Inform user
				print("Creating Shortcut, please wait.\n")
				# Check if link exists already
				if link_exists(choice) :
					# Inform user
					print("Symbolic Link already exists, returning to main menu.")
					break
				# Create symlink
				os.symlink(filePath, home + "/" + choice)
				# Inform user
				print("Shortcut created. Returning to Main Menu.")
				break;
			else :
				# Entered invalid option (not Y or y), loops again
				print("\nYou entered an invalid option!\n")
	else :
		# File is not found, exit to main menu
		print("Searching, please wait...\n")
		print("Sorry, couldn't find " + style.GREEN + choice + style.RESET + "!\nReturning to Main Menu")
	# Wait 3.5 seconds before going back to menu
	time.sleep(3.5)
	
# Function for removing a shortcut from home directory
def remove_shortcut() :
	flag1 = True
	# Home path of user
	home = os.path.expanduser("~")
	# Clear window
	os.system('cls' if os.name == 'nt' else 'clear')
	# Variable for saving user input of shortcut they want to remove
	choice = input("Please enter the shortcut/link to remove:\t")
	# Check if file is valid
	if check_file(choice, home) == True :
		# While flag is True
		while flag1 == True :
			# Double check if user wants to remove
			choice1 = input("Are you sure you want to remove " + style.GREEN + choice + style.RESET + "? Press " + style.GREEN + "Y/y " + style.RESET + "to confirm. ")	
			# If choice is Y or y
			if choice1 == "y" or choice1 == "Y" :
				# Inform user
				print("Removing link, please wait...\n")
				# Unlink symLink
				os.unlink(filePath)
				# Sleep for 2 seconds
				time.sleep(2)
				# Inform user
				print("Link removed, returning to Main Menu")
				# Sleep for 3.5 seconds
				time.sleep(3.5)	
				# Break out of loop
				break
			else :
				# Inform user option other than y or Y was entered
				print("\nYou entered an invalid option!\n")
	else :
		# Inform user that no symlink was found to remove based on file they entered
		print("\nSorry, couldn't find " + style.RED + choice + style.RESET + "!\nReturning to Main Menu")
		# Wait 3.5 seconds before going back to menu
		time.sleep(3.5)

# Function for running shortcut report
def run_report() :
	# Variable for home directory
	home = os.path.expanduser("~")
	# Clear window
	os.system('cls' if os.name == 'nt' else 'clear')
	# Inform user
	print(style.GREEN + "Shortcut Report" + style.RESET + "\n\n")
	print("Your current directory is " + style.YELLOW + home + style.RESET + ".\n\n")
	# Check if file is a sym link
	check_sym_links(home)
	# Inform user
	print("The number of symbolic links is " + style.YELLOW + str(len(linkPaths)) + style.RESET + ".\n")
	# Inform user
	print(style.YELLOW + style.UNDERLINE + "Symbolic Link" + style.RESET + "\t\t" + style.UNDERLINE + style.RESET + style.YELLOW + style.UNDERLINE + "Target Path" + style.RESET)
	# For loop to print sym links and target links
	for row in linkPaths :	
		print(row[0] + "\t\t" + row[1])
	# Inform user - when they hit enter, it brings them to main menu
	choice = input("\nTo return to the " + style.YELLOW + "Main Menu" + style.RESET + ", press " + style.YELLOW + "Enter." + style.RESET)
	
# Function for checking if link exists
def link_exists(fileName) :
	# Loop through folders, subfolders, and files in home directory
	for folder, subfolder, file in os.walk("/") :
		# Loop through files
		for f in file :
			# Get path of file
			pathOfFile = os.path.join(folder, f)
			# If file is already in directory
			if f == fileName :
				if os.path.islink(pathOfFile) :
					# Return True
					return True
	return False
				
# Function for checking if file is valid
def check_file(fname, directory) :
	# Global variable for file path
	global filePath
	# Loop for Checking folders, subfolders, and files
	for folder, subfolder, file in os.walk(directory) :
		# Loop through files
		for f in file :
			# If file is valid
			if f == fname :
				# Get file path
				filePath = os.path.join(folder, f)
				return True

# Function for checking if file is symlink and appending symLinks to list
def check_sym_links(directory) :
	# Global variable to store link paths
	global linkPaths
	linkPaths = []
	# Loop through folders, subfolders, and files
	for folder, subfolder, file in os.walk(directory) :
		# Get files
		for f in file :
			# Variable for singular link path
			global linkPath
			linkPath = os.path.join(folder, f)
			# List of all sym links
			symLinks = []
			# Check if link is symlink
			if os.path.islink(linkPath) :
				# Append file and file path
				symLinks.append(f)
				symLinks.append(os.readlink(linkPath))
				# Append sym link
				linkPaths.append(symLinks)

# Main function for menu loop
def main() :
	# Set flag to true for loop
	flag = True
	# While True
	while flag == True:
		# Clear window
		os.system('cls' if os.name == 'nt' else 'clear')
		# User interface for program
		print(style.GREEN + "\nShortcut Creator\n" + style.RESET)
		print("Enter Selection:\n")
		print("\t1 - Create a shortcut in your home directory.")
		print("\t2 - Remove a shortcut from your home directory.")
		print("\t3 - Run shortcut report.\n")
		# Grab user's input
		choice = input("Please enter a " + style.GREEN + "number (1-3) " + style.RESET + "or " + style.GREEN + "'Q/q'" + style.RESET + " to quit the program: ")
		# If choice is 1, create shortcut
		if choice == "1":
			create_shortcut()
			flag = True
		# If choice is 2, remove shortcut
		elif choice == "2":
			remove_shortcut()
			flag = True
		# If choice is 3, run shortcut report
		elif choice == "3":
			run_report()
			flag = True
		# If choice is Q or q, quit program
		elif choice == "Q" or choice == "q":
			# Clear window
			os.system('cls' if os.name == 'nt' else 'clear')
			# Inform user
			print("Quitting program: returning to shell.\n\n" + style.YELLOW + "Have a wonderful day!" + style.RESET)
			# Wait 3.5 seconds before going back to menu
			time.sleep(3.5)
			# Clear window
			os.system('cls' if os.name == 'nt' else 'clear')
			# Exit script
			sys.exit()
		# If user did not select one of the valid options, they have to reselect
		else:
			# Inform user
			print("\nYou entered an invalid option!\n\nPlease enter a number between 1 through 3")
			# Wait 3.5 seconds before going back to menu
			time.sleep(3.5)
			# Clear window
			os.system('cls' if os.name == 'nt' else 'clear')

# Call main function
main()

