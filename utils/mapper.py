from data.model.email import Email
from data.model.user import User
from dto.requests.email_request import Email_Request
from dto.requests.user_register_request import User_Registration_Request
from dto.response.email_response import Email_Response
from dto.response.user_response import User_Response


class Mapper:
    @staticmethod
    def map_user_request(user_register: User_Registration_Request) -> User:
        user = User()
        user.set_first_name(user_register.get_first_name())
        user.set_last_name(user_register.get_last_name())
        user.set_email_address(user_register.get_email_address())
        user.set_phone_number(user_register.get_phone_number())
        user.set_password(user_register.get_password())
        return user

    @staticmethod
    def map_user_response(user: User) -> User_Response:
        user_response = User_Response()
        user_response.set_full_name(user.get_first_name() + " " + user.get_last_name())
        user_response.set_email_address(user.get_email_address())
        user_response.set_phone_number(user.get_phone_number())
        user_response.set_password(user.get_password())
        return user_response

    @staticmethod
    def map_email_request(email_request: Email_Request) -> Email:
        email = Email()
        email.set_recipient_email(email_request.get_recipient_email())
        email.set_title(email_request.get_title())
        email.set_email_body(email_request.get_email_body())
        return email

    @staticmethod
    def map_email_response(email: Email) -> Email_Response:
        email_response = Email_Response()
        email_response.set_recipient_email(email.get_recipient_email())
        email_response.set_title(email.get_title())
        email_response.set_email_body(email.get_email_body())
        return email_response
    
