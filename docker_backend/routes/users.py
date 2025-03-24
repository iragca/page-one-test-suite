from routes.config import BASE_URL, RANDOM, requests


class TestUsers:

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

    def test_get_users(self, setup):
        """Test GET request to /users endpoint
        Get all users from the database
        """
        response = requests.get(self.users_url)

        assert response.status_code == 200, "Status code should be 200"
        assert type(response.json()) is list, "Response should be a list"
