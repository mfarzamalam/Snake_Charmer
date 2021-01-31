unconfirm_users = ['alice','brian','carol','laura','steve']
confirm_users = []

while unconfirm_users:
    user = unconfirm_users.pop()

    print("Confirming user : " +user.title())

    confirm_users.append(user)

print("These users are confirmed")

for confirm_user in confirm_users:
    print(confirm_user.title())