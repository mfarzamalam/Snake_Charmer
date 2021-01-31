responses={}

poll_active = True

while poll_active:

    name = input("Enter you name \n:")
    
    breakfast = input("Would you like to do breakfast? Yes/No\n:")
    if breakfast.lower() == 'yes' or breakfast.lower() == 'no':
        responses[name] = breakfast.lower()
    else:
        responses[name] = 'not answered'
    
    # lunch = input("Would you like to do lunch? Yes/No\n:")
    # if lunch.lower() == 'yes' or lunch.lower() == 'no':
    #     responses[name] = lunch
    # else:
    #     responses[name] = 'not answered'
    
    # dinner = input("Would you like to do dinner? Yes/No\n:")
    # if dinner.lower() == 'yes' or dinner.lower() == 'no':
    #     responses[name] = dinner
    # else:
    #     responses[name] = 'not answered'

    continueAgain = input("Would you like to do continue again? Yes/No\n:")
    if continueAgain.lower() == 'no':
        poll_active = False

for name,response in responses.items():
    print("Customer " +name + " say " +response + " to breakfast")