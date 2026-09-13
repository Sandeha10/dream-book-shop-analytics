# src/strategies/language_by_year.py
from typing import List, Dict, Any
from collections import defaultdict
from src.models.book import Book
from src.strategies.base_strategy import IAnalysisStrategy

class LanguageByYearStrategy(IAnalysisStrategy):
    """Analyzes publication volumes per year broken down by top languages."""

    def execute(self, books: List[Book]) -> Dict[str, Any]:
        # Filter valid records
        matrix = defaultdict(lambda: defaultdict(int))
        years = set()
        languages = set()

        for b in books:
            if b.pub_year > 0 and b.language != "Unknown":
                matrix[b.pub_year][b.language] += 1
                years.add(b.pub_year)
                languages.add(b.language)

        sorted_years = sorted(list(years))
        top_languages = sorted(list(languages))[:4]  # Limit to 4 for clean CLI representation

        return {
            "title": self.get_analysis_name(),
            "years": [str(y) for y in sorted_years],
            "languages": top_languages,
            "matrix": matrix,
            "type": "grouped_bar"
        }

    def get_analysis_name(self) -> str:
        return "Books Published per Year Categorized by Language"