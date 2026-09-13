# src/strategies/missing_isbn.py
from typing import List, Dict, Any
from src.models.book import Book
from src.strategies.base_strategy import IAnalysisStrategy

class MissingIsbnStrategy(IAnalysisStrategy):
    """Calculates the count and percentage of records lacking a valid ISBN."""

    def execute(self, books: List[Book]) -> Dict[str, Any]:
        total_books = len(books)
        if total_books == 0:
            return {"title": self.get_analysis_name(), "missing_count": 0, "total": 0, "missing_pct": 0.0, "type": "summary"}

        missing_count = sum(1 for b in books if not b.has_isbn())
        missing_pct = (missing_count / total_books) * 100

        return {
            "title": self.get_analysis_name(),
            "labels": ["With ISBN", "Missing ISBN"],
            "values": [total_books - missing_count, missing_count],
            "missing_count": missing_count,
            "total": total_books,
            "missing_pct": round(missing_pct, 2),
            "type": "donut"
        }

    def get_analysis_name(self) -> str:
        return "Missing ISBN Analysis"