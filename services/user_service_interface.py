from abc import ABC, abstractmethod

from data.model.user import User
from dto.requests.user_register_request import User_Registration_Request
from dto.response.user_response import User_Response


class User_Service_Interface(ABC):
    @abstractmethod
    def register_user(self, user_register_request: User_Registration_Request) -> User_Response:
        pass

    @abstractmethod
    def find_user(self, email_address: str) -> User:
        pass

    @abstractmethod
    def close_account(self, email_address:str, password:str):
        pass

    @abstractmethod
    def login(self, email_address: str, password:str):
        pass
