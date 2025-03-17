class Book:
    """Base class representing a book with a title and author."""
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """Derived class representing an eBook with a file size."""
    def __init__(self, title, author, file_size):
        super().__init__(title, author)  # Call the base class constructor
        self.file_size = file_size  # Unique attribute for EBook

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """Derived class representing a printed book with a page count."""
    def __init__(self, title, author, page_count):
        super().__init__(title, author)  # Call the base class constructor
        self.page_count = page_count  # Unique attribute for PrintBook

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """Library class that manages a collection of books."""
    def __init__(self):
        self.books = []  # List to store Book, EBook, and PrintBook instances

    def add_book(self, book):
        """Adds a book (Book, EBook, or PrintBook) to the library."""
        if isinstance(book, Book):  # Ensure only Book or its subclasses are added
            self.books.append(book)
        else:
            print("Only books can be added to the library.")

    def list_books(self):
        """Prints details of each book in the library."""
        for book in self.books:
            print(book)  # Calls __str__() for each book
