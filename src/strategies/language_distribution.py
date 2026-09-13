# src/strategies/language_distribution.py
from typing import List, Dict, Any
from collections import Counter
from src.models.book import Book
from src.strategies.base_strategy import IAnalysisStrategy

class LanguageDistributionStrategy(IAnalysisStrategy):
    """Computes the distribution of publications across different languages."""

    def execute(self, books: List[Book]) -> Dict[str, Any]:
        lang_counts = Counter(b.language for b in books if b.language and b.language != "Unknown")
        # Top 5 languages and group the rest as 'Other'
        common = lang_counts.most_common(5)
        top_keys = {item[0] for item in common}
        other_sum = sum(count for lang, count in lang_counts.items() if lang not in top_keys)

        labels = [item[0] for item in common]
        values = [item[1] for item in common]
        if other_sum > 0:
            labels.append("Other")
            values.append(other_sum)

        return {
            "title": self.get_analysis_name(),
            "labels": labels,
            "values": values,
            "type": "pie"
        }

    def get_analysis_name(self) -> str:
        return "Language Distribution of Books"