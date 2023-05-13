from dto.requests.email_request import Email_Request
from services.email_service_impl import Email_service_Implementation
from utils.email_not_found import EmailNotFound


class Email_Controller:
    def __init__(self):
        self.email_services = Email_service_Implementation()

    def save_email(self, email_request: Email_Request):
        try:
            save_mail_response = self.email_services.save_email(email_request)
            return save_mail_response
        except EmailNotFound as error:
            return str(error)

    def send_mail(self, email_request: Email_Request):
        try:
            send_mail_response = self.email_services.send_email(email_request)
            return send_mail_response
        except EmailNotFound as error:
            return str(error)

    def find_email(self, email_title):
        try:
            find_email_response = self.email_services.find_email(email_title)
            return find_email_response
        except EmailNotFound as error:
            return str(error)

    def delete_email(self, email_title):
        try:
            find_email_response = self.email_services.delete_email(email_title)
            return find_email_response
        except EmailNotFound as error:
            return str(error)

    def view_inbox(self):
        try:
            view_in = self.email_services.view_inbox()
            return view_in
        except ValueError as error:
            return error

    def view_outbox(self):
        try:
            view_out = self.email_services.view_outbox()
            return view_out
        except ValueError as error:
            return error

    def view_draft(self):
        try:
            view_dft = self.email_services.view_draft()
            return view_dft
        except ValueError as error:
            return error
