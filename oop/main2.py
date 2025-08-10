# oop/main.py

from library_system import Book, EBook, PrintBook, Library

def main():
    my_library = Library()

    classic_book = Book("Pride and Prejudice", "Jane Austen", 1813, 432)
    ebook = EBook("Snow Crash", "Neal Stephenson", 500)
    print_book = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    my_library.add_book(classic_book)
    my_library.add_book(ebook)
    my_library.add_book(print_book)

    my_library.list_books()

if __name__ == "__main__":
    main()
