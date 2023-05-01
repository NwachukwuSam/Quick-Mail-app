from abc import ABC
from random import random

from data.model.user import User
from data.repositories.user_repository_interface import User_Repository_Interface


class User_Implementation(User_Repository_Interface, ABC):
    users: list[User] = []
    count = 0

    def save_user(self, user: User) -> User:
        rand = random.randint(1, 100)
        if user.get_id() == 0:
            user.set_id(self.generate_user_id())
            user.set_email_address(user.get_first_name() + user.get_last_name() + rand)
        self.users.append(user)
        self.count += 1
        return user

    def generate_user_id(self):
        return self.count + 1

    def find_user_by_email(self, email_address: str) -> User:
        for user in self.users:
            if user.get_email_address() == email_address:
                return user

    def delete_user_by_email(self, email_address: str):
        for user in self.users:
            if user.get_email_address() == email_address:
                self.users.remove(user)
                self.count -= 1
                break

    def counter(self):
        return self.count
