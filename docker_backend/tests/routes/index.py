from tests.config import BASE_URL


class Index:

    @property
    def index_url(self):
        return f"{BASE_URL}"

    @staticmethod
    def basic_assert(response, status_code, content_type, json_kws=None):
        """Basic assertions for API tests."""

        assert (
            response.status_code == status_code
        ), f"Expected: {status_code}, Got: {response.status_code}"
        assert content_type in response.headers["Content-Type"], (
            f"Expected: {content_type}, "
            f"Got: {response.headers['Content-Type']}"
        )

        if json_kws:
            for key, value in json_kws.items():
                assert (
                    response.json()[key] == value
                ), f"Expected: {value}, Got: {response.json()[key]}"
