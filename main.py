# main.py
import os
from src.ui.console_ui import ConsoleUI

def main():
    # Path to your dataset
    csv_file = os.path.join("data", "Dataset Books.csv")

    if not os.path.exists(csv_file):
        print(f"[ERROR] Dataset file not found at '{csv_file}'. Please verify the path.")
        return

    app = ConsoleUI(data_path=csv_file)
    app.display_menu()

if __name__ == "__main__":
    main()