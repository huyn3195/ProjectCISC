def admin_interaction():
    from admin import create_cs_employee, create_book, create_university, deactivate_admin, \
       remove_customer_support

    emp_id = create_cs_employee('csrep1', 'csemp1@example.com', 50000)
    print(emp_id)
    create_book('9781234567892', 'Python 101', 'Jane Doe', 5, 19.99)
    deactivate_admin(105)


def customer_service_interaction():
    from customerservice import create_trouble_ticket, update_trouble_ticket,cancel_order
    # Customer service interaction logic
    # ...
    student_id=1
    ticket_id = create_trouble_ticket(student_id, 'Order Issue', 'Shipping Delay',
                                      'My order has not arrived')
    print(ticket_id)

    assign_to = 102
    update_trouble_ticket(ticket_id, assign_to, 'Sorry for the trouble, investigating issue')


def student_interaction():
    from student import create_cart, add_to_cart, create_book_rating, create_student, create_order, \
        view_information
    # Student interaction logic
    # ...
    student_id = create_student('jsmith', 'jsmith@example.com', '123 Main St, Anytown')
    print(student_id)
    cart_id = create_cart(student_id)
    print(cart_id)
    create_book_rating(student_id, '9781234567891', 5)
    add_to_cart(cart_id, '9781234567891', 2)
    order_id = create_order(student_id, cart_id, 'Standard', '4444333322221111')
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