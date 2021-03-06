a = 10
b = 10

try:
    d = a/b
    print("Try block:",d)
except:
    print("Except block: You cannot divide the number by Zero")
else:
    print("Else block")
finally:
    print("Final block")

print("Rest of the code")