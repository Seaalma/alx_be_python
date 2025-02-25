class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"

# Derived class for EBooks
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)  # Call the __init__ of the base class
        self.file_size = file_size  # EBook-specific attribute

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

# Derived class for PrintBooks
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)  # Call the __init__ of the base class
        self.page_count = page_count  # PrintBook-specific attribute

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

# Library class demonstrating composition
class Library:
    def __init__(self):
        self.books = []  # List to hold instances of books

    def add_book(self, book):
        self.books.append(book)  # Add any Book, EBook, or PrintBook instance

    def list_books(self):
        for book in self.books:
            print(book)  # Calls the __str__ method of the respective book
