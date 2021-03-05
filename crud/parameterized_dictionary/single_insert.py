import connect 

    # Inserting single data in dictionary format
sql = "INSERT INTO student1(name,roll,fees) VALUES (%(n)s,%(rn)s,%(f)s)"
myc = connect.conn.cursor()
single_parameter = {    #no need to maintain the order because it's bind with Key
    'n':'sameer',
    'f':25000,
    'rn':55
}

try:
    myc.execute(sql,single_parameter)
    print(myc.rowcount,'row inserted')
    print(myc.lastrowid,'is the id of last data inserted in the table')
    connect.conn.commit()
except:
    connect.conn.rollback()
    print("unable to add data")