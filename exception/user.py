# User Defined Exception

class UserDefinedException(Exception):
    pass


def checkbalance():
    money = 10000
    withdraw = 9000
    balance = money - withdraw
    if balance <= 2000:
        raise UserDefinedException('Insufficient Balance')
    else:
        print("You've currently the balance of "+str(balance)+"rs")
try:
    checkbalance()
    
except UserDefinedException as UDE:
    print(UDE)