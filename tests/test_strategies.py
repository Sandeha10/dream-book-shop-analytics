# tests/test_strategies.py
import pytest
from src.models.book import Book
from src.strategies.publication_trends import PublicationTrendsStrategy
from src.strategies.top_authors import TopAuthorsStrategy
from src.strategies.language_distribution import LanguageDistributionStrategy
from src.strategies.publisher_distribution import PublisherDistributionStrategy
from src.strategies.missing_isbn import MissingIsbnStrategy
from src.strategies.language_by_year import LanguageByYearStrategy

@pytest.fixture
def sample_books():
    """Fixture providing representative mock book data for unit tests."""
    return [
        Book("Book 1", "Author Alpha", 2020, "English", "Publisher One", "978-1", "BNB001"),
        Book("Book 2", "Author Alpha", 2020, "English", "Publisher One", "978-2", "BNB002"),
        Book("Book 3", "Author Beta", 2021, "French", "Publisher Two", "", "BNB003"),        # Missing ISBN
        Book("Book 4", "Author Gamma", 2021, "English", "Publisher One", "978-3", "BNB004"),
        Book("Book 5", "Author Beta", 2022, "German", "Publisher Three", None, "BNB005")      # Missing ISBN
    ]

def test_missing_isbn_strategy_calculation(sample_books):
    """Verify that MissingIsbnStrategy accurately calculates counts and percentages."""
    strategy = MissingIsbnStrategy()
    result = strategy.execute(sample_books)
    
    assert result["total"] == 5
    assert result["missing_count"] == 2
    assert result["missing_pct"] == 40.0

def test_top_authors_strategy(sample_books):
    """Verify author ranking logic identifies most frequent authors."""
    strategy = TopAuthorsStrategy()
    result = strategy.execute(sample_books)
    
    # Author Alpha (2 books) and Author Beta (2 books) must lead
    assert "Author Alpha" in result["labels"]
    assert "Author Beta" in result["labels"]
    assert result["values"][0] == 2

def test_publication_trends_strategy(sample_books):
    """Verify publication years are counted and ordered chronologically."""
    strategy = PublicationTrendsStrategy()
    result = strategy.execute(sample_books)
    
    assert result["labels"] == ["2020", "2021", "2022"]
    assert result["values"] == [2, 2, 1]

def test_language_distribution_strategy(sample_books):
    """Verify language breakdown counts."""
    strategy = LanguageDistributionStrategy()
    result = strategy.execute(sample_books)
    
    assert "English" in result["labels"]
    assert "French" in result["labels"]

# --- EDGE CASE TESTS (Critical for Distinction D2) ---

def test_strategy_with_empty_dataset():
    """Edge Case: Strategies must handle an empty list without crashing."""
    empty_list = []
    
    isbn_strategy = MissingIsbnStrategy()
    result = isbn_strategy.execute(empty_list)
    assert result["total"] == 0
    assert result["missing_pct"] == 0.0

    authors_strategy = TopAuthorsStrategy()
    result_authors = authors_strategy.execute(empty_list)
    assert result_authors["labels"] == []
    assert result_authors["values"] == []

def test_strategy_with_invalid_year():
    """Edge Case: Books with year 0 or negative years must be excluded from trends."""
    corrupted_books = [
        Book("Corrupt 1", "Author X", 0, "English", "Pub A", "123", "B01"),
        Book("Corrupt 2", "Author Y", -5, "English", "Pub B", "456", "B02"),
        Book("Valid 1", "Author Z", 2023, "English", "Pub C", "789", "B03")
    ]
    strategy = PublicationTrendsStrategy()
    result = strategy.execute(corrupted_books)
    
    # Only the valid year 2023 should appear
    assert result["labels"] == ["2023"]
    assert result["values"] == [1]


def test_publisher_distribution_strategy(sample_books):
    """Verify publisher aggregation and ranking accuracy."""
    strategy = PublisherDistributionStrategy()
    result = strategy.execute(sample_books)
    
    assert "Publisher One" in result["labels"]
    pub_one_index = result["labels"].index("Publisher One")
    assert result["values"][pub_one_index] == 3

def test_language_by_year_strategy(sample_books):
    """Verify cross-dimensional aggregation of books per year categorized by language."""
    strategy = LanguageByYearStrategy()
    result = strategy.execute(sample_books)
    
    assert "2020" in result["years"]
    assert "English" in result["languages"]
    assert result["matrix"][2020]["English"] == 2
    assert result["matrix"][2021]["French"] == 1