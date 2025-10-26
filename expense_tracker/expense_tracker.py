import os 
import json 
from expense_tracker.model.expense import Expense
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
        if expense.amount <= 0:
            self.data.append({"description": expense.description, "amount": expense.amount, "date": expense.date.isoformat()})
            self._save_data()
            print(f"added expense: {expense.description} of amount {expense.amount} on date {expense.date}")
        else: 
            print("amount must be positive")
    def view_expenses(self) -> None:
        for expense in self.data:
            print(f"expense: {expense['description']} of amount {expense['amount']} on date {expense['date']}")
    def edit_expense(self, expense: Expense) -> None:
        for e in self.data:
            if e['description'] == expense.description:
                e['amount'] = expense.amount
                self._save_data()
                print(f"edited expense: {expense.description}")
                return          
        print(f"expense with description {expense.description} not found")
    def remove_expense(self, description: str) -> None:
        for e in self.data:
            if e['description'] == description:
                self.data.remove(e)
                self._save_data()
                print(f"removed expense: {description}")
                return          
        print(f"expense with description {description} not found")