# flake8: noqa

import pymongo
import pytest
import requests
from loguru import logger
from tests.books import (  
    Test_Book_User_username, 
    Test_Book_user,
    Test_Books, 
    Test_Books_id, 
    Test_Books_Isbn_isbn,  
)
from tests.config import BASE_URL, MONGODB_URL
from tests.fallback import Test_Fallback  
from tests.index import Test_Index  
from tests.login import Test_Login  
from tests.profile import Test_Profile  
from tests.signup import Test_Signup  
from tests.users import (
    Test_Users,
    Test_Users_username,
)


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


def ping_webapp(host):
    """
    Sends a GET request to the specified host to check its availability.

    Args:
        host (str): The URL of the host to ping.

    Returns:
        bool:
            True if the host is reachable (HTTP status code 200),
            False otherwise.

    Logs:
        Logs an error message if the request fails or the host is unreachable.
    """
    try:
        response = requests.get(host)
        response.raise_for_status()
        return True

    except requests.exceptions.RequestException as e:
        logger.error(f"Could not ping {host}: {e}")
        return False


def ping_mongodb(host):
    """Pings a MongoDB server to check its availability.

        host (str): The hostname or URI of the MongoDB server to ping.

        bool: True if the server is reachable and responds to the ping command,
              False otherwise.

    Raises:
        pymongo.errors.ServerSelectionTimeoutError:
            If the server is not reachable within the timeout period.
    """
    try:
        client = pymongo.MongoClient(host)
        client.admin.command("ping")
        client.close()
        return True

    except pymongo.errors.ServerSelectionTimeoutError as e:
        logger.error(f"Could not ping {host}: {e}")
        return False


if __name__ == "__main__":

    # Ping the server and MongoDB
    if ping_webapp(BASE_URL) and ping_mongodb(MONGODB_URL):
        pytest.main()

    else:  # If the server or MongoDB is not reachable, stop the tests
        logger.error("Stopping tests")
        exit(1)
