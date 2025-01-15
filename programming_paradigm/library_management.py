class Book:
    """A class representing a book in the library."""
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as available."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out

class Library:
    """A class to manage a collection of books in the library."""
    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Add a new book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title."""
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"The book '{title}' has been checked out.")
                    return
                else:
                    print(f"The book '{title}' is already checked out.")
                    return
        print(f"The book '{title}' is not available in the library.")

    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"The book '{title}' has been returned.")
                    return
                else:
                    print(f"The book '{title}' was not checked out.")
                    return
        print(f"The book '{title}' is not part of this library.")

    def list_available_books(self):
        """List all books that are available in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books are currently available.")

