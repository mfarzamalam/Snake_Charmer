import connect

sql = "DELETE FROM student WHERE stid=11"
myc = connect.conn.cursor()

try:
    myc.execute(sql)

    connect.conn.commit()
    print(myc.rowcount,'row has been deleted')
except:
    connect.conn.rollback()
    print("Unable to delete data")
    
myc.close()