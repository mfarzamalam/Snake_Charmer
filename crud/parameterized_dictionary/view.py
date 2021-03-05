import connect

sql = "SELECT * FROM student1 WHERE stid=%(id)s"
myc = connect.conn.cursor()
value = {'id':21}

try:
    myc.execute(sql,value)
    row = myc.fetchone()
    if row == None:
        print("No data in the database")
    else:
        print(row)
        print("Total rows fetched:",myc.rowcount)
    
    connect.conn.commit()
except:
    connect.conn.rollback()
    print("unable to retreive data")