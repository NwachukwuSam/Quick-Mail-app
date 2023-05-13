from dto.requests.user_register_request import User_Registration_Request
from services.user_service_impl import User_Service_Implementation


class User_Controller:
    def __init__(self):
        self.user_services = User_Service_Implementation()

    def register_account(self, create_request: User_Registration_Request):
        try:
            register_response = self.user_services.register_user(create_request)
            return register_response
        except ValueError as error:
            return str(error)

    def login(self, email_address, password):
        try:
            login_response = self.user_services.login(email_address, password)
            return login_response
        except ValueError as error:
            return str(error)

    def find_user(self, email_address):
        try:
            find_user = self.user_services.find_user(email_address)
            return find_user
        except ValueError as error:
            return str(error)

    def close_account(self, account_number, password):
        try:
            delete = self.user_services.close_account(account_number, password)
            return delete
        except ValueError as error:
            return str(error)
