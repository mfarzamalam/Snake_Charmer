import connect

sql="SELECT * FROM student1 WHERE stid=%s"
myc = connect.conn.cursor()
value = (43,)

try:
    myc.execute(sql,value)
    row = myc.fetchone()
    print(row)
    print("Total rows:",myc.rowcount)
    connect.conn.commit()
except:
    connect.conn.rollback()
    print("unable to retrieve data")