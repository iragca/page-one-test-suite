from tests.routes.signup import Signup


class Login(Signup):

    @property
    def login_url(self):
        return f"{self.index_url}/login"
