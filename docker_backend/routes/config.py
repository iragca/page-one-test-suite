import requests
from faker import Faker

BASE_URL = "http://localhost:5000"
MONGODB_URL = "mongodb://localhost:27017/"
RANDOM = Faker()

print(f"{BASE_URL=}, {MONGODB_URL=}")
