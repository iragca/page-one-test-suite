import os

import requests  # noqa: F401
from faker import Faker

BASE_URL = os.getenv("BASE_URL", "http://localhost:5000")
MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27017/pageone")
RANDOM = Faker()
