from src.dataloader.loader_factory import DataLoaderFactory
from src.dataloader.data_store import AppDataStore
from src.strategies.base_strategy import IAnalysisStrategy
from src.visualizer.chart_visualizer import ChartVisualizer

class AnalysisController:
    def __init__(self, data_path: str):
        self.data_store = AppDataStore()
        
        if not self.data_store.is_loaded():
            loader = DataLoaderFactory.get_loader("csv")
            books = loader.load_data(data_path)
            self.data_store.set_books(books)

        self.visualizer = ChartVisualizer()

    def get_total_records(self) -> int:
        return len(self.data_store.get_books())

    def run_strategy(self, strategy: IAnalysisStrategy):
        books = self.data_store.get_books()
        result = strategy.execute(books)
        save_path = self.visualizer.render(result)
        result["saved_chart"] = save_path
        return result

