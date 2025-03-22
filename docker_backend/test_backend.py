import requests
from faker import Faker

BASE_URL = "http://localhost:5000"  # Deployed instance


def test_signup():
    url = f"{BASE_URL}/signup"

    random_user = Faker().user_name()

    data = {
        "username": random_user,
        "password": "password",
        "email": "test@email.com"
    }

    response = requests.post(url, json=data)

    assert response.status_code == 201
    assert response.json()["username"] == random_user
    assert not response.json()["isVerified"]

    response = requests.post(url, json=data)

    assert response.status_code == 409
    assert response.json()["message"] == "User already exists"


def test_get_user():
    url = f"{BASE_URL}"
    response = requests.get(url)

    assert response.status_code == 200
    assert response.json()["message"] == "Hello World!"
