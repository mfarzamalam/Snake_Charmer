filename = 'alice.txt'

try:
    with open(filename) as f_obj:
        f_content = f_obj.read()
        # print(f_content)
except:
    with open(filename,'w') as f_obj:
        f_content = f_obj.write("Just created")
        print(f_content)

words = f_content.split()
num_words = len(words)
print("The file "+filename+ " has "+str(num_words)+ " words")    