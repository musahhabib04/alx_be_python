class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.year})"


class EBook(Book):
    def __init__(self, title, author, year, filesize):
        super().__init__(title, author, year)
        self.filesize = filesize

    def __str__(self):
        return f"E-Book: '{self.title}' by {self.author} ({self.year}), {self.filesize}MB"


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

    def __str__(self):
        if not self.books:
            return "The library is empty."
        return "\n".join(str(book) for book in self.books)
