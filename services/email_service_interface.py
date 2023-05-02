from abc import ABC, abstractmethod

from dto.requests.email_request import Email_Request
from dto.response.email_response import Email_Response


class Email_Service_Interface(ABC):
    @abstractmethod
    def save_email(self, email_request: Email_Request) -> Email_Response:
        pass

    @abstractmethod
    def send_email(self, email_request: Email_Request) -> Email_Response:
        pass

    @abstractmethod
    def find_email(self, email_title: str) -> Email_Response:
        pass

    @abstractmethod
    def delete_email(self, email_title: str):
        pass
