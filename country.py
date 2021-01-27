message = "How many countries have you visited? "
message += "Name a few\n"
message += "(Press F to Exit the program)\n:"
countries = []

while True:
    country = input(message)

    if country == 'F':
        break
    else:
        countries.append(country)

if len(countries) == 0:
    print("You've visited no country. Ghareeb")
elif len(countries) > 1:
    print("You've visited " +str(len(countries))+ " countries so far. Names are ")
else:
    print("You've visited only " +str(len(countries))+ " country. That is")

for country in countries:
    print(country.title())