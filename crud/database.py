        #Creating and viewing new database

database = 'SHOW DATABASES'
myc = conn2.cursor()
myc.execute(database)
for d in myc:
    print(d)

myc.close()