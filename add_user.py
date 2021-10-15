# !/usr/bin/python3
# Brandon Akuoko
# October 13, 2021

import os
import csv
import pwd as p
import grp as g

def fileReader(file): #fileReader takes in a file that is opened and read and split based on line
    with open(file) as fp:
            read = csv.reader(fp.read().splitlines())
            next(read) #Skips the opening line of the file ex: EmployeeID, Last, First,etc...
            for line in read:
                # creates variables for each sub section of the csv file
                eid = line[0]
                last = line[1].lower()
                first = line[2].lower()
                number = line[4]
                office = line[3]
                department = line[5]
                group = line[6]
                password = "password"
                
                if(len(first) > 0):
                    name = first[0] + last
                name = name.replace("'", "")

                #checks if the user already exists and changes the name if it does
                for i in range(0, 15):
                    try:
                        p.getpwnam(name)
                        if(i == 0):
                            name = name + "1"
                        else:
                            name = name[:-1]
                            name = name + str(i + 1)
                    except KeyError:
                        break

                #checks if group exists and if it does not it adds the group
                try:
                    g.getgrnam(group)
                except KeyError:
                    os.system("sudo groupadd " + group)

                # Creates directory for each department e.g: /home/ceo/nrichardson
                directory = "/home/" + department.lower() + "/" + name

                shell = ""
                if(group == "office"): # Any member of office should use csh 
                    shell = "/bin/csh"
                else:
                    shell = "/bin/bash"

                if(eid != "" and last != "" and first != "" and department != ""):
                    print("Processing employee ID " + eid + "." + "\t\t" + "\33[92m" + name + "\33[0m" + " added to system.\n")
                    os.system("sudo mkdir -p " + directory)
                    os.system("sudo useradd " + name + " -g " + group + " --create-home --home-dir " + directory + " -s " + shell + " -p " + "password")
                    os.system("sudo chage -d 0 " + name)  # Expires the users password forcing them to change it upon creation
                    os.system("sleep 2")
                else:
                    print("Could not process employee ID " + eid + "." + "\t\t" + "\33[91m" + "Insufficient information" + "\33[0m" + ".")
                # add an elif to judge each part whether its empty or not
    read.close() # try and see if it actually closes
def main():
    os.system("clear")
    print("Adding users to the system\n")
    print("Please note: The defualt password for new users is" + "\33[92m" + " password" + "\33[0m" + ".\n")
    print("For testing purposes. Please change the password to" + "\33[92m" + " 1$4pizz@" + "\33[0m" + ".\n")
    file = "linux_users.csv"
    fileReader(file)

main()