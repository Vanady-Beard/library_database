from connect_mysql import connect_database
from mysql.connector import Error
import datetime


def borrow_book():
    try:
        c = connect_database()
        cursor = c.cursor()

        library_id = input("Please enter the customer library Id:  ")
        name = input ("Please enter the customer name: ")
        borrowed_books = datetime.date.today()
        return_books = None
        
        # borrow = (library_id, name, borrowed_books, return_books )
        sql = "INSERT INTO Users (library_id, name, borrowed_books, return_books) VALUES (%s, %s, %s, %s)"
        cursor.execute (sql,(library_id, name, borrowed_books,return_books))
        c.commit()

        print("Book borrowing record is successfully completed!")

    except Error as e:
        print(f"Error: {e}")
    
    finally:
        cursor.close()
        c.close() 




def return_book():
    try:
            c = connect_database()
            cursor = c.cursor()

            library_id = input("Please enter the customer library Id:  ")
            name = input ("Please enter the customer name: ")
            sql_check = "SELECT * FROM users WHERE library_id = %s AND name = %s AND return_books IS NULL "
            cursor.execute(sql_check, (library_id,name))
            record = cursor.fetchone()
            if record:
                return_book = datetime.date.today ()

                sql_update = "UPDATE users SET return_books = %s WHERE library_id = %s AND name = %s"
                cursor.execute(sql_update, (return_book,library_id,name))
                c.commit()
                    
                print (f"Thank you {name} you have successfully returned your book on {return_book} ")         
            else:
                print("Invalid library ID or no borrowing record had been found.")

    except Error as e:
        print(f"Error: {e}")
    
    finally:
        cursor.close()
        c.close() 
    

def view_users():
    try:
        c = connect_database()
        cursor = c.cursor()
        
        query = "SELECT * FROM Users"
        cursor.execute(query)
        users = cursor.fetchall()

        if users:
             for user in users:
                print(user)
    except Error as e:
       print(f"Error: {e}")
    finally: 
        if cursor:
            cursor.close()
        if c:
            c.close()

# return_book()