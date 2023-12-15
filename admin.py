import mysql.connector

cnx = mysql.connector.connect(user='root', password='Quanlynhansu2023@',
                              host='127.0.0.1',
                              database='bookfetch')
cursor = cnx.cursor()
def create_cs_employee(username, email, salary):
    empid = 0
    cursor.callproc('createCSEmployee', [username, email, salary, empid])
    cnx.commit()
    return empid
def create_university(name, abbrevname, repfname, replname, repemail, repphone):
    universityid = 0
    cursor.callproc('createUniversity', [name, abbrevname, repfname, replname,
                                         repemail, repphone, universityid])
    cnx.commit()
    return universityid
def create_book(isbn, title, author, quantity, price):
    cursor.callproc('createBook', [isbn, title, author, quantity, price])
    cnx.commit()
def remove_customer_support(empid):
    try:
        # Call stored procedure to perform additional cleanup if needed
        cursor.callproc('removeEmployee', [empid])
        cnx.commit()

        # Delete the employee record from the database
        delete_query = "DELETE FROM customersupport WHERE empid = %s"
        cursor.execute(delete_query, (empid,))
        cnx.commit()

        print(f"Employee with ID {empid} has been successfully removed.")
    except mysql.connector.Error as err:
        # Handle any errors or exceptions that might occur during removal
        print(f"Error occurred: {err}")





def deactivate_admin(empid):
    cursor.callproc('deactivateAdmin', [empid])
    cnx.commit()
