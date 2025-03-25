from tests.routes.user import User


class Signup(User):

    @property
    def signup_url(self):
        return f"{self.index_url}/signup"
