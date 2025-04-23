from tests.config import requests
from tests.routes.authentication import UpdatePassword
from tests.routes.signup import Signup
from tests.routes.login import Login
from tests.utils import generate_user


class Test_Authentication(UpdatePassword):
    def test_authentication_updatepassword(self, DB):
        """Test POST request to /authentication/update-password endpoint
        Update a user's password
        """

        SIGNUP_URL = Signup().signup_url
        LOGIN_URL = Login().login_url

        user = generate_user()
        login_data = {
            "username": user["username"],
            "password": user["password"],
        }

        # Signup a user
        response = requests.post(SIGNUP_URL, json=user)
        self.basic_assert(
            response,
            201,
        )

        # Login with the user
        response = requests.post(LOGIN_URL, json=login_data)
        self.basic_assert(
            response,
            200
        )

        # Update password
        new_password = "new_password"

        response = requests.post(
            self.updatepassword_url,
            json={
                "username": user["username"],
                "oldPassword": user["password"],
                "newPassword": new_password,
            },
        )
        self.basic_assert(response, 200)

        # Login with the using the old password
        response = requests.post(LOGIN_URL, json=login_data)
        self.basic_assert(response, 401)

        # Login with non-existent user
        response = requests.post(
            LOGIN_URL,
            json={
                "username": "non_existent_user",
                "password": "non_existent_password",
            },
        )
        self.basic_assert(response, 404)

        # Login with the updated password
        response = requests.post(
            LOGIN_URL,
            json={
                "username": user["username"],
                "password": new_password,
            },
        )
        self.basic_assert(response, 200)
