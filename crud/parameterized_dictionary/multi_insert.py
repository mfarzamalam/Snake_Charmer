import connect

    # Inserting multiple data in tuple format
sql = "INSERT INTO student1(name,roll,fees) VALUES (%(n)s,%(rn)s,%(f)s)"
myc = connect.conn.cursor()
multiple_data = [
    {
        'n':'sameer',
        'f':25000,
        'rn':55
    },{
        'n':'sameer',
        'f':25000,
        'rn':55
    },{
        'n':'sameer',
        'f':25000,
        'rn':55
    }
]

try:
    myc.executemany(sql,multiple_data)
    print(myc.rowcount,'row inserted')
    print(myc.lastrowid,'is the last data inserted in the table')
    connect.conn.commit()
except:
    connect.conn.rollback()
    print("unable to add data")