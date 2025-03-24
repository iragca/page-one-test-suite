from routes.config import BASE_URL, FAKER, requests


class TestUsers:

    @property
    def users_url(self):
        return f"{BASE_URL}/users"

    def _generate_user(self):
        random_user = FAKER.user_name()
        random_password = FAKER.password()
        random_email = FAKER.email()

        user = {
            "username": random_user,
            "password": random_password,
            "email": random_email,
        }

        return user

    def test_get_users(self, setup):
        """Test GET request to /users endpoint
        Get all users from the database
        """
        response = requests.get(self.users_url)

        assert response.status_code == 200, "Status code should be 200"
        assert type(response.json()) is list, "Response should be a list"
