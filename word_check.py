def check_word(filename,word):
    """Creating a function that check how many words are in a file"""

    try:
        with open(filename) as f_obj:
            f_con = f_obj.read()
    except:
        print("file "+filename + " not found")

    else:
        """splitting the words in a list"""
        words_split = f_con.split()

        """calculating how many words are there"""
        words_verify = len(words_split)

        """calculating how many times a single word or words appear in the file"""
        word_repeat = f_con.lower().count(word)

        """printing the result"""
        print("The "+filename+ " has "+str(words_verify)+ " words. The word '"+word+"' repeats "+str(word_repeat)+ " times")


"""taking a empty list of files and words"""
filename = []
words = []
print("(press 'q' to quit asking)")


"""Asking the files to check"""
while True:

    files = input("File-name: ")
    if files.lower() == 'q':
        break
    else:
        filename.append(files)


"""Asking the word or words to check"""
while True:

    word = input("Word to look: ")
    if word.lower() == 'q':
        break
    else:
        words.append(word)


"""Generating the result using a for-loop"""
for files in filename:
    for word in words:
        check_word(files,word)