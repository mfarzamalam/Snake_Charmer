import connect

sql1 = 'INSERT INTO student(name,roll,fees) VALUES ("sam",544,150.21)'
sql2 = "SELECT * FROM student"
myc = connect.conn.cursor()

try:
    myc.execute(sql2)
    for values in myc:
        print(values)
        pass
    print(myc.rowcount,'rows has been fetched')     # number of row fetched from table

    connect.conn.commit()       # commting the change
    print(myc.lastrowid)        # showing the number of last data insert in the table
except:
    connect.conn.rollback()     # rollback the change if it's not successful
    print("Unable to fetch data of table")

myc.close()