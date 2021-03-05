import connect 

sql="UPDATE student1 SET name=%s,fees=%s WHERE stid=%s"
myc = connect.conn.cursor()
value = ("shahid",6000,43)

try:
    myc.execute(sql,value)
    row = value[2]
    print("Row",row,"has been updated successfully")
    connect.conn.commit()
except:
    connect.conn.rollback()
    print("Failed to update data")