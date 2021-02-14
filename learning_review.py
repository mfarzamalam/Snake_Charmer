filename = 'learning_python.txt'

with open(filename) as fileData:
    value = fileData.read()
    # print(value)

# print()

with open(filename) as fileData:
    lines = fileData.readlines()

content = ''

for line in lines:
    # print(line.strip())
    pass

for line in lines:
    content += line

replaceContent = content.replace('php','python')
print(replaceContent)