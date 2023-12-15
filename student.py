import mysql.connector
from mysql.connector import Error

cnx = mysql.connector.connect(user='root', password='Quanlynhansu2023@',
                              host='127.0.0.1',
                              database='bookfetch')
cursor = cnx.cursor()


def create_cart(studentid):
    cartid = 0
    cursor.callproc('createNewCart', [studentid, cartid])
    cnx.commit()
    return cartid



def add_to_cart(cart_id,isbn,quantity):
    cursor.callproc('addToCart', [cart_id, isbn, quantity])
    cnx.commit()

def create_book_rating(studentid, isbn, rating):
    cursor.callproc('createBookRating', [studentid, isbn, rating])
    cnx.commit()



def cancel_order(orderid):
    cursor.callproc('cancelOrder', [orderid])
    cnx.commit()


def create_user_and_add_to_student(loginname, password, passworddate, f_name, l_name, email, status, year):
    try:

        # Connection parameters - replace with your database details

        connection = mysql.connector.connect(

            host='127.0.0.1',

            database='bookfetch',

            user='root',

            password='Quanlynhansu2023@'

        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Call the stored procedure

            args = (loginname, password, passworddate, f_name, l_name, email, status, year)

            cursor.callproc('CreateUserAndAddToStudent', args)

            # Commit the transaction

            connection.commit()

            print("User and student record inserted successfully")



    except Error as e:

        print("Error while connecting to MySQL", e)



    finally:

        # Closing the connection

        if connection.is_connected():
            cursor.close()

            connection.close()

            print("MySQL connection is closed")


# Example usage



def create_order(studentid, cartid, shipping, ccdetails):
    orderid = 0
    cursor.callproc('createOrderFromCart', [studentid, cartid,
                                            shipping, ccdetails, orderid])
    cnx.commit()
    return orderid


def create_trouble_ticket(studentid, category, title, description):
    ticketid = 0
    cursor.callproc('createTroubleTicket', [studentid, category, title,
                                            description, ticketid])
    cnx.commit()
    return ticketid




def view_information(studentid):
    cursor.execute("SELECT username, email, address FROM student WHERE studentid = %s", (studentid,))
    student_info = cursor.fetchone()
    if student_info:
        username, email, address = student_info
        print(f"Student ID: {studentid}")
        print(f"Username: {username}")
        print(f"Email: {email}")
        print(f"Address: {address}")
    else:
        print("Student information not found.")
