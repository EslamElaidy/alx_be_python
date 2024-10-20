# book_class.py

class Book:
    def __init__(self, title, author, year):
        """Constructor to initialize the Book instance."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor called when the object is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """String representation of the Book instance for users."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official representation of the Book instance for developers."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
