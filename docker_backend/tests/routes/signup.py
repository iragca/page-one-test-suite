from tests.config import BASE_URL
from tests.routes.user import User


class Signup(User):

    @property
    def signup_url(self):
        return f"{BASE_URL}/signup"
