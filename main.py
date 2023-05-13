import sys
import tkinter as tk
from tkinter import messagebox, simpledialog
import re
from unittest import TestCase

from controllers.Email_controller import Email_Controller
from controllers.User_controller import User_Controller
from data.model.user import User
from data.repositories.user_implementation import User_Implementation
from dto.requests.email_request import Email_Request
from dto.requests.user_register_request import User_Registration_Request
from dto.response.user_response import User_Response

user_controller = User_Controller()
email_controller = Email_Controller()


def input_collector(prompt):
    root = tk.Tk

    collect_input = tk.simpledialog.askstring(title="Quick-Mail", prompt=prompt)
    return collect_input


def display(prompt):
    messagebox.showinfo("Quick-Mail", prompt)


def sign_up_page():
    page = """
      WELCOME QUICK MAIL
    ==============================
    1. Login
    2. Create A Quick Mail Account
    3. Exit Application
    =============================="""
    user_input = input_collector(page)

    if user_input == "1":
        login()
    elif user_input == "2":
        create_account()
    elif user_input == "3":
        exit_application()
    else:
        sign_up_page()


def login():
    email_address = input_collector("Enter Your Email Address: ")
    password = input_collector("Enter Your Password: ")
    login_response = user_controller.login(email_address, password)
    display(login_response)
    if login_response is True:
        home_page()
    else:
        sign_up_page()


def create_account():
    register_user = User_Registration_Request()
    first_name = input_collector("Enter Your First Name: ")
    last_name = input_collector("Enter Your Last Name: ")
    while True:
        phone_number = input_collector("Enter your valid Phone Number")
        if validate_nigerian_phone_number(phone_number):
            break
        else:
            display("Invalid Phone Number. Please Enter a Valid Nigerian Phone Number.")
    password = input_collector("Create A Password: ")
    register_user.set_first_name(first_name)
    register_user.set_last_name(last_name)
    register_user.set_phone_number(phone_number)
    register_user.set_password(password)
    response = user_controller.register_account(register_user)
    display(response)
    sign_up_page()


def exit_application():
    display("Thank You For Using Quick Mail")
    sys.exit()


def home_page():
    home = """
    =============================
    1. Compose Draft Mail
    2. Send Message
    3. Inbox
    4. Outbox
    5. Draft
    6. Find Email
    7. Delete A Mail
    8. Logout
    =============================="""
    user_input = input_collector(home)
    if user_input == "1":
        compose_draft_mail()
    elif user_input == "2":
        send_message()
    elif user_input == "3":
        inbox()
    elif user_input == "4":
        outbox()
    elif user_input == "5":
        draft()
    elif user_input == "6":
        find_email()
    elif user_input == "7":
        delete_mail()
    elif user_input == "8":
        sign_up_page()
    else:
        print("Wrong Input! Enter A Valid Input")
    home_page()


def compose_draft_mail():
    email_request = Email_Request()
    email_title = input_collector("Enter Message Title: ")
    email_body = input_collector("Type Your Message: ")
    email_request.set_title(email_title)
    email_request.set_email_body(email_body)
    save_message_response = email_controller.save_email(email_request)
    display(save_message_response)
    home_page()


def send_message():
    email_request = Email_Request()
    senders_email = input_collector("Enter Your e-Mail Address: ")
    receivers_email = input_collector("Enter Recipient's e-Mail Address: ")
    email_title = input_collector("Enter Message Title: ")
    email_body = input_collector("Type Your Message: ")
    email_request.set_senders_email(senders_email)
    email_request.set_recipient_email(receivers_email)
    email_request.set_title(email_title)
    email_request.set_email_body(email_body)
    save_message_response = email_controller.send_mail(email_request)
    display(save_message_response)
    home_page()


def inbox():
    view_inbox = email_controller.view_inbox()
    display(view_inbox)
    home_page()


def outbox():
    view_outbox = email_controller.view_outbox()
    display(view_outbox)
    home_page()


def draft():
    view_draft = email_controller.view_draft()
    display(view_draft)


def find_email():
    email_title = input_collector("Enter Email Title: ")
    find_response = email_controller.find_email(email_title)
    display(find_response)
    home_page()


def delete_mail():
    email_title = input_collector("Enter Account Number: ")
    response = email_controller.delete_email(email_title)
    display(response)
    home_page()


def validate_nigerian_phone_number(phone_number):
    pattern = r"^(080|081|090|070|091)\d{8}$"
    return bool(re.match(pattern, phone_number))


def validate_email_address(email):
    pat = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pat, email))


def test_that_user_can_register():
    register = User()
    user_repo = User_Implementation()
    register.set_first_name("Sam")
    register.set_last_name("Big")
    register.set_password("1234")
    user_repo.save_user(register)


if __name__ == '__main__':
    #test_that_user_can_register()
    sign_up_page()





