from tests.config import requests
from tests.routes.login import Login


class Test_Login(Login):

    def test_login(self, DB):
        """Test POST request to /login endpoint
        Signup and Login a user
        """

        user = self.generate_user()

        login_data = {
            "username": user["username"],
            "password": user["password"],
        }

        requests.post(self.signup_url, json=user)

        response = requests.post(self.login_url, json=login_data)

        self.basic_assert(response)
