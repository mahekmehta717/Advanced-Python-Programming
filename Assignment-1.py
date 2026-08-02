class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(self.title, "borrowed successfully")
        else:
            print(self.title, "is already borrowed")

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(self.title, "returned successfully")
        else:
            print(self.title, "was not borrowed")


class Patron:
    def __init__(self, name, patron_id):
        self.name = name
        self.patron_id = patron_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.is_borrowed:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            print("Book not available")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print(self.name, "did not borrow this book")


class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, book):
        self.books.append(book)

    def register_patron(self, patron):
        self.patrons.append(patron)

    def borrow_book(self, patron, book):
        patron.borrow_book(book)

    def return_book(self, patron, book):
        patron.return_book(book)


def main():
    library = Library()

    book1 = Book("Python Basics", "John", "101")
    book2 = Book("Data Science", "Alice", "102")

    library.add_book(book1)
    library.add_book(book2)

    patron1 = Patron("Rahul", 1)
    patron2 = Patron("Priya", 2)

    library.register_patron(patron1)
    library.register_patron(patron2)

    library.borrow_book(patron1, book1)
    library.borrow_book(patron2, book2)

    library.return_book(patron1, book1)

    print("Books in Library:")
    for book in library.books:
        print(book.title, "-", "Borrowed" if book.is_borrowed else "Available")


if __name__ == "__main__":
    main()
