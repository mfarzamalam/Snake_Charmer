import mysql.connector as mc


        # First way to connect to the database
conn = mc.connect(
    user='root',
    password='',
    host='localhost',
    database='pdb'
    )
if conn:
    print("Connected")
else:
    print("Not Connected")


        # Second way to connect to the database
config = {
    'user':'root',
    'password':'',
    'host':'localhost',
    'database':'pdb'
}
try:
    conn2 = mc.connect(**config)
    print(conn2.is_connected())     # Print TRUE if connected
except:
    print("No x2")