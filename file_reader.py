filePath = 'pi_digit.txt'

with open('pi_digit.txt') as f:
    read = f.read()
    print(read)

print()

with open(filePath) as fileContent:
    lines = fileContent.readlines()

for line in lines:
    print(line.rstrip())