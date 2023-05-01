from abc import ABC, abstractmethod

from data.model.user import User


class User_Repository_Interface(ABC):
    @abstractmethod
    def save_user(self, user: User) -> User:
        pass

    @abstractmethod
    def find_user_by_email(self, email_address: str) -> User:
        pass

    @abstractmethod
    def delete_user_by_email(self, email_address: str):
        pass
