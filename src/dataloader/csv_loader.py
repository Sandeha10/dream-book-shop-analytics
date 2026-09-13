# src/dataloader/csv_loader.py
import pandas as pd
from typing import List
from src.models.book import Book
from src.dataloader.base_loader import IDataLoader

class CsvDataLoader(IDataLoader):
    """
    Concrete implementation of IDataLoader for reading CSV bibliographic datasets.
    Handles data cleansing, type conversions, and missing record scenarios.
    """
    def load_data(self, file_path: str) -> List[Book]:
        try:
            df = pd.read_csv(file_path)
        except Exception as e:
            raise FileNotFoundError(f"Error reading dataset at '{file_path}': {e}")

        books: List[Book] = []

        for _, row in df.iterrows():
            # Robust Year parsing
            raw_year = row.get('publication date')
            try:
                pub_year = int(float(raw_year))
            except (ValueError, TypeError):
                pub_year = 0

            # Safe string handling
            title = str(row.get('book', '')) if pd.notna(row.get('book')) else ''
            author = str(row.get('author', '')) if pd.notna(row.get('author')) else ''
            language = str(row.get('language', '')) if pd.notna(row.get('language')) else ''
            publisher = str(row.get('book publisher', '')) if pd.notna(row.get('book publisher')) else ''
            isbn = str(row.get('ISBN', '')) if pd.notna(row.get('ISBN')) else ''
            bnb_id = str(row.get('BNB id', '')) if pd.notna(row.get('BNB id')) else ''

            book = Book(
                title=title,
                author=author,
                pub_year=pub_year,
                language=language,
                publisher=publisher,
                isbn=isbn,
                bnb_id=bnb_id
            )
            books.append(book)

        return books