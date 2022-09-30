from operator import not_
import os 
import time
from turtle import clearscreen
from typing_extensions import Self



def clearscr():
   os.system('clear')

def help_screen():
    print("This is the help screen")
 
def enter_option():
    input("Enter an option: ")

def nmap_instal():
           return (os.path.isfile("/usr/bin/nmap") or os.path.isfile("/usr/local/bin/nmap"))
    
def nmap_instal():
           return (os.path.isfile("/usr/bin/aircrack-ng") or os.path.isfile("/usr/local/bin/aircrack-ng"))
    


def already_intalled():
    print("This tool is alread installed, would you like to go back? y/n")
    already_installed_input = input("Enter a Option: ")
    if already_installed_input == "y":
        tool_installation_screen()
    elif already_installed_input == "n":
            print("exiting ......")


class mainmenu:
    def __init__(self):
        print("----------------MainMenu+++++++++++++++++")
        print("(1) SSH")
        print("(2) Nmap scan")
        print("(3) Install Tools")
        user_input = input("Enter an option: ")
        if user_input == "1":
            ssh_ip = input("Enter an IP:")
            ssh_host_name = input("Enter a hostname")    
            print("Are these correct?" + " "+ ssh_host_name + " " + ssh_ip +" "+"y or n ")
            answer_ssh = input("Enter a choice :")
            if answer_ssh == "y" or "Y":
                os.system("ssh" + " " +ssh_host_name +"@"+ ssh_ip )
        elif user_input == "3":
                clearscr()
                tool_installation_screen()
        elif user_input == "4":
               help_screen()
           


def choice():
    print("Are you sure? y or n ")
    choice_input= input ("Enter a choice: ")
    if choice_input == "y":
        print("exiting ..... ")
    elif choice_input == "n":
         mainmenu()


def welcome_scren():
    print("+++++++++++Welcome+++++++")#
    print("(1) Main Menu")
    print("(2) Exit")
    welcome_option = input("Enter a Option: ")
    if welcome_option == "1":
         mainmenu()
         clearscr()
    elif welcome_option == "2":
         choice()

    elif welcome_option == "3":
        tool_installation_screen()
        clearscr()



def tool_installation_screen():
            print("(1) NMAP")
            print("(2) Aircrack -ng" )
            tool_instalation = input("Choose a tool you want to install: ")
            if tool_instalation == "1":
             if nmap_instal():
                print("Nmap is already installed, would you like to go back ? y/n ")
                y = input("Enter an Option: ")
                if y == "y":
                    tool_installation_screen()
                elif nmap_instal () ==  False :
                   os.system("")




welcome_scren()

