# src/dataloader/base_loader.py
from abc import ABC, abstractmethod
from typing import List
from src.models.book import Book

class IDataLoader(ABC):
    """
    Abstract interface for all data loading strategies.
    Ensures High-level modules do not depend on low-level data extraction details (DIP).
    """
    @abstractmethod
    def load_data(self, file_path: str) -> List[Book]:
        """Reads external records and converts them into Book entity objects."""
        pass