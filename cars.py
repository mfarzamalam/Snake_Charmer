cars = ['bmw','audi','fraari']


print("All cars")
print(cars)

print("\nAlphabetic order")
cars.sort()     # Permenantly sort the order.
print(cars)

print("\nReverse Alphabetic order")
cars.sort(reverse=True)     # Permenantly sort the order.
print(cars)

cars = ['bmw','audi','fraari']

print("\nAlphabetic order but temporarily")
print(sorted(cars))     # Sorted function temporarily changed the order

print("\nAll cars")
print(cars)

print("\nReversing the order of the list")
cars.reverse()
print(cars)

print("\nReversing it again!")
cars.reverse()
print(cars)

print("\nlength of the list")
print(len(cars))
print(cars[-1])