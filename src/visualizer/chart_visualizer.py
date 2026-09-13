# src/visualizer/chart_visualizer.py
import os
import matplotlib.pyplot as plt
from typing import Dict, Any

class ChartVisualizer:
    """Generates graphical charts and saves them to the reports directory."""

    def __init__(self, output_dir: str = "reports"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def render(self, data: Dict[str, Any]) -> str:
        chart_type = data.get("type")
        title = data.get("title", "Report")
        save_path = os.path.join(self.output_dir, f"{title.replace(' ', '_').lower()}.png")

        plt.figure(figsize=(10, 5))
        plt.title(title, fontsize=14, fontweight='bold')

        if chart_type == "line":
            plt.plot(data["labels"], data["values"], marker='o', color='#1f77b4', linewidth=2)
            plt.xlabel("Year")
            plt.ylabel("Count")
            plt.xticks(rotation=45)
            plt.grid(True, linestyle='--', alpha=0.6)

        elif chart_type == "bar":
            plt.bar(data["labels"], data["values"], color='#2ca02c')
            plt.xlabel("Category")
            plt.ylabel("Book Count")
            plt.xticks(rotation=30, ha='right')

        elif chart_type == "pie":
            plt.pie(data["values"], labels=data["labels"], autopct='%1.1f%%', startangle=140)

        elif chart_type == "donut":
            plt.pie(data["values"], labels=data["labels"], autopct='%1.1f%%', startangle=90, colors=['#4CAF50', '#FF5722'])
            centre_circle = plt.Circle((0, 0), 0.70, fc='white')
            fig = plt.gcf()
            fig.gca().add_artist(centre_circle)

        elif chart_type == "grouped_bar":
            years = data["years"][-6:]  
            languages = data["languages"]
            for lang in languages:
                vals = [data["matrix"][int(y)][lang] for y in years]
                plt.plot(years, vals, marker='s', label=lang)
            plt.legend()
            plt.xlabel("Recent Years")
            plt.ylabel("Publication Count")

        plt.tight_layout()
        plt.savefig(save_path)
        plt.show() 
        plt.close()

        return save_path




    