import connect

sql = "DELETE FROM student1 WHERE stid=%s"
myc = connect.conn.cursor()
value = (64,)

try:
    myc.execute(sql,value)
    row = value[0]
    print("Row number",row,"has been deleted")
    connect.conn.commit()
except:
    connect.conn.rollback()
    print("Unable to delete")