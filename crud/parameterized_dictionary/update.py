import connect 

sql="UPDATE student1 SET name=%(n)s WHERE stid=%(id)s"
myc = connect.conn.cursor()
value = {
    'n':'akmal',
    'id':'46'
}

try:
    myc.execute(sql,value)
    for v,k in value.items():
        row = k
    print("Row",row,"has been updated")
    connect.conn.commit()
except:
    connect.conn.rollback()
    print("unable to update data")