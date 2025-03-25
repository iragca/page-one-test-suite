from tests.config import BASE_URL


class Index:

    @property
    def index_url(self):
        return f"{BASE_URL}"
