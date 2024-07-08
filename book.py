
from connect_mysql import connect_database
from mysql.connector import Error
from datetime import datetime

def date_check(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False


def book_availability(book_id):
    try:
        c = connect_database()
        cursor = c.cursor()

        sql = " SELECT available_status FROM Books WHERE book_id = %s "
        cursor.execute(sql, (book_id,))
        result = cursor.fetchone()

        if result:
           return result [0]
        return "Not Found"

        #    if return_books is None:
        #        if borrowed_books is None:
        #         return "Available" 
        #        else:
        #          return (f"Not Available")
        #    else:
        #       return "Available"
    except Error as e:
        print(f"Error: {e}")
        return "Error"
    finally:
        cursor.close()
        c.close()
         

def add_book():
    try:
        c = connect_database()
        cursor = c.cursor()

        # book_id = input("What's your book_id? ")
        title = input("Please enter the title of the book:  ")
        genre = input ("Please enter the genre of the book: ")
        publication_date = input("Please enter the book publication date (YYYY-MM-DD):  ")
        author_id = int(input("Please enter the author_id: "))
        

        if not date_check(publication_date):
            print("Invalid date format. Please format the date YYYY-MM-DD. ")
            return
        available_status = book_availability(author_id)
        if available_status == "Available":
            print(f"Author with author_id {author_id} is available.")
            return
     
        sql = "INSERT INTO Books (title, genre, publication_date, available_status, author_id ) VALUES (%s, %s, %s, %s, %s)"
        add_books = (title, genre, publication_date, available_status, author_id )
        cursor.execute (sql, add_books)
        c.commit()

        print( "Added book successfully!")
        

    except Error as e:
        print(f"Error: {e}")
    
    finally:
        cursor.close()
        c.close() 

def view_books():
    try:
        c = connect_database()
        cursor = c.cursor()
        
        query = "SELECT * FROM BOOKS"
        cursor.execute(query)
        books = cursor.fetchall()

        if books:
             for book in books:
                print(book)
    except Error as e:
       print(f"Error: {e}")
    finally: 
        if cursor:
            cursor.close()
        if c:
            c.close()

    
# add_book()



