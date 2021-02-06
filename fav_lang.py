from collections import OrderedDict
from random import randint

x = randint(1,6)
while x:
    print(x)

favourite_language = OrderedDict()

favourite_language['jen'] = 'python'
favourite_language['mike'] = 'c'
favourite_language['carol'] = 'c++'
favourite_language['james'] = 'java'

for name,lang in favourite_language.items():
    print("name " + name + " language " + lang)