from abc import ABC, abstractmethod
from typing import List, Dict, Any
from src.models.book import Book

class IAnalysisStrategy(ABC):
    """
    Abstract Base Class representing an analysis strategy (Strategy Pattern).
    Adheres to Open/Closed Principle (OCP) and Interface Segregation Principle (ISP).
    """

    @abstractmethod
    def execute(self, books: List[Book]) -> Dict[str, Any]:
        """
        Executes analytical computation over the book entities.
        Returns a dictionary containing summary data ready for CLI and Visualization.
        """
        pass

    @abstractmethod
    def get_analysis_name(self) -> str:
        """Returns descriptive name of the analysis."""
        pass