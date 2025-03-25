from tests.config import BASE_URL, RANDOM
from tests.routes.index import Index


class Book(Index):

    @property
    def books_url(self):
        return f"{BASE_URL}/books"

    @staticmethod
    def generate_book():
        return {
            "title": RANDOM.word(),
            "author": RANDOM.name(),
            "genre": RANDOM.word(),
            "year_published": RANDOM.year(),
            "publisher": RANDOM.company(),
            "isbn_issn": RANDOM.isbn13(),
            "cover_photo": RANDOM.image_url(),
        }
