        ## Integer 
# print("{}"              .format(10))
# print("{}  {}"          .format(10,20))     # space between two curly braces matters
# print("{0}"             .format(10))        # zero in curly braces is index
# print("{0} {1}"         .format(10,20))     # zero/one in curly braces show indexes
# print("{1} {0}"         .format(10,20))     # zero/one in curly braces show indexes as shown reverse
# print("{num1}"          .format(num1=50))
# print("{num1} {num2}"   .format(num1=25, num2=75))
# print("{num2} {num1}"   .format(num1=77, num2=88))
# print("{:d}"   .format(66))
# print("{0:d}"   .format(44))                   # zero represent the index
# print("{num:d}"   .format(num=21))
# print("{num:05d}"   .format(num=21))
# print("{num:+5d}"   .format(num=21))
# print("{num:<5d}"   .format(num=21))
# print("{num:>5d}"   .format(num=21))
# print("{num:*<5d}"   .format(num=21))
# print("{num:-^6d}"   .format(num=21))



        ## Float 
# print("{}"              .format(10.56))
# print("{}  {}"          .format(10.55,20.42))     # space between two curly braces matters
# print("{0}"             .format(10.77))           # zero in curly braces is index
# print("{0} {1}"         .format(10.82,20.443))    # zero/one in curly braces show indexes
# print("{1} {0}"         .format(10.76,20.991))    # zero/one in curly braces show indexes as shown reverse
# print("{num1}"          .format(num1=50.3))
# print("{num1} {num2}"   .format(num1=25.42, num2=75.81))
# print("{num2} {num1}"   .format(num1=77.66, num2=88.0112))
# print("{:f}"   .format(66))
# print("{0:f}"   .format(44.147))                   # zero represent the index
# print("{num:8f}"   .format(num=21.11))
# print("{num:+9.2f}"   .format(num=21.11))
# print("{num:>9.2f}"   .format(num=21.11))
# print("{num:<9.2f}"   .format(num=21.11))
# print("{num:*<9.2f}"   .format(num=21.11))
# print("{num:*>9.2f}"   .format(num=21.11))
# print("{num:*^9.2f}"   .format(num=21.11))



        ## String 
# print("{}"              .format("10.56"))
# print("{}  {}"          .format("10.55","20.42"))     # space between two curly braces matters
# print("{0}"             .format("10.77"))             # zero in curly braces is index
# print("{0} {1}"         .format("10.82","20.443"))    # zero/one in curly braces show indexes
# print("{1} {0}"         .format("10.76","20.991"))    # zero/one in curly braces show indexes as shown reverse
# print("{num1}"          .format(num1="50.3"))
# print("{num1} {num2}"   .format(num1="25.42", num2="My name"))
# print("{num2} {num1}"   .format(num1="77.66", num2="88.0112"))
print("{:s}"           .format("66"))
print("{0:s}"          .format("44.147"))               # zero represent the index
print("{num:8s}"       .format(num="21.11"))
print("{num:*<8}"      .format(num="hi"))
print("{num:*>8}"      .format(num="hi"))
print("{num:*^8}"      .format(num="hi"))
print("{num:*<8.3s}"   .format(num="Hellloooooo"))
print("{num:^8.2s}"    .format(num="hombareee"))


        ## All Combination
# print("Hi {}, My age is {}. I have {}rs in my wallet " .format("Patric", 27, 666.69))
print("{:,}" .format(12131231313121))
print("{:_}" .format(12131231313121))


        ## with variables
a = 67
b = 3
print("{:3.2%}" .format(a/b))

value = (10,20,30)
print("{0[0]} {0[1]} {0[2]}". format(value))

value = {'name':"Farzam", 'age':22}
print("{0[name]} {0[age]}". format(value))
print("{d[name]} {d[age]}". format(d=value))
print("{name} {age}". format(**value))