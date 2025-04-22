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

        non_existent_user = {
            "username": "non_existent_user",
            "password": "non_existent_password",
        }

        # Checking if a user is not signed up
        response = requests.post(self.login_url, json=non_existent_user)
        self.basic_assert(response, 404)

        # Signup a user
        requests.post(self.signup_url, json=user)

        # Wrong password
        response = requests.post(
            self.login_url,
            json={
                "username": user["username"],
                "password": "wrong_password",
            },
        )
        self.basic_assert(response, 401)

        # Correct password
        response = requests.post(self.login_url, json=login_data)
        self.basic_assert(response, 200)
