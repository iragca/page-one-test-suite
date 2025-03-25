from tests.config import RANDOM
from tests.routes.index import Index


class Fallback(Index):

    @property
    def fallback_url(self):
        return f"{self.index_url}/{RANDOM.word()}"
