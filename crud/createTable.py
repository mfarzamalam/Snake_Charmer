import connect

sql1 = "CREATE TABLE student1(stid INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(20), roll INT, fees FLOAT)"
sql2 = "SHOW TABLES"
myc = connect.conn2.cursor()    # connect the table with database
myc.execute(sql2)               # execute the command
for table in myc:               # get all the tables in myc and looping them one by one
    print(table)

myc.close()