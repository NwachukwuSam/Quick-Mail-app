from abc import ABC

from data.model.email import Email
from data.repositories.email_implementation import Email_Implementation
from data.repositories.user_repository_interface import User_Repository_Interface
from dto.requests.email_request import Email_Request
from dto.response.email_response import Email_Response
from services.email_service_interface import Email_Service_Interface
from utils.email_not_found import EmailNotFound
from utils.mapper import Mapper


class Email_service_Implementation(Email_Service_Interface, ABC):
    email_repository = Email_Implementation()
    email = Email()
    user_repository = User_Repository_Interface()

    def save_email(self, email_request: Email_Request) -> Email_Response:
        self.recipient_email_not_found(email_request.get_recipient_email())
        email = Mapper.map_email_request(email_request.)


    def recipient_email_not_found(self, email_address):
         email = self.user_repository.find_user_by_email(email_address)
         if email is False:
             raise EmailNotFound("Email does not exist")
