filename = 'programming_poll_response.txt'

while True:
    name = input("Tell me your name\n:")
    response = input("Tell me the reason why you like programming\n:")

    with open(filename,'a') as fileObject:
        fileObject.write("\n\nName:"+name + ",\nReason:"+response)

    end = input("Would you like to continue? Yes/No\n:")

    if end.lower() == 'no':
        break