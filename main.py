def admin_interaction():
    from admin import create_cs_employee, create_book, create_university, deactivate_admin, \
       remove_customer_support

    emp_id = create_cs_employee('csrep9', 'csemp10@example.com', 50000)
    print(emp_id)
    create_book('9781234567820', 'Python 108', 'Jane Doe6', 5, 19.99)
    #deactivate_admin(106)


def customer_service_interaction():
    from customerservice import create_trouble_ticket, update_trouble_ticket,cancel_order
    # Customer service interaction logic
    # ...
    student_id=62
    ticket_id = create_trouble_ticket(student_id, 'Order Issue', 'Shipping Delay',
                                      'My order has not arrived')
    print(ticket_id)

    #assign_to = 102
    #update_trouble_ticket(ticket_id, assign_to, 'Sorry for the trouble, investigating issue')


def student_interaction():
    from student import create_cart, add_to_cart, create_book_rating, create_user_and_add_to_student, create_order, \
        view_information,cancel_order
    # Student interaction logic
    # ...
    student_id = create_user_and_add_to_student('cat5', '2016', '2023-12-15 00:00:00', 'Nguyen', 'Cat',
                               'huynh3298@gmail.com', 'graduate', 2)

    print(student_id)
    cart_id = create_cart(student_id)
    print(cart_id)
    create_book_rating(student_id, '9781234567891', 5)

    order_id = create_order(student_id, cart_id, 'Standard', '4444333322221122')
    cancel_order(order_id)
    print(order_id)


def main():
    print("Welcome! Please select the mode of interaction:")
    print("1. Admin")
    print("2. Customer Service")
    print("3. Student")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        admin_interaction()
    elif choice == '2':
        customer_service_interaction()
    elif choice == '3':
        student_interaction()
    else:
        print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()