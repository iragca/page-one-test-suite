from routes.config import BASE_URL, requests


class TestIndex:

    def test_get_index(self, setup):
        """Test GET request to / endpoint
        Should return a simple message
        """
        url = f"{BASE_URL}"
        response = requests.get(url)

        assert response.status_code == 200, "Status code should be 200"
        assert type(response.json()) is dict, "Response should be a dictionary"
        assert (
            response.json()["message"] == "Hello World!"
        ), "Message should be Hello World!"
