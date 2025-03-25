from tests.config import requests
from tests.routes.book import Book


class Test_Books(Book):

    # /books

    def test_get_books(self, DB):
        """Test GET request to /books endpoint
        Get all books from the database
        """
        response = requests.get(self.books_url)

        assert response.status_code == 200, "Status code should be 200"
        assert type(response.json()) is list, "Response should be a list"

    def test_post_books(self, DB):
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


class Test_Books_id(Book):

    def test_get_books_by_id(self, DB):
        """Test GET request to /books/<id> endpoint
        Get a single book by id
        """

        book = self.generate_book()
        random_title = book["title"]

        DB.books.insert_one(book)

        book_id = DB.books.find_one({"title": random_title})["_id"]

        response = requests.get(self.books_url + f"/{book_id}")

        assert response.status_code == 200, "Status code should be 200"
        assert type(response.json()) is dict, "Response should be a dictionary"
        assert (
            response.json()["title"] == random_title
        ), f"Title should be {random_title}"

    def test_patch_book(self, DB):
        """Test PATCH request to /books/<id> endpoint
        Update a single book in the database
        """

        book = self.generate_book()
        random_title = book["title"]

        DB.books.insert_one(book)

        book_id = DB.books.find_one({"title": random_title})["_id"]

        response = requests.patch(
            self.books_url + f"/{book_id}", data={"title": "Updated Title"}
        )

        assert response.status_code == 200, "Status code should be 200"
        assert type(response.json()) is dict, "Response should be a dictionary"
        assert (
            response.json()["message"] == "Book updated successfully"
        ), "Message should be Book updated successfully"

    def test_delete_book(self, DB):
        """Test DELETE request to /books/<id> endpoint"
        Delete a single book from the database
        """

        book = self.generate_book()
        random_title = book["title"]

        DB.books.insert_one(book)

        book_id = DB.books.find_one({"title": random_title})["_id"]

        response = requests.delete(self.books_url + f"/{book_id}")

        assert response.status_code == 200, "Status code should be 200"
        assert type(response.json()) is dict, "Response should be a dictionary"
        assert (
            response.json()["message"] == "Book deleted successfully"
        ), "Message should be Book deleted successfully"


class Test_Books_Isbn_isbn(Book):

    def test_get_books_by_isbn(self, DB):
        """Test GET request to /books/isbn/<isbn> endpoint
        Get a single book by isbn
        """
        book = self.generate_book()
        random_isbn = book["isbn_issn"]

        DB.books.insert_one(book)

        response = requests.get(self.books_url + f"/isbn/{random_isbn}")

        assert response.status_code == 200, "Status code should be 200"
        assert (
            "json" in response.headers["Content-Type"]
        ), "Content-Type should be json"
        assert type(response.json()) is dict, "Response should be a dictionary"
        assert (
            response.json()["isbn_issn"] == random_isbn
        ), f"ISBN should be {random_isbn}"
