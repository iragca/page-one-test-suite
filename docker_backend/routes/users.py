from routes.config import BASE_URL, RANDOM, requests


class Users:

    @property
    def users_url(self):
        return f"{BASE_URL}/users"

    @staticmethod
    def generate_user():
        return {
            "username": RANDOM.user_name(),
            "password": RANDOM.password(),
            "email": RANDOM.email(),
        }


class TestUsers(Users):
    def test_get_users(self, DB):
        """Test GET request to /users endpoint
        Get all users from the database
        """
        response = requests.get(self.users_url)

        assert response.status_code == 200, "Status code should be 200"
        assert type(response.json()) is list, "Response should be a list"

    def test_get_a_user(self, DB):
        """Test GET request to /users/<username> endpoint
        Get a user from the database
        """
        user = self.generate_user()
        DB.users.insert_one(user)

        response = requests.get(f"{self.users_url}/{user['username']}")

        assert response.status_code == 200, "Status code should be 200"
        assert type(response.json()) is dict, "Response should be a dictionary"
        assert (
            "json" in response.headers["Content-Type"]
        ), "Content-Type should be application/json"
        assert (
            response.json()["username"] == user["username"]
        ), f"Response should be the {user['username']=}"
