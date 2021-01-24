for value in range(2,59,10):
    print(value)


number = list(range(1,6))
print(number)

even_numbers = list(range(2,11,2))
print(even_numbers)

squares = []

for value in range(1,11):

    squares.append(value**2)

print(squares)
print(min(squares))
print(max(squares))
print(sum(squares))

million = [value for value in range(1,1000001)]

#print(million)     print value from 1 to million
print(min(million))
print(max(million))
print(sum(million))

for value in range(1,21,2):
    print(value)

multiples = []
for multiple in range(3,31):
    multiple = multiple**3

    multiples.append(multiple)

print(multiples)

for cube in range(1,11):
    cube = cube ** 3

    print(cube)

cubes = [cube ** 3 for cube in range(1,11)]
print(cubes)