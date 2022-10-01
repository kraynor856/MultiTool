from logging import error
from operator import not_
import os
import time
from turtle import clearscreen
from typing_extensions import Self
import keyboard
import pyfiglet
import subprocess
import mysql.connector 

mydb = mysql.connector.connect(
    host = "localhost",
    user= "root",
    password = ""
)

def clearscr():
    os.system('clear')


def help_screen():
    i = 2
    while i == 2:
        help = pyfiglet.figlet_format("help")
        print(help)
        print("This is the help screen")
   
    


def enter_option():
    input("Enter an option: ")


def nmap_instal():
    return (os.path.isfile("/usr/bin/nmap") or os.path.isfile("/usr/local/bin/nmap"))
def sql_instal():
   return (os.path.isfile("/usr/bin/sqlmap") or os.path.isfile("/usr/local/bin/sqlmap"))



def website_ping():
        host = input("Enter a hostname/url :")
        if os.system("ping" + " " + host) == 0:
            print("no error")
        else: 
            print("Error, Would you like to try that agian? y/n ")
            choice = input("Enter an option : ")
            if choice == "y": 
                website_ping()
            else:
                print("exiting....")

def aircrak_instal():
    return (os.path.isfile("/usr/bin/aircrack-ng") or os.path.isfile("/usr/local/bin/aircrack-ng"))

def simple_http():
    try:
       os.system("python2 -m SimpleHTTPServer 8000")
    except:
       print("There was an error, would you like to give that another go?")

def use_a_tool_nmap():
        select_tool_nmap = pyfiglet.figlet_format("Nmap!")
        print(select_tool_nmap)
        print("(1) Scan a network for open ports")
        print("(2) Preform an agressive scan on the target")
        use_tool_nmap = input("Enter an option : ")


def use_tool_screen():
   select_tool_nmap = pyfiglet.figlet_format("Select a Tool!")
   print(select_tool_nmap)
   print("(1) Nmap")
   use_tool = input("Enter a option :")
   if use_tool == "1":
      clearscr()
      use_a_tool_nmap()
    

class userinfo():
    def create_user(user):
        def __int__(user):
            username = input("Enter a username")
            email = input("Enter a  Email")
            pin = input("Enter a pin: ")

            user.username = username
            user.email = email
            user.pin = pin


def login_page():
    ascii_banner = pyfiglet.figlet_format("login")
    print(ascii_banner)
    print("New and dont have an account? press C, to make an account")
    username = input("Enter your username: ")
    pin = input("Enter your Pin: ")
    if username == "123" and pin == "123":
        Loggedin = True
        welcome_scren()
    else:
        print("User not found, please try again!")
        login_page()


def already_intalled():
    print("This tool is alread installed, would you like to go back? y/n")
    already_installed_input = input("Enter a Option: ")
    if already_installed_input == "y":
        tool_installation_screen()
    elif already_installed_input == "n":
        print("exiting ......")


class mainmenu:
    def __init__(self):
        menu = pyfiglet.figlet_format("Menu!")
        print(menu)
        print("(1) SSH")
        print("(2) Nmap scan")
        print("(3) Install Tools")
        print("(4) Use a tool")
        print("(5) Start a HTTP server ")
        print("(6) Ping a website")
        print("(7) Set wifi addapter to monitor mode")
        user_input = input("Enter an option: ")
        if user_input == "1":
            ssh_ip = input("Enter an IP:")
            ssh_host_name = input("Enter a hostname")
            print("Are these correct?" + " " +
                  ssh_host_name + " " + ssh_ip + " "+"y or n ")
            answer_ssh = input("Enter a choice :")
            if answer_ssh == "y" or "Y":
                os.system("ssh" + " " + ssh_host_name + "@" + ssh_ip)
        elif user_input == "3":
            clearscr()
            tool_installation_screen()
        elif user_input == "5":
             simple_http()
        elif user_input == "4":
           use_tool_screen()
        elif user_input == "6":
           website_ping()

def choice():
    print("Are you sure? y or n ")
    choice_input = input("Enter a choice: ")
    if choice_input == "y":
        print("exiting ..... ")
    elif choice_input == "n":
        mainmenu()


def welcome_scren():
    welcome = pyfiglet.figlet_format("Welcome!")
    print(welcome)
    print("(1) Main Menu")
    print("(2) Exit")
    print("(3) Help ")
    welcome_option = input("Enter a Option: ")
    if welcome_option == "1":
        mainmenu()
        clearscr()
    elif welcome_option == "2":
        choice()

    elif welcome_option == "3":
        help_screen()
        clearscr()


def tool_installation_screen():
    instal = pyfiglet.figlet_format("Install a tool!")
    print(instal)
    print("(1) NMAP")
    print("(2) Aircrack-ng")
    print("(3) Sqlmap ")
    print("(4) Back")
    tool_instalation = input("Choose a tool you want to install: ")
    if tool_instalation == "1":
        if nmap_instal():
            print("Nmap is already installed, would you like to go back ? y/n ")
            y = input("Enter an Option: ")
            if y == "y":
                tool_installation_screen()
            elif nmap_instal() == False:
                os.system("")
    elif tool_instalation == "2":
        if aircrak_instal():
            print("Aircrack is already installed, would you like to go back?")
            aircrack = input("Enter an option : ")
            if aircrack == "y":
                tool_installation_screen()
            else:
                print("exiting ..")
        elif tool_instalation == "4":
             welcome_scren()

        elif aircrak_instal == False:
            os.system("")
    elif tool_instalation == "3":
        if sql_instal():
            print("sqlmap is already installed, would you like to go back? y/n")
            sql_choice = input("Enter an option: ")
            if sql_choice == "y":
                tool_installation_screen()
            else:
                print("Exiting...")
        else: 
            os.system("")


# login_page()


welcome_scren()

# user_name()

#simple_http()