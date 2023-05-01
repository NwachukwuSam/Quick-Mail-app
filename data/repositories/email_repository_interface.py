from abc import ABC, abstractmethod

from data.model.email import Email


class Email_Repository_Interface(ABC):
    @abstractmethod
    def save_email(self, email: Email) -> Email:
        pass

    @abstractmethod
    def find_email_by_title(self, email_title: str) -> Email:
        pass

    @abstractmethod
    def delete_email_by_title(self, email_title: str) -> None:
        pass

