import connect

sql = "DELETE FROM student1 WHERE stid=%(id)s"
myc = connect.conn.cursor()
value = {'id':66}

try:
    myc.execute(sql,value)
    for k,v in value.items():
        row = v

    print("Row number",row,"has been deleted")
    connect.conn.commit()
except:
    connect.conn.rollback()
    print("Unable to delete")