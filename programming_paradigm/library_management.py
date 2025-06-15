# library_management.py

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # private attribute

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []  # private list of books

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                print(f"Book '{title}' checked out successfully.")
                return
        print(f"Book '{title}' is either not available or already checked out.")

    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                print(f"Book '{title}' returned successfully.")
                return
        print(f"Book '{title}' was not checked out or does not exist.")

    def list_available_books(self):
        available = [book for book in self._books if book.is_available()]
        if not available:
            print("No books available.")
        for book in available:
            print(f"{book.title} by {book.author}")