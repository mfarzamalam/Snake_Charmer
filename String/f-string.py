        ### Integer

a1 = 10
b1 = 20

print(f"{a1}")
print(f"{a1} {b1}")

num = 15
print(f"{num} ")
print(f"{num:d} ")
print(f"{num:5d} ")
print(f"{num:05d} ")
print(f"{num:+5d} ")
print(f"{num:<5d} ")
print(f"{num:>5d} ")
print(f"{num:^<5d} ")
print(f"{num:^>5d} ")
print(f"{num:*^6d} ")



        ### Float
print()
a2 = 10.22
b2 = 20.11

print(f"{a2}")
print(f"{a2} {b2}")

num = 15.12313123123
print(f"{num} ")
print(f"{num:f} ")
print(f"{num:7.3f} ")
print(f"{num:.2f} ")
print(f"{num:+5.1f} ")
print(f"{num:<9.2f} ")
print(f"{num:>9.2f} ")
print(f"{num:^<7.2f} ")
print(f"{num:^>7.2f} ")
print(f"{num:*^7.3f} ")



        ### String
print()
a3 = "Hi"
b3 = "Bitcoin"

print(f"{a3}")
print(f"{a3} {b3}")

name = "ChinnarSwamiMuttarSwaamiVenuGupaarAyyyer"
print(f"{name} ")
print(f"{name:s} ")
print(f"{name:.20s}..... ")
print(f"{name:<5s} ")
print(f"{name:>5s} ")
print(f"{name:*>12.4s} ")
print(f"{name:*<12.4s} ")
print(f"{name:*^12.4s} ")

print()
price = 50000000000
print(f"{price:,} ")
print(f"{10*8}")
print(f"{a1/b1:.2%} ")

value = (10,20,30)
print(f"{value[0]} ")
print(f"{name.upper()} ")