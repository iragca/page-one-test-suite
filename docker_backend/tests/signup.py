from tests.config import BASE_URL, requests
from tests.routes.signup import Signup


class Test_Signup(Signup):

    def test_signup(self, DB):

        user = self.generate_user()
        random_user = user["username"]

        response = requests.post(self.signup_url, json=user)

        self.basic_assert(
            response,
            201,
            json_kws={"username": random_user, "isVerified": False},
        )

    def test_duplicate_signup(self, DB):
        url = f"{BASE_URL}/signup"

        user = self.generate_user()

        # Make two requests with the same username
        response = requests.post(url, json=user)
        response = requests.post(url, json=user)

        self.basic_assert(
            response, 409, json_kws={"message": "User already exists"}
        )
