# src/dataloader/data_store.py
from typing import List, Optional
from src.models.book import Book

class AppDataStore:
    """
    Singleton Pattern Implementation.
    Ensures that only a single instance of the Book repository exists in memory across the CLI lifecycle.
    """
    _instance: Optional['AppDataStore'] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AppDataStore, cls).__new__(cls)
            cls._instance._books = []
            cls._instance._is_loaded = False
        return cls._instance

    def set_books(self, books: List[Book]) -> None:
        self._books = books
        self._is_loaded = True

    def get_books(self) -> List[Book]:
        return self._books

    def is_loaded(self) -> bool:
        return self._is_loaded