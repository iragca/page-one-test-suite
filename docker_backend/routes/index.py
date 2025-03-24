from routes.config import BASE_URL, requests


class TestIndex:

    @property
    def index_url(self):
        return f"{BASE_URL}"

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
