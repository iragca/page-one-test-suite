from tests.config import requests
from tests.routes.index import Index


class TestIndex(Index):

    def test_get_index(self, DB):
        """Test GET request to / endpoint
        Should return a simple message
        """
        response = requests.get(self.index_url)

        assert response.status_code == 200, "Status code should be 200"
        assert type(response.json()) is dict, "Response should be a dictionary"
        assert (
            response.json()["message"] == "Hello World!"
        ), "Message should be Hello World!"
