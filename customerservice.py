import mysql.connector

cnx = mysql.connector.connect(user='root', password='Quanlynhansu2023@',
                              host='127.0.0.1',
                              database='bookfetch')
cursor = cnx.cursor()

def cancel_order(orderid):
    cursor.callproc('cancelOrder', [orderid])
    cnx.commit()

def update_trouble_ticket(ticketid, empid, resolution):
    cursor.callproc('updateTroubleTicket', [ticketid, empid, resolution])
    cnx.commit()

def create_trouble_ticket(studentid, category, title, description):
    ticketid = 0
    cursor.callproc('createTroubleTicket', [studentid, category, title,
                                           description, ticketid])
    cnx.commit()
    return ticketid
