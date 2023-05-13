from abc import ABC
from typing import Type, List

from data.model.email import Email
from data.model.user import User
from data.repositories.email_implementation import Email_Implementation
from data.repositories.user_implementation import User_Implementation
from dto.requests.email_request import Email_Request
from dto.response.email_response import Email_Response
from services.email_service_interface import Email_Service_Interface
from utils.cannot_send_to_yourself import CannotSendToYourself
from utils.email_not_found import EmailNotFound
from utils.mapper import Mapper


class Email_service_Implementation(Email_Service_Interface, ABC):
    email_repository = Email_Implementation()
    email = Email()
    user = User()
    user_repository = User_Implementation()

    def save_email(self, email_request: Email_Request) -> Email_Response:
        senders_email = self.user_repository.find_user_by_email(email_request.get_senders_email())
        if senders_email is None:
            raise EmailNotFound("Email Address Not Found")
        else:
            email = Mapper.map_email_request(email_request)
            save_email = senders_email.set_draft(email)
            response = Mapper.map_email_response(save_email)
            return response

    def email_account_exist(self, email_address):
        email = self.user_repository.find_user_by_email(email_address)
        if email is not None:
            return True
        else:
            return False

    def send_email(self, email_request: Email_Request) -> Email_Response:
        recipient_email = self.user_repository.find_user_by_email(email_request.get_recipient_email())
        senders_email = self.user_repository.find_user_by_email(email_request.get_senders_email())
        if recipient_email is None or senders_email is None:
            raise EmailNotFound("One Of the Email Address does not exist")
        elif senders_email == recipient_email:
            raise CannotSendToYourself("Cannot Send Email To Yourself")
        else:
            send = Mapper.map_email_request(email_request)
            recipient_email.set_inbox(send)
            senders_email.set_outbox(send)
            send_response = Mapper.map_email_response(send)
            return send_response

    def view_inbox(self, email_request: Email_Request) -> list[Email]:
        # inbox = self.user.get_inbox()
        # if len(inbox) == 0:
        #     raise ValueError("Your Inbox is Empty")
        user = self.user_repository.find_user_by_email(email_request.get_recipient_email())
        inbox = user.get_inbox()
        return inbox

    def view_outbox(self, email_request: Email_Request) -> list[Email]:
        # outbox = self.user.get_outbox()
        # if len(outbox) == 0:
        #     raise ValueError("Your Outbox is Empty")
        user = self.user_repository.find_user_by_email(email_request.get_recipient_email())
        outbox = user.get_outbox()
        return outbox

    def view_draft(self) -> Type[Email_Response]:
        draft = self.user.get_draft()
        if len(draft) == 0:
            raise ValueError("Your Draft Box is Empty")
        return Email_Response

    def find_email(self, email_title: str) -> Email:
        email = self.email_repository.find_email_by_title(email_title)
        if email == email_title:
            return email
        else:
            raise EmailNotFound("Email with the title You entered Not Found")

    def delete_email(self, email_title: str):
        email = self.email_repository.find_email_by_title(email_title)
        if email.get_title() == email_title:
            self.email_repository.delete_email_by_title(email_title)
        else:
            raise EmailNotFound("Email with title " + email.get_title() + " Not Found")

        # elif senders_email or recipient_email or email_request.get_title() \
        #         or email_request.get_email_body() is not None:
        #     recipient_email.set_inbox(send)
        #     senders_email.set_outbox(send)
        #     send_response = Mapper.map_email_response(send)
        #     return send_response
        # else:
        #     senders_email.set_draft(send)
