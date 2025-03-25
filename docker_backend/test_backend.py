import pytest
import pymongo

from tests.config import MONGODB_URL
from tests.users import TestUsers  # noqa: F401, Ruff linter ignores F401
from tests.signup import TestSignup  # noqa: F401
from tests.login import TestLogin  # noqa: F401
from tests.index import TestIndex  # noqa: F401
from tests.books import TestBooks  # noqa: F401


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
