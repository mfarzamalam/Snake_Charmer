import connect 

    # Inserting single data in tuple format
sql = "INSERT INTO student1(name,roll,fees) VALUES (%s,%s,%s)"
myc = connect.conn.cursor()
single_parameter = ('sumit',21,5000)

try:
    myc.execute(sql,single_parameter)
    print(myc.rowcount,'row inserted')
    print(myc.lastrowid,'is the last data inserted in the table')
    connect.conn.commit()
except:
    connect.conn.rollback()
    print("unable to add data")