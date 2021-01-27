active = True

while active != False:
    message = input("Press F to stop\n:")
    if message == 'F':
        active = False

odd = 0

while odd < 10:
    odd += 1
    if odd % 2 == 0:
        continue

    print(odd)