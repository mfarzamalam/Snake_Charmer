import json

filename = 'username.json'

name_check = input("What is your name?:\n")

with open(filename) as f_obj:
    username = json.load(f_obj)
    print("Welcome "+username)