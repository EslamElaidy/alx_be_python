# Book class
class Book:
    def __init__(self, title, author):
        self.title = title  # Public attribute
        self.author = author  # Public attribute
        self._is_checked_out = False  # Private attribute, initially book is not checked out

    def check_out(self):
        if not self._is_checked_out:  # If the book is available, mark as checked out
            self._is_checked_out = True
            return True
        return False  # Return False if the book is already checked out

    def return_book(self):
        if self._is_checked_out:  # If the book is checked out, mark as returned
            self._is_checked_out = False
            return True
        return False  # Return False if the book was not checked out

    def is_available(self):
        return not self._is_checked_out  # Return availability of the book

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}"

# Library class
class Library:
    def __init__(self):
        self._books = []  # Private list to store Book instances

    def add_book(self, book):
        self._books.append(book)  # Add a Book instance to the list

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.is_available():  # Find book by title and check availability
                book.check_out()
                print(f'Checked out "{book.title}" by {book.author}.')
                return True
        print(f'Book "{title}" is either not available or already checked out.')
        return False

    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_available():  # Find book by title and check if it's checked out
                book.return_book()
                print(f'Returned "{book.title}".')
                return True
        print(f'Book "{title}" was not checked out.')
        return False

    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]  # List only available books
        if available_books:
            print("Available books:")
            for book in available_books:
                print(f"- {book}")
        else:
            print("No books available at the moment.")
