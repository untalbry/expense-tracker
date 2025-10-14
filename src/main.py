import os 
import json 
import argparse
FILENAME = "expensses.json"    

class Expenses_Tracker(): 
    def __init__(self) -> None:
        if not os.path.exists(FILENAME):
            with open(FILENAME, 'w') as file:
                json.dump([], file)
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

    def add_expense(self, description: str, amount: float) -> None:
        self.data.append({"description": description, "amount": amount})
        self._save_data()
        print(f"added expense: {description} of amount {amount}")

    def run(self) -> None:
        pass
        

def main():
    expenses = Expenses_Tracker()

    parser = argparse.ArgumentParser()
    parser.add_argument("action", help="action to be performed")
    parser.add_argument("-d","--description", help="set description of the expense", type=str)
    parser.add_argument("-a","--amount", help="set amount of the expense", type=float)
    args = parser.parse_args()

    if args.action == "add" and args.description and args.amount:
        expenses.add_expense(args.description, args.amount)
    elif args.action == "view":
        print("viewing expenses")
    elif args.action == "remove" and args.description:
        print(f"removed expense: {args.description}")
    else:
        print("invalid command")

if __name__ == "__main__":
    main()