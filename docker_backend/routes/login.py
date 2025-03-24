from routes.config import BASE_URL, requests
from routes.signup import TestSignup


class TestLogin(TestSignup):

    @property
    def login_url(self):
        return f"{BASE_URL}/login"

    def test_login(self, setup):
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
        assert response.status_code == 200
