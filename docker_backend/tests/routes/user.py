from tests.config import RANDOM
from tests.routes.index import Index


class User(Index):

    @property
    def users_url(self):
        return f"{self.index_url}/users"

    @staticmethod
    def generate_user():
        return {
            "username": RANDOM.user_name(),
            "password": RANDOM.password(),
            "email": RANDOM.email(),
        }
