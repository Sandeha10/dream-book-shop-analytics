# src/models/book.py

class Book:
    """
    Represents a single bibliographic book entity from the British National Bibliography (BNB).
    Adheres to the Single Responsibility Principle by solely managing entity state.
    """
    def __init__(self, title: str, author: str, pub_year: int, language: str, 
                 publisher: str, isbn: str, bnb_id: str):
        self._title = title.strip() if title else "Untitled"
        self._author = author.strip() if author else "Unknown Author"
        self._pub_year = pub_year
        self._language = language.strip() if language else "Unknown"
        self._publisher = publisher.strip() if publisher else "Unknown Publisher"
        self._isbn = isbn.strip() if (isbn and str(isbn).strip().lower() not in ['nan', 'none', '']) else None
        self._bnb_id = bnb_id.strip() if bnb_id else "UNKNOWN"

    @property
    def title(self) -> str:
        return self._title

    @property
    def author(self) -> str:
        return self._author

    @property
    def pub_year(self) -> int:
        return self._pub_year

    @property
    def language(self) -> str:
        return self._language

    @property
    def publisher(self) -> str:
        return self._publisher

    @property
    def isbn(self) -> str:
        return self._isbn

    @property
    def bnb_id(self) -> str:
        return self._bnb_id

    def has_isbn(self) -> bool:
        """Returns True if the book contains a valid ISBN string, False otherwise."""
        return self._isbn is not None

    def __repr__(self) -> str:
        return f"<Book {self._bnb_id}: '{self._title}' by {self._author} ({self._pub_year})>"