def word_count(filename):
    try:
        with open(filename) as f_obj:
            f_content = f_obj.read()
            # print(f_content)
    except:
        print("Sorry the file x"+filename +" doesnot exist")
    else:        
        words = f_content.split()
        num_words = len(words)
        print("The file "+filename+ " has "+str(num_words)+ " words")


filenames = ['sandwich.py','user.py','vacation.py','topping.py','alice.txt']

for filename in filenames:
    word_count(filename)