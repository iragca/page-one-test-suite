import pytest
import pymongo

from tests.config import MONGODB_URL
from tests.users import Test_Users, Test_Users_username  # noqa: F401, Ruff linter ignores F401
from tests.signup import Test_Signup  # noqa: F401
from tests.login import Test_Login  # noqa: F401
from tests.index import Test_Index  # noqa: F401
from tests.books import (  # noqa: F401
    Test_Books,  # noqa: F401
    Test_Books_id,  # noqa: F401
    Test_Books_Isbn_isbn,  # noqa: F401
)
from tests.profile import Test_Profile  # noqa: F401
from tests.fallback import Test_Fallback  # noqa: F401


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
