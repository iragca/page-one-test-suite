from tests.routes.user import User


class Profile(User):

    @property
    def profile_url(self):
        return f"{self.index_url}/profile"
