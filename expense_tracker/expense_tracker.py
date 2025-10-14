import os 
import json 
from .model.expense import Expense
FILENAME = "expense_tracker/data/expenses.json"    

class Expenses_Tracker(): 
    def __init__(self) -> None:
        os.makedirs(os.path.dirname(FILENAME), exist_ok=True)
        if not os.path.exists(FILENAME):
            with open(FILENAME, "w") as f:
                json.dump([], f)
        self._load_data()

    def _load_data(self) -> None:
        with open(FILENAME, 'r') as file:
            try:
                file_content = file.read()
                if file_content:
                    self.data = json.loads(file_content)
                    if not isinstance(self.data, list):
                        self.data = []
                else:
                    self.data = []
            except json.JSONDecodeError:
                self.data = []

    def _save_data(self) -> None:
        with open(FILENAME, 'w') as file:
            json.dump(self.data, file)

    def add_expense(self, expense: Expense) -> None:
        self.data.append({"description": expense.description, "amount": expense.amount, "date": expense.date.isoformat()})
        self._save_data()
        print(f"added expense: {expense.description} of amount {expense.amount} on date {expense.date}")