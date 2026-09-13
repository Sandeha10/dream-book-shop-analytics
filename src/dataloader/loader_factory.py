# src/dataloader/loader_factory.py
from src.dataloader.base_loader import IDataLoader
from src.dataloader.csv_loader import CsvDataLoader

class DataLoaderFactory:
    """
    Factory class responsible for instantiating concrete data loaders.
    Implements the Creational Factory Method Pattern.
    """
    @staticmethod
    def get_loader(file_type: str = "csv") -> IDataLoader:
        normalized_type = file_type.lower().strip()
        if normalized_type == "csv":
            return CsvDataLoader()
        else:
            raise ValueError(f"Unsupported loader type: '{file_type}'. Only 'csv' is currently supported.")