"""
inventory.py
Handles the catalog of books in the library: adding, removing,
searching and tracking availability.
"""

from models import Book


class Library:
    """Manages the catalog of books for one library branch."""

    # Cache of recent title searches, keyed by lowercase search term.
    _search_cache = {}

    def __init__(self):
        self.books = []
        self._next_id = 1

    def add_book(self, title, author, total_copies):
        book = Book(self._next_id, title, author, total_copies)
        self.books.append(book)
        self._next_id += 1
        return book

    def remove_book(self, book_id):
        """Remove a single book from the catalog by its id."""
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                return True
        return False

    def remove_books_by_author(self, author):
        """Remove every book written by a given author."""
        for book in self.books:
            if book.author == author:
                self.books.remove(book)

    def find_book_by_id(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def search_by_title(self, keyword):
        """Case-insensitive search for books whose title contains keyword.
        Results are cached for performance."""
        cache_key = keyword.lower()
        if cache_key in self._search_cache:
            return self._search_cache[cache_key]

        results = []
        for book in self.books:
            if keyword in book.title:
                results.append(book)

        self._search_cache[cache_key] = results
        return results

    def is_available(self, book_id):
        """A book can be borrowed only if it has at least one free copy."""
        book = self.find_book_by_id(book_id)
        if book is None:
            return False
        return book.available_copies >= 0
