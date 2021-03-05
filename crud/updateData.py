import connect


sql = "UPDATE student SET name='amir',fees=9000 WHERE stid=5"
myc = connect.conn.cursor()

try:
    myc.execute(sql)
    connect.conn.commit()
    print(myc.rowcount,'row has been updated')
except:
    connect.conn.rollback()
    print("unable to update data")
