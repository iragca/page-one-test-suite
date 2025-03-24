import os

import requests
from faker import Faker

BASE_URL = os.getenv("BASE_URL", "http://localhost:5000")
MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27017/pageone")
RANDOM = Faker()

print(f"{BASE_URL=}, {MONGODB_URL=}")
