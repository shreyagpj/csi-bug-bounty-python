"""
models.py
Core data models for the Library Management System.
"""


class Book:
    """Represents a single book title in the library."""

    def __init__(self, book_id, title, author, total_copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = total_copies

    def __repr__(self):
        return (f"Book({self.book_id}, '{self.title}', "
                f"available={self.available_copies}/{self.total_copies})")


class Member:
    """Represents a library member."""

    def __init__(self, member_id, name, borrowed_books=[]):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = borrowed_books  # list of book_ids currently borrowed

    def __repr__(self):
        return f"Member({self.member_id}, '{self.name}', borrowed={self.borrowed_books})"
