import connect

sql = "SELECT * FROM student"
myc = connect.conn.cursor()

myc.execute(sql)
try:
    row = myc.fetchone()    # fetch only one data
    # row2 = myc.fetchall()   # fetch all data
    # row3 = myc.fetchmany(6)   # fetch selected data of my choice

    while row is not None:
        name = row[1]
        rollno = row[2]
        fees = row[3]
   
        print(name,rollno,fees)
        row = myc.fetchone()
        
    print(myc.rowcount,'row has been fetched')
    connect.conn.commit()
except:
    connect.conn.rollback()