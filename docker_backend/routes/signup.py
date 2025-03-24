from routes.config import BASE_URL, requests
from routes.users import TestUsers


class TestSignup(TestUsers):

    @property
    def signup_url(self):
        return f"{BASE_URL}/signup"

    def test_signup(self, setup):

        user = self._generate_user()
        random_user = user["username"]

        response = requests.post(self.signup_url, json=user)

        assert type(response.json()) is dict, "Response should be a dictionary"
        assert response.status_code == 201, "Status code should be 201"
        assert (
            response.json()["username"] == random_user
        ), f"Username should be {random_user}"
        assert not response.json()["isVerified"], "User should not be verified"

    def test_duplicate_signup(self, setup):
        url = f"{BASE_URL}/signup"

        user = self._generate_user()

        # Make two requests with the same username
        response = requests.post(url, json=user)
        response = requests.post(url, json=user)

        assert response.status_code == 409
        assert response.json()["message"] == "User already exists"
