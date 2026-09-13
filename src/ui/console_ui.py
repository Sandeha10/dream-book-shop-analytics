# src/ui/console_ui.py
import sys
from src.controllers.analysis_controller import AnalysisController
from src.strategies.publication_trends import PublicationTrendsStrategy
from src.strategies.top_authors import TopAuthorsStrategy
from src.strategies.language_distribution import LanguageDistributionStrategy
from src.strategies.publisher_distribution import PublisherDistributionStrategy
from src.strategies.missing_isbn import MissingIsbnStrategy
from src.strategies.language_by_year import LanguageByYearStrategy

class ConsoleUI:
    def __init__(self, data_path: str):
        print("\n[INFO] Loading Dream Book Shop dataset...")
        self.controller = AnalysisController(data_path)
        print(f"[SUCCESS] Loaded {self.controller.get_total_records()} records successfully.\n")

    def display_menu(self):
        while True:
            print("=" * 60)
            print("        DREAM BOOK SHOP - DATA ANALYSIS APPLICATION        ")
            print("=" * 60)
            print("1. Publication Trends Over Time")
            print("2. Top 5 Most Prolific Authors")
            print("3. Language Distribution of Books")
            print("4. Books Published by Publisher")
            print("5. Missing ISBN Analysis")
            print("6. Books Published per Year Categorized by Language")
            print("0. Exit Application")
            print("=" * 60)

            choice = input("Enter your selection (0-6): ").strip()

            strategy_map = {
                "1": PublicationTrendsStrategy(),
                "2": TopAuthorsStrategy(),
                "3": LanguageDistributionStrategy(),
                "4": PublisherDistributionStrategy(),
                "5": MissingIsbnStrategy(),
                "6": LanguageByYearStrategy()
            }

            if choice == "0":
                print("\nExiting application. Goodbye!")
                sys.exit(0)
            elif choice in strategy_map:
                selected_strategy = strategy_map[choice]
                print(f"\n>>> Executing: {selected_strategy.get_analysis_name()}...")
                result = self.controller.run_strategy(selected_strategy)
                self._print_text_summary(result)
            else:
                print("\n[!] Invalid choice, please enter an option between 0 and 6.")

    def _print_text_summary(self, result: dict):
        print("\n" + "-" * 50)
        print(f" TEXTUAL SUMMARY: {result.get('title')}")
        print("-" * 50)
        if "labels" in result and "values" in result:
            for lbl, val in zip(result["labels"], result["values"]):
                print(f" • {lbl:<30}: {val}")
        if "missing_pct" in result:
            print(f" • Total Records Analyzed   : {result['total']}")
            print(f" • Missing ISBN Count       : {result['missing_count']}")
            print(f" • Missing Percentage       : {result['missing_pct']}%")
        print(f"\n[INFO] Chart saved to: {result.get('saved_chart')}")
        input("\nPress Enter to return to main menu...")