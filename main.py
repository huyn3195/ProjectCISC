def admin_interaction():
    from admin import create_cs_employee, create_book, create_university, deactivate_admin, \
       remove_customer_support

    # Admin interaction logic
    # ...


def customer_service_interaction():
    from customerservice import create_trouble_ticket, update_trouble_ticket,cancel_order
    # Customer service interaction logic
    # ...


def student_interaction():
    from student import create_cart, add_to_cart, create_book_rating, create_student, create_order, \
        view_information
    # Student interaction logic
    # ...


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