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

        assert response.status_code == 200

        assert (
            "json" in response.headers["Content-Type"]
        ), "Response should be JSON"

        assert response.json()["username"] == new_user["username"], (
            f"Expected: {new_user['username']},"
            f" Got: {response.json()['username']}"
        )

    def test_delete_profile(self, DB):
        """Test DELETE request to /profile endpoint"""

        user = self.generate_user()
        DB.users.insert_one(user)

        # 404 error
        response = requests.delete(
            self.profile_url, cookies={"username": "wrong_username"}
        )

        assert response.status_code == 404
        assert (
            "json" in response.headers["Content-Type"]
        ), "Response should be JSON"
        assert response.json()["message"] == "User not found", (
            f"Expected: User not found," f" Got: {response.json()['message']}"
        )

        # 200 success
        response = requests.delete(
            self.profile_url, cookies={"username": user["username"]}
        )

        assert response.status_code == 200
        assert (
            "json" in response.headers["Content-Type"]
        ), "Response should be JSON"
        assert response.json()["username"] == user["username"], (
            "Expected: the object of the deleted user,"
            f" Got: {response.json()=}"
        )
