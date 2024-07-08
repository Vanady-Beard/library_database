import mysql.connector
from mysql.connector import Error

def connect_database():
    data_name = "libary_manage"
    user = "root"
    password = "newyork12"
    host = "localhost"

    try:
        c = mysql.connector.connect(
        database = data_name,
        user = user,
        password = password,
        host = host
    )
        if c.is_connected ():
         print("Connected to MySQL Database successfully")
        return c
    
    except Error as e:
       print(f"Error: {e}")

    # finally:
    #    if c and c.is_connected():
    #       c.close()
    #       print("Mysql connection is closed.")
connect_database()