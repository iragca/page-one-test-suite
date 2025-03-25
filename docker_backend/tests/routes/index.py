from tests.config import BASE_URL, requests


class Index:

    @property
    def index_url(self):
        return f"{BASE_URL}"

    @staticmethod
    def basic_assert(
        response: requests.models.Response,
        status_code: int = 200,
        content_type: str = "json",
        data_structure: dict | list = dict,
        json_kws: dict = None,
    ) -> None:
        """Basic assertions for API tests."""

        assert (
            response.status_code == status_code
        ), f"Expected: {status_code}, Got: {response.status_code}"

        assert content_type in response.headers["Content-Type"], (
            f"Expected: {content_type}, "
            f"Got: {response.headers['Content-Type']}"
        )

        assert (
            type(response.json()) is data_structure
        ), f"Response should be a {data_structure}"

        if json_kws:
            for key, value in json_kws.items():

                assert response.json()[key] == value, (
                    f"Expected: {key}={value},"
                    f" Got: {key}={response.json()[key]}"
                )
