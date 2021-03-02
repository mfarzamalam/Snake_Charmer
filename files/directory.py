import os

w = os.walk('.')    # to search in current directory
for i in w:
    print(i)