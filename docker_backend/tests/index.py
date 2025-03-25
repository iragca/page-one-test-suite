from tests.config import requests
from tests.routes.index import Index


class Test_Index(Index):

    def test_get_index(self, DB):
        """Test GET request to / endpoint
        Should return a simple message
        """
        response = requests.get(self.index_url)

        self.basic_assert(response, json_kws={"message": "Hello World!"})
