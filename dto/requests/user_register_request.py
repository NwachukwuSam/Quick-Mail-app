class User_Registration_Request:

    def __init__(self):
        self.__first_name: str = ""
        self.__last_name: str = ""
        self.__phone_number: str = ""
        self.__email_address: str = ""
        self.__password: str = ""

    def set_first_name(self, first_name: str):
        self.__first_name = first_name

    def get_first_name(self) -> str:
        return self.__first_name

    def set_last_name(self, last_name: str):
        self.__first_name = last_name

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
