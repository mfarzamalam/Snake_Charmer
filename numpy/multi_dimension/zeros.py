from numpy import zeros

rows = int(input("How many rows do you need?\n:"))
columns = int(input("How many columns do you need?\n:"))

st_roll = zeros((rows,columns), dtype=int)


        ### Using For Loop

# for i in range(len(st_roll)):
#     for j in range(len(st_roll[i])):
#         print("Please enter the data for row",i,j)
#         col_data = int(input(":"))
#         st_roll[i][j] = col_data
#     print()

# for i in range(len(st_roll)):
#     for j in range(len(st_roll[i])):
#         print(str(i)+str(j)+": "+str(st_roll[i][j]))
#     print()



        ### Using While Loop

# i = 0
# while i < len(st_roll):
#     j = 0
#     while j < len(st_roll[i]):
#         print("Please enter the data for row",i,j)
#         col_data = int(input(":"))
#         st_roll[i][j] = col_data
#         j += 1
#     i+=1
#     print()

# i = 0
# while i < len(st_roll):
#     j = 0
#     while j < len(st_roll[i]):
#         print(str(i)+str(j)+": "+str(st_roll[i][j]))
#         j += 1
#     i += 1
#     print()