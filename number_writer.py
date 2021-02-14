import json

numbers = [2,3,4,5,6,7]

filename = 'numbers.json'

with open(filename) as f_obj:
    json.dump(numbers,f_obj)