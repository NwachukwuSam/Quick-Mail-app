from abc import ABC

from data.model.email import Email
from data.repositories.email_repository_interface import Email_Repository_Interface


class Email_Implementation(Email_Repository_Interface, ABC):
    emails: list[Email] = []
    count = 0

    def save_email(self, email: Email) -> Email:
        email.set_email_id(self.generate_email_id())
        self.emails.append(email)
        self.count += 1
        return email

    def generate_email_id(self):
        return self.count + 1

    def find_email_by_title(self, email_title: str) -> Email:
        for email in self.emails:
            if email.get_title() == email_title:
                return email

    def delete_email_by_title(self, email_title: str) -> None:
        for email in self.emails:
            if email.get_title() == email_title:
                self.emails.remove(email)
                self.count -= 1
                break

    def counter(self):
        return self.count
