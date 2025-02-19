

# library_management.py

class Book:
    """Represents a book in the library."""
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """Marks the book as checked out."""
        if self._is_checked_out:
            print(f"'{self.title}' is already checked out.")
        else:
            self._is_checked_out = True
            print(f"'{self.title}' has been checked out.")

    def return_book(self):
        """Marks the book as available again."""
        if not self._is_checked_out:
            print(f"'{self.title}' was not checked out.")
        else:
            self._is_checked_out = False
            print(f"'{self.title}' has been returned.")

    def is_available(self):
        """Returns True if the book is available, False otherwise."""
        return not self._is_checked_out


class Library:
    """Represents a collection of books in the library."""

    def __init__(self):
        self._books = []  # Private list to store book objects

    def add_book(self, book):
        """Adds a book to the library."""
        self._books.append(book)
        print(f"Added '{book.title}' by {book.author} to the library.")

    def check_out_book(self, title):
        """Checks out a book if it's available."""
        for book in self._books:
            if book.title == title:
                book.check_out()
                return
        print(f"Book '{title}' not found in the library.")

    def return_book(self, title):
        """Returns a checked-out book to the library."""
        for book in self._books:
            if book.title == title:
                book.return_book()
                return
        print(f"Book '{title}' not found in the library.")

    def list_available_books(self):
        """Displays all books that are currently available."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books are available.")

