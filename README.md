# 📚 Dream Book Shop — Bibliographic Data Processing Engine

[![Python Version](https://img.shields.io/badge/Python-3.13%2B-blue.svg)](https://www.python.org/)
[![Testing Framework](https://img.shields.io/badge/Tested%20with-PyTest-yellow.svg)](https://pytest.org/)
[![Architecture](https://img.shields.io/badge/Architecture-Layered%20%2F%20Clean-green.svg)](#system-architecture)
[![Code Style](https://img.shields.io/badge/Code%20Style-PEP8%20%2F%20Clean%20Code-orange.svg)](#clean-code--solid-compliance)
[![License](https://img.shields.io/badge/License-Academic%20Use-lightgrey.svg)](#license)

An enterprise-grade, object-oriented data analytics and visualization command-line application engineered for **Dream Book Shop** to ingest, cleanse, audit, and analyze large-scale archival records from the **British National Bibliography (BNB)**.

This system was developed as part of **Pearson BTEC Higher National Diploma in Computing (Level 5) — Unit 20: Applied Programming and Design Principles**.

---

##  Table of Contents
- [Executive Overview](#executive-overview)
- [Key Features & Analytics](#key-features--analytics)
- [System Architecture](#system-architecture)
- [Design Patterns Applied](#design-patterns-applied)
- [Clean Code & SOLID Compliance](#clean-code--solid-compliance)
- [Directory Structure](#directory-structure)
- [Running the Application](#running-the-application)



---

##  Executive Overview

Dream Book Shop acquired an archival corpus of **3,876 British comic book publication records** from the British National Bibliography. Historically constrained by fragmented manual workflows, the organization required an automated engine capable of:
* Auditing catalogue data integrity (quantifying missing ISBN commercial tracking codes).
* Identifying market-dominating creators and publishing imprints.
* Analyzing multi-decade historical publishing trajectories.
* Generating publication-grade 300 DPI graphical charts automatically.

The solution avoids monolithic script architecture in favor of a decoupled, layered design that achieves sub-second processing speeds through $O(n)$ hash-map lookups and isolated algorithm strategies.

---

##  Key Features & Analytics

The application features an interactive Command-Line Interface (CLI) executing six core analytical queries:

1. **Publication Trends Over Time:** Chronological analysis from 1930 to 2024 with a marked multi-decade line chart.
2. **Top 5 Most Prolific Authors:** Descending ranking of creators (led by René Goscinny and Hergé) visualized via horizontal bar charts.
3. **Language Distribution Profile:** Categorization across English (96.54%), French, Welsh, and German editions illustrated via a proportional pie chart.
4. **Publisher Volume Breakdown:** Market-share distribution identifying industry leaders (Titan Books, DC, Marvel) with vertical column graphs.
5. **Missing ISBN Integrity Audit:** Comprehensive audit detecting that 40 records (1.03%) lack ISBNs, rendered as a high-contrast donut chart.
6. **Decennial Cross-Matrix (Language by Year):** Multi-dimensional matrix cross-tabulating language evolution across historical decades.

---

##  System Architecture

The codebase adheres strictly to a **Separation of Concerns (SoC)** layered pattern:

[Presentation Layer: ConsoleUI]
│
▼
[Application Orchestration Layer: AnalysisController]
│──────────────────────────────────────┐
▼                                      ▼
[Business Logic: IAnalysisStrategy]   [Visualization Subsystem: ChartVisualizer Facade]
(6 Concrete Interchangeable Classes)         │
│                                      ▼
▼                                 [reports/*.png (300 DPI)]
[Data Access: DataLoaderFactory & CsvDataLoader]
│
▼
[In-Memory Cache: AppDataStore Singleton] ──▶ [Domain Entity: Book Model]




##  Design Patterns Applied

| Pattern Category | Design Pattern | Implementation Target | Architectural Benefit |
| :--- | :--- | :--- | :--- |
| **Creational** | **Factory Method** | `DataLoaderFactory` | Decouples controller from concrete CSV loaders; enables future JSON/SQL extension. |
| **Creational** | **Singleton** | `AppDataStore` | Enforces a single in-memory store for 3,876 books; eliminates duplicate disk I/O. |
| **Behavioural** | **Strategy** | `IAnalysisStrategy` | Encapsulates the 6 queries in swappable classes; eliminates complex `if/elif` blocks. |
| **Structural** | **Facade** | `ChartVisualizer` | Hides low-level Matplotlib canvas setup behind a single clean `.render()` call. |

---

##  Clean Code & SOLID Compliance

* **Single Responsibility Principle (SRP):** Classes have one reason to change (`CsvDataLoader` parses files, `ChartVisualizer` renders plots).
* **Open/Closed Principle (OCP):** New reporting routines are introduced by implementing `IAnalysisStrategy` without editing existing controllers.
* **Liskov Substitution Principle (LSP):** All strategies are interchangeable via identical `execute(books)` polymorphic contracts.
* **Interface Segregation Principle (ISP):** Small, focused interfaces (`IDataLoader` defines 1 method; `IAnalysisStrategy` defines 2).
* **Dependency Inversion Principle (DIP):** High-level orchestrators depend on abstract interfaces rather than concrete parsers.
* **$O(n)$ Hash Performance:** Implements Python's native `collections.Counter` for linear frequency counting, completing all analyses in **< 0.8s**.

---

##  Directory Structure

dream_book_analytics/
│
├── data/
│   └── Dataset Books.csv           # Archival BNB dataset (3,876 items)
│
├── reports/                        # Auto-generated visualization target directory
│   ├── publication_trends.png
│   ├── top_authors.png
│   ├── language_distribution.png
│   ├── publisher_distribution.png
│   ├── missing_isbn_analysis.png
│   └── language_by_year.png
│
├── src/
│   ├── models/
│   │   └── book.py                 # Encapsulated Book entity model
│   ├── dataloader/
│   │   ├── base.py                 # IDataLoader abstract contract
│   │   ├── csv_loader.py           # Concrete CSV parser with data cleaning
│   │   └── factory.py              # DataLoaderFactory creational engine
│   ├── datastore/
│   │   └── store.py                # Thread-safe AppDataStore Singleton
│   ├── strategies/
│   │   ├── base.py                 # IAnalysisStrategy behavioural interface
│   │   ├── trends.py               # Publication trends algorithm
│   │   ├── authors.py              # Top prolific authors algorithm
│   │   ├── languages.py            # Language distribution algorithm
│   │   ├── publishers.py           # Publisher distribution algorithm
│   │   ├── missing_isbn.py         # Missing ISBN metric algorithm
│   │   └── language_by_year.py     # Cross-dimensional matrix algorithm
│   ├── visualizer/
│   │   └── chart_visualizer.py     # Matplotlib Facade wrapper
│   ├── controllers/
│   │   └── analysis_controller.py  # Central workflow orchestrator
│   └── ui/
│       └── console_ui.py           # Interactive CLI menu & terminal formatter
│
├── tests/
│   ├── conftest.py                 # In-memory mock fixtures (sample_books)
│   ├── test_loader.py              # Positive/Negative tests (Factory, Loader, Model, Store)
│   └── test_strategies.py          # Arithmetic & edge-case tests (All 6 strategies)
│
├── main.py                         # Application composition root & bootstrap
├── requirements.txt                # Pinned production and testing dependencies
└── README.md                       # Comprehensive system documentation



## Running the Application
Ensure your virtual environment is active, then launch the interactive CLI:

Bash
python main.py
Interactive Menu Navigation

============================================================
       DREAM BOOK SHOP - BIBLIOGRAPHIC ANALYTICS ENGINE
============================================================
[1] Publication Trends Over Time (Annual Counts)
[2] Top 5 Most Prolific Authors (Creator Rankings)
[3] Language Distribution Profile
[4] Publisher Volume Distribution (Top Imprints)
[5] Missing ISBN Integrity Audit (Count & Percentage)
[6] Books Published per Year Categorized by Language
[0] Exit Application
============================================================
Select an option (0-6): 5
Note: Selecting an analysis displays a formatted textual summary in the terminal, renders an interactive Matplotlib chart window, and automatically exports a 300 DPI graphic to the reports/ folder.

 
## Automated Testing Suite
The system includes 14 automated unit tests built on PyTest, running against isolated in-memory fixtures (sample_books) without external disk dependencies.

To execute the test suite with detailed output:

Bash
pytest -v
Verified Test Run Output:

============================= test session starts =============================
platform win32 -- Python 3.13.6, pytest-9.1.1, pluggy-1.6.0
rootdir: D:\dream_book_analytics
collected 14 items

tests/test_loader.py::test_factory_returns_csv_loader PASSED             [  7%]
tests/test_loader.py::test_factory_invalid_type_raises_value_error PASSED [ 14%]
tests/test_loader.py::test_loader_non_existent_file_raises_exception PASSED [ 21%]
tests/test_loader.py::test_book_model_encapsulation_and_isbn PASSED      [ 28%]
tests/test_loader.py::test_singleton_app_data_store PASSED              [ 35%]
tests/test_loader.py::test_singleton_app_data_store_identity PASSED     [ 42%]
tests/test_strategies.py::test_missing_isbn_strategy_calculation PASSED  [ 50%]
tests/test_strategies.py::test_top_authors_strategy PASSED              [ 57%]
tests/test_strategies.py::test_publication_trends_strategy PASSED        [ 64%]
tests/test_strategies.py::test_language_distribution_strategy PASSED    [ 71%]
tests/test_strategies.py::test_strategy_with_empty_dataset PASSED       [ 78%]
tests/test_strategies.py::test_strategy_with_invalid_year PASSED        [ 85%]
tests/test_strategies.py::test_publisher_distribution_strategy PASSED   [ 92%]
tests/test_strategies.py::test_language_by_year_strategy PASSED         [100%]

============================= 14 passed  ==============================


