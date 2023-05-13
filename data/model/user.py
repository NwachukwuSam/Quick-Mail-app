from data.model.email import Email


class User:

    def __init__(self):
        self.__id: int = 0
        self.__first_name: str = ""
        self.__last_name: str = ""
        self.__phone_number: str = ""
        self.__email_address: str = ""
        self.__password: str = ""
        self.__inbox:  list[Email] = []
        self.__outbox: list[Email] = []
        self.__draft: list[Email] = []

    def set_id(self, identity_number: int):
        self.__id = identity_number

    def get_id(self) -> int:
        return self.__id

    def set_first_name(self, first_name: str):
        self.__first_name = first_name

    def get_first_name(self) -> str:
        return self.__first_name

    def set_last_name(self, last_name: str):
        self.__last_name = last_name

    def get_last_name(self) -> str:
        return self.__last_name

    def set_phone_number(self, phone_number: str):
        self.__phone_number = phone_number

    def get_phone_number(self) -> str:
        return self.__phone_number

    def set_email_address(self, email_address: str):
        self.__email_address = email_address

    def get_email_address(self) -> str:
        return self.__email_address

    def set_password(self, password: str):
        self.__password = password

    def get_password(self) -> str:
        return self.__password

    def set_inbox(self, email: Email):
        self.__inbox.append(email)

    def get_inbox(self) -> list[Email]:
        return self.__inbox

    def set_outbox(self, email: Email):
        self.__outbox.append(email)

    def get_outbox(self) -> list[Email]:
        return self.__outbox

    def set_draft(self, email: Email):
        self.__draft.append(email)

    def get_draft(self) -> list[Email]:
        return self.__draft

    def __str__(self):
        return f"""
            QUICK-MAIL
    ========================================
    First Name:{self.__first_name}
    LAST Name: {self.__last_name}
    Phone Number:{self.__phone_number}
    Email Address: {self.__email_address}
    Password: {self.__password}
    ========================================
    """
