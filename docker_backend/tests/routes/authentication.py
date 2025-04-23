from tests.routes.index import Index


class Authentication(Index):

    @property
    def auth_url(self):
        return self.index_url / "authentication"


class UpdatePassword(Authentication):

    @property
    def updatepassword_url(self):
        return self.auth_url / "update-password"
