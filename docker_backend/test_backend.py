import pytest
import pymongo

from routes.config import MONGODB_URL
from routes.users import TestUsers  # noqa: F401, Ruff linter ignores F401
from routes.signup import TestSignup  # noqa: F401
from routes.login import TestLogin  # noqa: F401
from routes.index import TestIndex  # noqa: F401
from routes.books import TestBooks  # noqa: F401


@pytest.fixture(autouse=True)
def DB():
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
