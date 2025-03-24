import pytest
import pymongo

from routes.config import MONGODB_URL
from routes.users import TestUsers
from routes.signup import TestSignup
from routes.login import TestLogin
from routes.index import TestIndex
from routes.books import TestBooks


@pytest.fixture(autouse=True)
def setup():
    client = pymongo.MongoClient(MONGODB_URL)
    db = client["pageone"]

    yield db

    db.users.delete_many({})
    db.credentials.delete_many({})
    db.userbooks.delete_many({})
    db.books.delete_many({})

    client.close()


if __name__ == "__main__":
    pytest.main()
