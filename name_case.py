person_name = "Eric"
message = "Hello " + person_name + " would you like to learn some python today?"

print(message)

print(message.title())
print(message.upper())
print(message.lower())

famous_person = "Albert Einstein"
quote = "A person who never made a mistake never tried anything new"

message = famous_person + " once said," + ' "' + quote.title() + '"'

print(message)

name = "\tName with spaces at both end\t"
print(name)

name = "\t Stripping left space \t"
print(name.lstrip())

name = "\t Stripping right space \t"
print(name.rstrip())

name = "\t Stripping both side of space \t"
print(name.strip())