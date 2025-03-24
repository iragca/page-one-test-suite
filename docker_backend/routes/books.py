from routes.config import BASE_URL, FAKER, requests


class TestBooks:

    @staticmethod
    def generate_book():
        random_title = FAKER.word()
        random_author = FAKER.name()
        random_genre = FAKER.word()
        random_year = FAKER.year()
        random_publisher = FAKER.company()
        random_isbn = FAKER.isbn13()
        random_cover_photo = FAKER.image_url()

        book = {
            "title": random_title,
            "author": random_author,
            "genre": random_genre,
            "year_published": random_year,
            "publisher": random_publisher,
            "isbn_issn": random_isbn,
            "cover_photo": random_cover_photo,
        }

        return book

    def test_get_books(self, setup):
        """Test GET request to /books endpoint
        Get all books from the database
        """
        url = f"{BASE_URL}/books"
        response = requests.get(url)

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

        url = f"{BASE_URL}/books/{book_id}"
        response = requests.get(url)

        assert response.status_code == 200, "Status code should be 200"
        assert type(response.json()) is dict, "Response should be a dictionary"
        assert (
            response.json()["title"] == random_title
        ), f"Title should be {random_title}"

    def test_post_books(self, setup):
        """Test POST request to /books endpoint
        Add a single book to the database
        """
        url = f"{BASE_URL}/books"

        book = self.generate_book()
        random_title = book["title"]

        response = requests.post(url, data=book)

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

        url = f"{BASE_URL}/books/{book_id}"
        response = requests.patch(url, data={"title": "Updated Title"})

        assert response.status_code == 200, "Status code should be 200"
        assert type(response.json()) is dict, "Response should be a dictionary"
        assert (
            response.json()["message"] == "Book updated successfully"
        ), "Message should be Book updated successfully"
