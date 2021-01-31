sandwich_orders = ['pastrami','oregano','pepparoni','pastrami','campus','caflet','pastrami']
finisher_sandwiches = []

print("Sorry we've run out of pastrami")

while sandwich_orders:

    while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')
              
    finish = sandwich_orders.pop()

    print("Your order is : "+finish)

    finisher_sandwiches.append(finish)

# for finisher_sandwiche in finisher_sandwiches:
#     print("Your order for " +finisher_sandwiche +" sandwich is ready")

print(sandwich_orders)
print(finisher_sandwiches)