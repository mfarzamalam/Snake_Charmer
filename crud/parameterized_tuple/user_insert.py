import connect

    # Inserting multiple data in tuple format from USER
sql = "INSERT INTO student1(name,roll,fees) VALUES (%s,%s,%s)"
myc = connect.conn.cursor()
rows = 0

n = int(input("How many data you wanna enter?\n:"))
for i in range(n):
    name = input("Enter the name ?: ")
    roll = input("Enter the rollno ?: ")
    fees = input("Enter the fees ?: ")
    multiple_data = [(name,roll,fees)]
    try:
        myc.executemany(sql,multiple_data)
        print(myc.lastrowid,'is the last data inserted in the table')
        rows += myc.rowcount
        connect.conn.commit()
    except:
        connect.conn.rollback()
        print("unable to add data")
    
print(rows,'rows inserted')