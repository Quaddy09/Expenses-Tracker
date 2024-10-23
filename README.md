# Expenses-Tracker

Here's an expanded description that meets the 350-word requirement:

---

# Personal Expense Tracker with Data Visualization

This project is a Python-based Personal Expense Tracker designed to help users manage and monitor their daily expenses effectively. With a focus on user-friendliness, this application allows individuals to log their expenses, categorize them, and analyze their spending patterns over time. The program features both a command-line interface (CLI) for straightforward interaction and an optional graphical user interface (GUI) built with `tkinter` for a more visual approach.

## Features:

- **Add Expenses**: Users can easily record expenses by entering the amount, selecting a category, and providing a brief description. Each entry is saved in a CSV file for easy access and management.
  
- **View Expenses**: All logged expenses can be retrieved and displayed, allowing users to see their spending habits at a glance.

- **Analyze Expenses**: The application calculates total expenses and provides insights into spending by category. Users can quickly identify where their money is going and make informed financial decisions.

- **Filter by Date**: Users can filter and view expenses within a specific date range, making it easier to track spending over different periods (e.g., monthly or weekly).

- **Data Visualization**: The program generates visual representations of spending data:
  - **Pie Charts**: Illustrate the distribution of expenses by category, providing a clear overview of spending habits.
  - **Line Charts**: Display cumulative spending trends over time, helping users understand their financial trajectory.

- **Graphical User Interface (Optional)**: The `tkinter`-based GUI enhances usability, allowing users to input expenses and view visualizations seamlessly.

## File Structure:

- **`main.py`**: The main script for the command-line interface (CLI).
- **`expense_tracker.py`**: Contains functions for managing expenses, including adding, viewing, and calculating totals.
- **`visualization.py`**: Contains functions for generating visualizations using `matplotlib`.
- **`gui.py`**: Implements the optional graphical user interface.

## Requirements:

- Python 3.x
- `matplotlib`
- `tkinter` (for GUI)

## How to Run:

1. Clone the repository.
2. Install the required packages:
   ```bash
   pip install matplotlib
   ```
3. To run the CLI:
   ```bash
   python main.py
   ```
4. To use the GUI (optional):
   ```bash
   python gui.py
   ```

This project aims to provide a comprehensive and user-friendly solution for personal finance management, empowering users to take control of their financial health.

---

Feel free to make any additional modifications!
