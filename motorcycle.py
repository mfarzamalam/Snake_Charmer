motorcycle = ['honda' , 'yamaha' , 'suzuki']
print(motorcycle)

motorcycle[0] = "harley davidson"
print(motorcycle)

motorcycle.append('ducati')
print(motorcycle)

cars = []
cars.append('first-car')
cars.append('second-car')
cars.append('third-car')

print(cars)

cars.insert(0,'zero-car')
print(cars)

del cars[2]     # Remove the item permenantly
print(cars)

popped_cars = cars.pop(1)   # Remove the item and save it into the new varaible for future use.
print(cars)
print(popped_cars)

RR = "My " + popped_cars + " was stolen four years back"
print(RR)
print(motorcycle)

Select_any_bike = "Please select any one of the bike available here " +str(motorcycle)
print(Select_any_bike)

bike_selection = 'harley davidson'
motorcycle.remove(bike_selection)


motorcycle_selected = "\nGonna buy " + bike_selection.title()
print(motorcycle_selected)

Success = "\nHere you go " + str(motorcycle)
print(Success)