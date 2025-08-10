# oop/library_system.py

class Book:
    """Base class for all books."""
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def info(self) -> str:
        """Return a simple string describing the book."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """Digital book with file size in KB."""
    def __init__(self, title: str, author: str, file_size: int):
        super().__init__(title, author)
        self.file_size = file_size

    def info(self) -> str:
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """Printed book with page count."""
    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count

    def info(self) -> str:
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """A simple library that holds a collection of Book instances."""
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        """Add a Book (or subclass) instance to the library."""
        if not isinstance(book, Book):
            raise TypeError("Only Book instances (or subclasses) can be added.")
        self.books.append(book)

    def list_books(self):
        """Print details of every book in the library."""
        if not self.books:
            print("No books in the library.")
            return
        for book in self.books:
            print(book.info())
