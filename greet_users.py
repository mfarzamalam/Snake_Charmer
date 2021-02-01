# def greeting_people(persons):
#     for person in persons:
#         print("Welcome "+person.title())

# people = ['ali','arawat','asfar','akmal','akib']

# greeting_people(people)

# def designs_order(request_designs,completed_designs):
#     while request_designs:
#         one_design = request_designs.pop()

#         print("Order to print is :"+one_design)
#         completed_designs.append(one_design)

# def complete_design(completed_designs):
#     for complete_design in completed_designs:
#         print("Following designs are ready :"+complete_design.title())

# request = ['iphone case', 'robot pendant', 'dodecahedron']
# complete = []

# designs_order(request[:],complete)     #We use[:] to pass a copy of list to function
# complete_design(request)


########################################################

def show_magician(magicians,great):
    while magicians:
        magician = magicians.pop()
        print("Welcome to the circus lord "+magician.title())
        make_great(magician)
        great.append(magician)

def make_great(magician):
    print("Great "+magician.title())

magicians = ['alex','mike','carol','rick','grimes']
great = []

show_magician(magicians[:],great)

print(magicians)
print(great)