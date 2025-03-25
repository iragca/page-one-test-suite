from tests.config import requests
from tests.routes.profile import Profile


class Test_Profile(Profile):

    # /profile

    def test_get_profile(self, DB):
        """Test GET request to /profile endpoint"""

        user = self.generate_user()
        DB.users.insert_one(user)

        response = requests.get(
            self.profile_url, cookies={"username": user["username"]}
        )

        assert response.status_code == 200
        assert (
            "json" in response.headers["Content-Type"]
        ), "Response should be JSON"
        assert (
            response.json()["username"] == user["username"]
        ), f"Expected: {user['username']}, Got: {response.json()['username']}"

    def test_put_profile(self, DB):
        """Test PUT request to /profile endpoint"""

        user = self.generate_user()
        DB.users.insert_one(user)

        new_user = self.generate_user()

        response = requests.put(
            self.profile_url,
            json=new_user,
            cookies={"username": user["username"]},
        )

        self.basic_assert(
            response, json_kws={"username": new_user["username"]}
        )

    def test_delete_profile(self, DB):
        """Test DELETE request to /profile endpoint"""

        user = self.generate_user()
        DB.users.insert_one(user)

        # 404 error
        response = requests.delete(
            self.profile_url, cookies={"username": "wrong_username"}
        )

        self.basic_assert(
            response, 404, json_kws={"message": "User not found"}
        )

        # 200 success
        response = requests.delete(
            self.profile_url, cookies={"username": user["username"]}
        )

        self.basic_assert(response, json_kws={"username": user["username"]})
