# tests/test_loader.py
import pytest
from src.dataloader.loader_factory import DataLoaderFactory
from src.dataloader.csv_loader import CsvDataLoader
from src.models.book import Book
from src.dataloader.data_store import AppDataStore
from src.dataloader.data_store import AppDataStore



def test_factory_returns_csv_loader():
    """Verify that DataLoaderFactory instantiates a CsvDataLoader correctly."""
    loader = DataLoaderFactory.get_loader("csv")
    assert isinstance(loader, CsvDataLoader)

def test_factory_invalid_type_raises_value_error():
    """Verify that requesting an unsupported loader type raises ValueError."""
    with pytest.raises(ValueError) as exc_info:
        DataLoaderFactory.get_loader("xml")
    assert "Unsupported loader type" in str(exc_info.value)

def test_loader_non_existent_file_raises_exception():
    """Edge Case: Loading from a non-existent file path must raise FileNotFoundError."""
    loader = CsvDataLoader()
    with pytest.raises(FileNotFoundError):
        loader.load_data("data/non_existent_file.csv")

def test_book_model_encapsulation_and_isbn():
    """Verify Book model property getters and missing ISBN identification."""
    book_with_isbn = Book("Title A", "Author A", 2021, "English", "Pub A", "1234567890", "BNB01")
    assert book_with_isbn.title == "Title A"
    assert book_with_isbn.has_isbn() is True

    book_without_isbn = Book("Title B", "Author B", 2022, "French", "Pub B", "", "BNB02")
    assert book_without_isbn.has_isbn() is False
    assert book_without_isbn.isbn is None


def test_singleton_app_data_store():
    """Verify that AppDataStore adheres to Singleton pattern returning identical instance."""
    store1 = AppDataStore()
    store2 = AppDataStore()
    assert store1 is store2



def test_singleton_app_data_store_identity():
    """Verify that AppDataStore adheres to Singleton pattern returning the identical memory instance."""
    store1 = AppDataStore()
    store2 = AppDataStore()
    # Identical memory reference check
    assert store1 is store2
    
    # Verify state sharing across instances
    sample_item = [Book("Test", "Author", 2022, "English", "Pub", "123", "B01")]
    store1.set_books(sample_item)
    assert store2.get_books() == sample_item
    assert store2.is_loaded() is True







