class User_Response:
    def __init__(self):
        self.__full_name: str = ""
        self.__phone_number: str = ""
        self.__email_address: str = ""
        self.__password: str = ""

    def set_full_name(self, full_name: str):
        self.__full_name = full_name

    def get_full_name(self) -> str:
        return self.__full_name

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

    def __str__(self):
        return f"""
            QUICK-MAIL
    ========================================
    Full Name:{self.__full_name}
    Phone Number:{self.__phone_number}
    Email Address: {self.__email_address}
    Password: {self.__password}
    ========================================
    """
