from tests.config import BASE_URL, RANDOM


class User:

    @property
    def users_url(self):
        return f"{BASE_URL}/users"

    @staticmethod
    def generate_user():
        return {
            "username": RANDOM.user_name(),
            "password": RANDOM.password(),
            "email": RANDOM.email(),
        }
