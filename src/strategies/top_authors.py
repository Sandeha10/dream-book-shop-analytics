# src/strategies/top_authors.py
from typing import List, Dict, Any
from collections import Counter
from src.models.book import Book
from src.strategies.base_strategy import IAnalysisStrategy

class TopAuthorsStrategy(IAnalysisStrategy):
    """Identifies the top 5 authors with the highest volume of publications."""

    def execute(self, books: List[Book]) -> Dict[str, Any]:
        author_counts = Counter(b.author for b in books if b.author and b.author != "Unknown Author")
        top_5 = author_counts.most_common(5)

        return {
            "title": self.get_analysis_name(),
            "labels": [item[0] for item in top_5],
            "values": [item[1] for item in top_5],
            "type": "bar"
        }

    def get_analysis_name(self) -> str:
        return "Top 5 Most Prolific Authors"