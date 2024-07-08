
from author import authors, view_authors
from book import add_book, view_books
from user import borrow_book, return_book, view_users
from connect_mysql import connect_database
from mysql.connector import Error


def main_menu():
    try:
        c = connect_database()
        cursor = c.cursor()
        while True:
            user_input = input('''
Welcome to the Library Management System!

    Main Menu:
    1. Book Operations
    2. User Operations
    3. Author Operations
    4. Quit

 ''')

            if user_input == '1':
             book_operations()
            elif user_input == '2':
                user_operations()
            elif user_input == '3':
                author_operations()
            elif user_input == '4':
                print("Goodbye!")
                break
            else:
                print("Invalid input. Please enter a valid option (1/2/3/4).")
    except Error as e:
       print(f"Error: {e}")
    finally: 
        if cursor:
            cursor.close()
        if c:
            c.close()
def book_operations():
    while True:
        user_input = input('''
    Book Operations Menu:

    1. Add a New Book
    2. View All Books
    3. Back to Main Menu
 ''')

        if user_input == '1':
            add_book()
        elif user_input == '2':
            view_books()
    
        elif user_input == '3':
            break
        else:
            print("Invalid input. Please enter a valid option (1/2/3).")

def user_operations():
    while True:
        user_input = input('''
    User Operations Menu:

    
    1. Borrow a Book
    2. Return a Book
    3. View Borrowed Books
    4. Back to Main Menu

 ''')

        if user_input == '1':
            borrow_book()
            
        elif user_input == '2':
           return_book()
        elif user_input == '3':
          view_users()
            
        elif user_input == '4':
            break
       
        else:
            print("Invalid input. Please enter a valid option (1/2/3/4/5).")

def author_operations():
    while True:
        user_input = input('''
    Author Operations Menu:

    1. Add a New Author
    2. View Author Details
    3. Back to Main Menu

 ''')

        if user_input == '1':
            authors()
        elif user_input == '2':
            view_authors()
        elif user_input == '3':
            pass
        else:
            print("Invalid input. Please enter a valid option (1/2/3).")






if __name__ == "__main__":
    main_menu()



#==============================================

# main.py

# main.py

# from author import authors
# from book import add_book
# from user import borrow_book, return_book
# from connect_mysql import connect_database
# import mysql.connector

# def main_menu(cursor):
#     while True:
#         user_input = input('''
# Welcome to the Library Management System!

#     Main Menu:
#     1. Book Operations
#     2. User Operations
#     3. Author Operations
#     4. Quit

#  ''')

#         if user_input == '1':
#             book_operations(cursor)
#         elif user_input == '2':
#             user_operations(cursor)
#         elif user_input == '3':
#             authors(cursor)
#         elif user_input == '4':
#             print("Goodbye!")
#             break
#         else:
#             print("Invalid input. Please enter a valid option (1/2/3/4).")

# def book_operations(cursor):
#     while True:
#         user_input = input('''
#     Book Operations Menu:

#     1. Add a New Book
#     2. View All Books
#     3. Back to Main Menu
#  ''')

#         if user_input == '1':
#             add_book(cursor)
#         elif user_input == '2':
#             view_books(cursor)
#         elif user_input == '3':
#             break
#         else:
#             print("Invalid input. Please enter a valid option (1/2/3).")

# def view_books(cursor):
#     query = "SELECT * FROM Books"
#     cursor.execute(query)
#     books = cursor.fetchall()
    
#     if books:
#         for book in books:
#             print(book)
#     else:
#         print("No books found.")

# def user_operations(cursor):
#     while True:
#         user_input = input('''
#     User Operations Menu:

#     1. Borrow a Book
#     2. Return a Book
#     3. View Borrowed Books
#     4. Back to Main Menu

#  ''')

#         if user_input == '1':
#             borrow_book(cursor)
#         elif user_input == '2':
#             return_book(cursor)
#         elif user_input == '3':
#             view_users(cursor)
#         elif user_input == '4':
#             break
#         else:
#             print("Invalid input. Please enter a valid option (1/2/3/4).")

# def view_users(cursor):
#     query = "SELECT * FROM Users"
#     cursor.execute(query)
#     users = cursor.fetchall()
    
#     if users:
#         for user in users:
#             print(user)
#     else:
#         print("No users found.")

# def author_operations(cursor):
#     while True:
#         user_input = input('''
#     Author Operations Menu:

#     1. Add a New Author
#     2. View Authors
#     3. Back to Main Menu

#  ''')

#         if user_input == '1':
#             authors(cursor)
#         elif user_input == '2':
#             view_authors(cursor)
#         elif user_input == '3':
#             break
#         else:
#             print("Invalid input. Please enter a valid option (1/2/3).")

# def view_authors(cursor):
#     query = "SELECT * FROM Authors"
#     cursor.execute(query)
#     authors = cursor.fetchall()
    
#     if authors:
#         for author in authors:
#             print(author)
#     else:
#         print("No authors found.")

# def main():
#     connection = connect_database()
    
#     if connection:
#         cursor = connection.cursor(buffered=True)
#         main_menu(cursor)
#         cursor.close()
#         connection.close()
#         print("MySQL connection is closed")

# if __name__ == "__main__":
#     main()
