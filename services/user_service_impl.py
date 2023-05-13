from abc import ABC

from data.model.user import User
from data.repositories.user_implementation import User_Implementation
from dto.requests.user_register_request import User_Registration_Request
from dto.response.user_response import User_Response
from services.user_service_interface import User_Service_Interface
from utils.mapper import Mapper


class User_Service_Implementation(User_Service_Interface, ABC):
    user_repository = User_Implementation()
    user = User()

    def register_user(self, user_register_request: User_Registration_Request) -> User_Response:
        if self.email_exist(user_register_request.get_email_address()):
            raise ValueError(user_register_request.get_email_address() + " " + "Already Exist")

        account = Mapper.map_user_request(user_register_request)
        save_account = self.user_repository.save_user(account)
        response = Mapper.map_user_response(save_account)
        return response

    def email_exist(self, email_address):
        email = self.user_repository.find_user_by_email(email_address)
        if email is not None:
            return True
        else:
            return False

    def login(self, email_address: str, password: str):
        email = self.user_repository.find_user_by_email(email_address)
        if email is None:
            raise ValueError("Email Account does not Exist")
        if email.get_password() == password:
            return True
        else:
            raise ValueError("Invalid Email or Password")

    def find_user(self, email_address: str) -> User:
        users = self.user_repository.find_user_by_email(email_address)
        if users.get_email_address() == email_address:
            return users

    def close_account(self, email_address: str, password: str):
        users = self.user_repository.find_user_by_email(email_address)
        if users.get_password() != password:
            raise ValueError("Invalid Email or Password")
        else:
            self.user_repository.delete_user_by_email(email_address)
