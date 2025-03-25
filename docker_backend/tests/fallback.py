from tests.config import requests
from tests.routes.fallback import Fallback


class Test_Fallback(Fallback):

    def test_get_fallback(self):
        response = requests.get(self.fallback_url)

        self.basic_assert(
            response, 404, json_kws={"error": "Resource not found"}
        )

    def test_post_fallback(self):
        response = requests.post(self.fallback_url)

        self.basic_assert(
            response, 404, json_kws={"error": "Resource not found"}
        )

    def test_put_fallback(self):
        response = requests.put(self.fallback_url)

        self.basic_assert(
            response, 404, json_kws={"error": "Resource not found"}
        )

    def test_patch_fallback(self):
        response = requests.patch(self.fallback_url)

        self.basic_assert(
            response, 404, json_kws={"error": "Resource not found"}
        )

    def test_delete_fallback(self):
        response = requests.delete(self.fallback_url)

        self.basic_assert(
            response, 404, json_kws={"error": "Resource not found"}
        )
