import mysql.connector

cnx = mysql.connector.connect(user='username', password='password',
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


def create_student(username, email, address):
    studentid = 0
    cursor.callproc('createNewStudent', [username, email, address, studentid])
    cnx.commit()
    return studentid


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
