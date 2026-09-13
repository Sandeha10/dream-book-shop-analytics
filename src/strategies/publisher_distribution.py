# src/strategies/publisher_distribution.py
from typing import List, Dict, Any
from collections import Counter
from src.models.book import Book
from src.strategies.base_strategy import IAnalysisStrategy

class PublisherDistributionStrategy(IAnalysisStrategy):
    """Computes the volume of books published by prominent publishing houses."""

    def execute(self, books: List[Book]) -> Dict[str, Any]:
        pub_counts = Counter(b.publisher for b in books if b.publisher and b.publisher != "Unknown Publisher")
        top_publishers = pub_counts.most_common(8)

        return {
            "title": self.get_analysis_name(),
            "labels": [item[0] for item in top_publishers],
            "values": [item[1] for item in top_publishers],
            "type": "bar"
        }

    def get_analysis_name(self) -> str:
        return "Books Published by Publisher"