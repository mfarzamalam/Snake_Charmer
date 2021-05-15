        ### Maintain the order
print()
print("%d"    %432)
print("%d %d" %(432, 445))
print("%f"    %55.125)
print("%f %f" %(774.14, 556.81))
print("%f"    %55578.988)
print("%s"    %"Alfa red")
print("%s %s" %("alpha", "red"))
print("%d %s" %(55, "red"))


        ### No need to maintain order
print()
print("%(val1)s %(val2)d" %{'val1':"This is string", 'val2':22})


        ### With Flag, width and precision
print()
print("% d   Hello" %21)         # With a single space
print("%+d "  %21)               # With postive integer
print("%-d "  %21)               # With negative integer
print("%10d " %21)               # Number of space created for the value to store. we called it width
print("%010d" %771.66)           # Zeros created instead of space
print("%.1f"  %432.77)           # Specifing how many number of digits you need. we called it precision
print("%8.1f" %667.7889)         # Width with precision combined.