# src/strategies/publication_trends.py
from typing import List, Dict, Any
from collections import Counter
from src.models.book import Book
from src.strategies.base_strategy import IAnalysisStrategy

class PublicationTrendsStrategy(IAnalysisStrategy):
    """Calculates total book publications grouped by year."""

    def execute(self, books: List[Book]) -> Dict[str, Any]:
        valid_years = [b.pub_year for b in books if b.pub_year > 0]
        year_counts = Counter(valid_years)
        # Sort chronologically by year
        sorted_years = sorted(year_counts.items(), key=lambda x: x[0])

        return {
            "title": self.get_analysis_name(),
            "labels": [str(item[0]) for item in sorted_years],
            "values": [item[1] for item in sorted_years],
            "type": "line"
        }

    def get_analysis_name(self) -> str:
        return "Publication Trends Over Time"