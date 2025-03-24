from routes.config import BASE_URL, RANDOM, requests


class TestBooks:

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

    def test_get_books(self, setup):
        """Test GET request to /books endpoint
        Get all books from the database
        """
        response = requests.get(self.books_url)

        assert response.status_code == 200, "Status code should be 200"
        assert type(response.json()) is list, "Response should be a list"

    def test_get_books_by_id(self, setup):
        """Test GET request to /books/<id> endpoint
        Get a single book by id
        """
        db = setup

        book = self.generate_book()
        random_title = book["title"]

        db.books.insert_one(book)

        book_id = db.books.find_one({"title": random_title})["_id"]

        response = requests.get(self.books_url + f"/{book_id}")

        assert response.status_code == 200, "Status code should be 200"
        assert type(response.json()) is dict, "Response should be a dictionary"
        assert (
            response.json()["title"] == random_title
        ), f"Title should be {random_title}"

    def test_post_books(self, setup):
        """Test POST request to /books endpoint
        Add a single book to the database
        """
        book = self.generate_book()
        random_title = book["title"]

        response = requests.post(self.books_url, data=book)

        assert response.status_code == 201, "Status code should be 201"
        assert type(response.json()) is dict, "Response should be a dictionary"
        assert (
            response.json()["title"] == random_title
        ), f"Title should be {random_title}"

    def test_patch_books(self, setup):
        """Test PATCH request to /books/<id> endpoint
        Update a single book in the database
        """
        db = setup

        book = self.generate_book()
        random_title = book["title"]

        db.books.insert_one(book)

        book_id = db.books.find_one({"title": random_title})["_id"]

        response = requests.patch(
            self.books_url + f"/{book_id}", data={"title": "Updated Title"}
        )

        assert response.status_code == 200, "Status code should be 200"
        assert type(response.json()) is dict, "Response should be a dictionary"
        assert (
            response.json()["message"] == "Book updated successfully"
        ), "Message should be Book updated successfully"
