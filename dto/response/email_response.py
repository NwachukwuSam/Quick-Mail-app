class Email_Response:
    def __init__(self):
        self.__recipient_email: str = ""
        self.__senders_email: str = ""
        self.__title: str = ""
        self.__email_body: str = ""

    def set_recipient_email(self, recipient_email: str):
        self.__recipient_email = recipient_email

    def get_recipient_email(self) -> str:
        return self.__recipient_email

    def set_senders_email(self, senders_email: str):
        self.__senders_email = senders_email

    def get_senders_email(self) -> str:
        return self.__senders_email

    def set_title(self, title: str):
        self.__title = title

    def get_title(self) -> str:
        return self.__title

    def set_email_body(self, email_body: str):
        self.__email_body = email_body

    def get_email_body(self) -> str:
        return self.__email_body

    def __str__(self):
        return f"""
                QUICK-MAIL
    ========================================
    Your Email: {self.__senders_email}
    Recipients Email:{self.__recipient_email} 
    Email Title:{self.__title}
    Message Body: {self.__email_body}
    ========================================
    """
