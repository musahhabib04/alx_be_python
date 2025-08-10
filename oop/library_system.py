class Book:
    def __init__(self, title, author, year, page_count):
        self.title = title
        self.author = author
        self.year = year
        self.page_count = page_count

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year}) - {self.page_count} pages"


class EBook(Book):
    def __init__(self, title, author, year, filesize):
        super().__init__(title, author, year)
        self.filesize = filesize

    def __str__(self):
        return f"{super().__str__()} [File size: {self.file_size}MB]"


class PrintBook(Book):
    def __init__(self, title, author, year, pages):
        super().__init__(title, author, year)
        self.pages = pages

    def __str__(self):
        return f"Print Book: '{self.title}' by {self.author} ({self.year}), {self.pages} pages"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(book)  # Uses each book’s __str__ method
