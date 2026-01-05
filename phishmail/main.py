import random
import webbrowser
from flask import Flask, render_template
from waitress import serve 
import sys


app = Flask(__name__)

logo = r"""

   ___ _     _     _                  _ _ 
  / _ \ |__ (_)___| |__   /\/\   __ _(_) |
 / /_)/ '_ \| / __| '_ \ /    \ / _` | | |  
/ ___/| | | | \__ \ | | / /\/\ \ (_| | | | 
\/    |_| |_|_|___/_| |_\/    \/\__,_|_|_|  
version 1.0.0                     __     |
                                \/  \    |
                                >= ) o>  J
                                /\__/
                                  /             
"""


colors = [
    '\033[91m', '\033[92m', '\033[93m',
    '\033[94m', '\033[95m', '\033[96m'
]

RESET = '\033[0m'

choice = None

data = {
    "name": "",
    "username": "",
    "email": "",
    "link": "",
    "template": "",
    "number_as_date": "",
    "day": "",
    "date": "",
    "month": "",  
    "year": "",
    "time": "",
    "city": "",
    "country": "",
    "ip" : "",
    "place" : "",
    "server" : ""
}

def print_logo():
    print(random.choice(colors) + logo + RESET)

def print_owner():
    print('\n [-] Tool Created by ScriptKiddie [-] \n ')

def print_menu():
    options = [
        "Instagram", "Facebook",
        "Gmail", "Discord",
        "PayPal", "RiotGames",
        "Steam"
    ]


    num = 1
    for i in range(0, len(options), 2):
        left = f"[{num}] {options[i]}".ljust(22)
        right = f"[{num+1}] {options[i+1]}" if i + 1 < len(options) else ""
        print(left + right)
        num += 2

    print("\n[0] Exit\n")

def safe_input(prompt):
    try:
        return input(prompt)
    except KeyboardInterrupt:
        print("\n[!] Program exited")
        sys.exit(0)
        
def input_not_empty(prompt):
    while True:
        value = safe_input(prompt).strip()
        if value:
            return value
        print("[!] This field cannot be empty.")


def input_digits(prompt):
    while True:
        value = safe_input(prompt).strip()
        if value.isdigit():
            return value
        print("[!] Numbers only allowed.")


def input_email(prompt):
    while True:
        value = safe_input(prompt).strip()
        if "@" in value and "." in value:
            return value
        print("[!] Invalid email format.")


def input_url(prompt):
    while True:
        value = safe_input(prompt).strip()
        if value.startswith("http://") or value.startswith("https://"):
            return value
        print("[!] URL must start with http:// or https://")


def input_year(prompt):
    while True:
        value = safe_input(prompt).strip()
        if value.isdigit() and len(value) == 4:
            return value
        print("[!] Enter a valid year (YYYY).")


def input_text(prompt):
    while True:
        value = safe_input(prompt).strip()
        if value.replace(" ", "").isalpha():
            return value
        print("[!] Letters only allowed.")

def handle_choice(user_choice):
    global choice
    choice = user_choice

    if choice == "0":
        print("\n Exiting...\n")
        exit()

    if choice == "1":
        data["template"] = "instagram.html"
        data["name"] = input_not_empty("\n[+] Enter Target Name: ")
        data["username"] = input_not_empty("[+] Enter Target Username: ")
        data["email"] = input_email("[+] Enter Target Email: ")
        data["link"] = input_url("[+] Enter Phishing URL: ")

        print("[+] Template ready")
        webbrowser.open("http://127.0.0.1:8080")
        print("[+] Enter  ^ + C to stop the server and exit.")



    elif choice == "2":
        data["template"] = "facebook.html"
        data["name"] = input_not_empty("\n[+] Enter Target Name: ")
        data["email"] = input_email("[+] Enter Target Email: ")
        data["link"] = input_url("[+] Enter Phishing URL: ")
        data["number_as_date"] = input_digits("[+] Enter a number as date: ")

        months = [
            "January", "February", "March", "April",
            "May", "June", "July", "August",
            "September", "October", "November", "December"
            ]

        print("\n[+] Enter Month Login Happened: \n")

        for idx, month in enumerate(months, start=1):
            print(f"[{idx}] {month}")

        month_choice = safe_input("\n[+] Month => ").strip()

        if month_choice.isdigit() and 1 <= int(month_choice) <= 12:
            data["month"] = months[int(month_choice) - 1]
        else:
            print("[!] Invalid month choice, defaulting to January.")
            data["month"] = "January"

        data["year"] = input_year("[+] Enter Year : ")
        data["time"] = input_not_empty("[+] Enter Time (Example, 10:30 pm/am): ")
        data["city"] = input_text("[+] Enter name of City: ")
        data["country"] = input_text("[+] Enter name of Country: ")

        
        print("[+] Template ready")
        webbrowser.open("http://127.0.0.1:8080")

        print("[+] Enter  ^ + C to stop the server and exit. ")

    elif choice == "3":
        data["template"] = "gmail.html"
        data["name"] = input_not_empty("\n[+] Enter Target Name: ")
        data["email"] = input_email("[+] Enter Target Email: ")
        data["day"] = input_not_empty("[+] Enter Day ex.Monday: ")
        data["date"] =input_not_empty("[+] Enter Date (Example, 01/03): ")
        data["year"] = input_year("[+] Enter Year : ")
        months = [
            "January", "February", "March", "April",
            "May", "June", "July", "August",
            "September", "October", "November", "December"
            ]

        print("\n[+] Enter Month Login Happened: \n")

        for idx, month in enumerate(months, start=1):
            print(f"[{idx}] {month}")

        month_choice = safe_input("\n[+] Month => ").strip()

        if month_choice.isdigit() and 1 <= int(month_choice) <= 12:
            data["month"] = months[int(month_choice) - 1]
        else:
            print("[!] Invalid month choice, defaulting to January.")
            data["month"] = "January"

        data["country"] = input_text("[+] Enter name of Country: ")
        data["city"] = input_text("[+] Enter name of City: ")
        data["link"] = input_url("[+] Enter Phishing URL: ")
        print("[+] Template ready")
        webbrowser.open("http://127.0.0.1:8080")  
        print("[+] Enter  ^ + C to stop the server and exit.")  
    
    elif choice =="4":
    
        data["template"] = "discord.html"
        data["name"] = input_not_empty("\n[+] Enter Target Name: ")
        data["link"] = input_url("[+] Enter Phishing URL: ")
        data["ip"] = input_not_empty("[+] Type a random IP-adress (Example, 192.168.0.15 ): ")
        data["place"]=input_not_empty("[+] type a  County And City (Example, Germany Eutin) :")
        print("[+] Template ready")
        webbrowser.open("http://127.0.0.1:8080")
        print("[+] Enter  ^ + C to stop the server and exit.")
    
    elif choice == "5":

        data["template"] = "paypal.html"
        data["link"] = input_url("[+] Enter Phishing URL: ")
        data["ip"] = input_not_empty("[+] Type a random IP-adress (Example, 192.168.0.15 ): ")
        data["place"]=input_not_empty("[+] type a  County And City (Example, Germany Eutin) :")
        print("[+] Template ready")
        webbrowser.open("http://127.0.0.1:8080")
        print("[+] Enter  ^ + C to stop the server and exit.")
    
    elif choice == "6":
        data["template"] = "riotgames.html"
        data["name"] = input_not_empty("\n[+] Enter Target Name: ")
        data["link"] = input_url("[+] Enter Phishing URL: ")
        print("\n[+] Pick A Server Your Target Is Having His RiotGames Account On:\n")
        server_options = [
            "Brazil (BR)",
            "Europe Nordic & East (EUNE)",
            "Europe West (EUW)",
            "Latin America North (LAN)",
            "Latin America South (LAS)",
            "North America (NA)",
            "Oceania (OCE)",
            "Russia (RU)",
            "Japan (JP)",
            "Turkey (TR)",
            "Republic of Korea (KR)"
        ]

        for idx, server in enumerate(server_options, start=1):
            print(f"[{idx}] {server} ")

        server_choice = safe_input("\n[+] Server =>\n").strip()

        if server_choice.isdigit() and 1 <= int(server_choice) <= len(server_options):
            data["server"] = server_options[int(server_choice) - 1]
        else:
            print("[!] Invalid server choice.")

        data["ip"] = input_not_empty("[+] Type a random IP-adress (Example, 192.168.0.15 ): ")
        data["place"]=input_not_empty("[+] type a  County And City (Example, Germany Eutin) :")
        print("[+] Template ready")
        webbrowser.open("http://127.0.0.1:8080")
        print("[+] Enter  ^ + C to stop the server and exit.")

    if choice == "7":
        data["template"] = "steam.html"
        data["name"] = input_not_empty("\n[+] Enter Target Username: ")
        data["place"]=input_not_empty("[+] type a  County And City (Example, Germany Eutin) :")
        data["link"] = input_url("[+] Enter Phishing URL: ")
        print("[+] Template ready")
        webbrowser.open("http://127.0.0.1:8080")
        print("[+] Enter  ^ + C to stop the server and exit.")

@app.route("/")
def index():
    views = {
        "1": (
            data["template"],
            {
                "name": data["name"],
                "username": data["username"],
                "email": data["email"],
                "link": data["link"]
            }
        ),
            "2": (
                data["template"],
                {
                    "name": data["name"],
                    "email": data["email"],
                    "link": data["link"],
                    "number_as_date": data["number_as_date"],
                    "month": data["month"],
                    "year": data["year"],
                    "time": data["time"],
                    "city": data["city"],
                    "country": data["country"]
                }
            ),
            "3": (
                data["template"],
                {
                    "name": data["name"],
                    "email": data["email"],
                    "link": data["link"],
                    "day": data["day"],
                    "date": data["date"],
                    "month": data["month"],
                    "year": data["year"],
                    "time": data["time"],
                    "city": data["city"],
                    "country": data["country"]
                }
            ),
            "4": (
                data["template"],
                {
                    "name": data["name"],
                    "link": data["link"],
                    "ip": data["ip"],
                    "place": data["place"]
                }
            ),
            "5": (
                data["template"],
                {
                    "link": data["link"],
                    "ip": data["ip"],
                    "place": data["place"]
                }
            ),
            "6": (
                data["template"],
                {
                    "name": data["name"],
                    "link": data["link"],
                    "server": data["server"],
                    "ip": data["ip"],
                    "place": data["place"]
                }
            ),
            "7": (
                data["template"],
                {
                    "name": data["name"],
                    "link": data["link"],
                    "place": data["place"]
                }
            )

        }

    if choice not in views:
        return "<h2>No template selected</h2>"

    template, context = views[choice]
    return render_template(template, **context)


if __name__ == "__main__":
    print_logo()
    print_owner()
    print_menu()

    user_choice = safe_input("=> Select an option: ").strip()
    handle_choice(user_choice)

    try:
        serve(app, host='0.0.0.0', port=8080)

    except KeyboardInterrupt:
        print("[!] Program exited")
        sys.exit(0)


__version__ = "1.0.0"
__author__ = "ScriptKiddie"