from tests.config import BASE_URL, requests
from tests.routes.signup import Signup


class TestLogin(Signup):

    @property
    def login_url(self):
        return f"{BASE_URL}/login"

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
        assert response.status_code == 200
