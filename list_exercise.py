print("I'm inviting the people for dinner. here's a list")

dinner_invitation = ['ali' , 'yaseen', 'shehroze']
print(dinner_invitation)
print("ali won't come")

dinner_invitation.remove('ali')
print(dinner_invitation)

print("We are invinting someone else in replacement of ali")
dinner_invitation.append('sabeen')
print(dinner_invitation)

print("Horray! We found a bigger table. Now it's time for party")
dinner_invitation.insert(0,'Shariq')
dinner_invitation.insert(2,'fawad')
dinner_invitation.append('aslam')

print(dinner_invitation)

print("Sorry. I just informed that big table is not availble. Only two person is allowed")

people_reject_1 = 'Shariq'
people_reject_2 = 'fawad'
people_reject_3 = 'yaseen'
people_reject_4 = 'shehroze'

dinner_invitation.remove(people_reject_1)
dinner_invitation.remove(people_reject_2)
dinner_invitation.remove(people_reject_3)
dinner_invitation.remove(people_reject_4)

rejection_apology = "Sorry. these people are not invited.\n" +people_reject_1+ "\n" +people_reject_2 + "\n" +people_reject_3+"\n"+people_reject_4
print(rejection_apology)

print("Only invited people are")
print(dinner_invitation)

print("Acually no-one is coming")
del dinner_invitation[0]
del dinner_invitation[0]
print(dinner_invitation)


###########################################

Travel = ['islamabad','turkey','moscow','istanbul','paris']
print("Places i wanna go:")
print(Travel)

print("\nList in alphabetical order using sorted function")
print(sorted(Travel))

print("\nlist in its orginal form")
print(Travel)

print("\nlist in reverse alphabetical order")
Travel.reverse()
print(Travel)

print("\nlist with its original order")
Travel.reverse()
print(Travel)

print("\nlist with sort function")
Travel.sort()
print(Travel)

print("\nlist with reverse sort function")
Travel.sort(reverse=True)
print(Travel)

print("\nPeople coming to my dinner")
print(len(dinner_invitation))