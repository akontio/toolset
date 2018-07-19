import os
import sys
import socket


def main():
        print("{run as sudo/root for all features to work 
properly}")
        print("Welcome to the main menu")
        print("Select an option using the corresponding number")
        print("\n\n")
        print("[1] nmap scan")
        print("[2] aquatone automated")
        print("[3] sqlmap scan")
        print("[4] reverse shell creation")
        input("make a selection: ")

def sqlmap():
        print("sqlmap main menu")
        print("[0] install sqlmap")
        print("[1] Set URL")
        print("[2] retrieve databases")
        print("[3] select database")
        print("[4] retrieve tables")
        print("[5] select table")
        print("[6] dump columns")
        print("[7] return to main menu")
        print("\n")
        choice = input("make a selection: ")
        if choice = 0 or "0":
                system = os.path.isfile("/usr/bin/pacman")
                if system = True or "True":
                        os.system("sudo pacman -S sqlmap")
                        sqlmap()
                elif system = False or "False":
                        system2 = os.path.isfile("/usr/bin/apt")
                        if system2 = True or "True":
                                os.system("sudo apt-get install 
sqlmap")
                                sqlmap()
                        elif system2 = False or "False":
                                system3 = 
os.path.isfile("/usr/bin/yum")
                                if system3 = True or "True":
                                        os.system("sudo yum 
install sqlmap")
                                        sqlmap()










main()
