class Email:
    def __init__(self):
        self.__email_id: int = 0
        self.__recipient_email: str = ""
        self.__senders_email: str = ""
        self.__title: str = ""
        self.__email_body: str = ""

    def set_email_id(self, email_id: int):
        self.__email_id = email_id

    def get_email_id(self) -> int:
        return self.__email_id

    def set_senders_email(self, senders_email: str):
        self.__senders_email = senders_email

    def get_senders_email(self) -> str:
        return self.__senders_email

    def set_recipient_email(self, recipient_email: str):
        self.__recipient_email = recipient_email

    def get_recipient_email(self) -> str:
        return self.__recipient_email

    def set_title(self, title: str):
        self.__title = title

    def get_title(self) -> str:
        return self.__title

    def set_email_body(self, email_body: str):
        self.__email_body = email_body

    def get_email_body(self) -> str:
        return self.__email_body
