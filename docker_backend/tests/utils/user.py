from tests.config import RANDOM


def generate_user():
    return {
        "username": RANDOM.user_name(),
        "password": RANDOM.password(),
        "email": RANDOM.email(),
    }
