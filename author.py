
from connect_mysql import connect_database
from mysql.connector import Error

def authors ():
    try:
         c = connect_database()
         cursor = c.cursor()


         author_id = int(input("What is the author ID of the book? "))
         name = input("What is the author's name: ")
         biography = input("What is the author's biography: ")
    
         sql = "INSERT INTO Authors (author_id, name, biography) VALUES (%s, %s, %s) "
         author_list = (author_id, name, biography )
        
         cursor.execute(sql, author_list)
         c.commit()

         print(f"Author with the ID {author_id}  was successfully updated!")

    except Error as e:
        print(f"Error:{e}")

    finally:
    
        cursor.close()
        c.close()

    return sql, author_list

def view_authors():
    try:
        c = connect_database()
        cursor = c.cursor()
        
        query = "SELECT * FROM Authors"
        cursor.execute(query)
        authors = cursor.fetchall()

        if authors:
             for author in authors:
                print(author)
    except Error as e:
       print(f"Error: {e}")
    finally: 
        if cursor:
            cursor.close()
        if c:
            c.close()

