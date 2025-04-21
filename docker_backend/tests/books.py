from tests.config import requests
from tests.routes.book import Book
from tests.routes.user import User


class Test_Books(Book):

    # /books

    def test_get_books(self, DB):
        """Test GET request to /books endpoint
        Get all books from the database
        """

        # Checking an empty response
        response = requests.get(self.books_url)
        self.basic_assert(response, 400, data_structure=dict)

        # Checking a correct response
        username = User.generate_user()["username"]
        book = self.generate_book()

        DB.books.insert_one(book)
        DB.users.insert_one({"username": username})
        DB.userbooks.insert_one(
            {"username": username, "isbn_issn": book["isbn_issn"]}
        )

        response = requests.get(self.books_url + f"?username={username}")

        self.basic_assert(response, 200, data_structure=list)
        response_json = response.json()
        assert response_json[0]["isbn_issn"] == book["isbn_issn"]
        assert response_json[0]["owned"] is True

    def test_post_books(self, DB):
        """Test POST request to /books endpoint
        Add a single book to the database
        """
        book = self.generate_book()
        random_title = book["title"]

        response = requests.post(self.books_url, data=book)

        self.basic_assert(
            response,
            201,
            data_structure=dict,
            json_kws={"title": random_title},
        )


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

        self.basic_assert(response, 200, "json")

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

        self.basic_assert(
            response, json_kws={"message": "Book updated successfully"}
        )

    def test_delete_book(self, DB):
        """Test DELETE request to /books/<id> endpoint"
        Delete a single book from the database
        """

        book = self.generate_book()
        random_title = book["title"]

        DB.books.insert_one(book)

        book_id = DB.books.find_one({"title": random_title})["_id"]

        response = requests.delete(self.books_url + f"/{book_id}")

        self.basic_assert(
            response, json_kws={"message": "Book deleted successfully"}
        )


class Test_Books_Isbn_isbn(Book):

    def test_get_books_by_isbn(self, DB):
        """Test GET request to /books/isbn/<isbn> endpoint
        Get a single book by isbn
        """
        book = self.generate_book()
        random_isbn = book["isbn_issn"]

        DB.books.insert_one(book)

        response = requests.get(self.books_url + f"/isbn/{random_isbn}")

        self.basic_assert(response, json_kws={"isbn_issn": random_isbn})


class Test_Book_User_username(Book):

    # books/user/:username

    def test_get_books_by_user(self, DB):

        books = [self.generate_book() for _ in range(3)]
        user = User.generate_user()

        DB.books.insert_many(books)
        DB.users.insert_one(user)
        DB.userbooks.insert_one(
            {"username": user["username"], "isbn_issn": books[1]["isbn_issn"]}
        )

        response = requests.get(self.books_url + f"/user/{user['username']}")

        self.basic_assert(response, 200, data_structure=list)
        response_json = response.json()

        assert response_json[0]["isbn_issn"] == books[1]["isbn_issn"]
        assert response_json[0]["owned"] is True


class Test_Book_user(Book):

    # books/user/

    def test_post_book_to_user(self, DB):
        """Test POST request to /books/user/ endpoint
        Add a book to a user's collection
        """
        book = self.generate_book()
        user = User.generate_user()

        DB.books.insert_one(book)
        DB.users.insert_one(user)

        response = requests.post(
            self.books_url + "/user",
            data={
                "username": user["username"],
                "isbn_issn": book["isbn_issn"],
            },
        )

        self.basic_assert(
            response,
            201,
            data_structure=dict,
            json_kws={"message": "Book added to user successfully"},
        )

    def test_delete_book_from_user(self, DB):
        """Test DELETE request to /books/user/ endpoint
        Remove a book from a user's collection
        """
        book = self.generate_book()
        user = User.generate_user()

        DB.books.insert_one(book)
        DB.users.insert_one(user)
        DB.userbooks.insert_one(
            {"username": user["username"], "isbn_issn": book["isbn_issn"]}
        )

        response = requests.delete(
            self.books_url + "/user",
            data={
                "username": user["username"],
                "isbn_issn": book["isbn_issn"],
            },
        )

        self.basic_assert(
            response,
            200,
            data_structure=dict,
            json_kws={"message": "Book removed from user successfully"},
        )
