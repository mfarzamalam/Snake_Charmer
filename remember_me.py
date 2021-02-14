import json

def get_stored_username():
    try:
        filename = 'username.json'
        with open(filename) as f_obj:
            username = json.load(f_obj)
        return username
    except:
        return None

def get_new_username():
    filename = 'username.json'
    username = input("What is your name?\n:")
    with open(filename,'w') as f_obj:
        json.dump(username,f_obj)
    return username

def greet_user():
    username = get_stored_username()
    if username:
        print("Welcome back "+username)
        confirm = input("Would you like to change the username? Y/N\n:")
        if confirm.lower() == 'y':
            username = get_new_username()
        else:
            print("Aight, "+username+". Whatever you want")
    else:
        username = get_new_username()
        print("Welcome "+username)
    
greet_user()