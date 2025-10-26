from expense_tracker.expense_tracker import Expenses_Tracker
from expense_tracker.model.expense import Expense
import argparse
from datetime import datetime


def main():
    expenses = Expenses_Tracker()

    parser = argparse.ArgumentParser()
    parser.add_argument("action", help="action to be performed")
    parser.add_argument("-d","--description", help="set description of the expense", type=str)
    parser.add_argument("-a","--amount", help="set amount of the expense", type=float)
    args = parser.parse_args()

    if args.action == "add" and args.description and args.amount:
        expenses.add_expense(Expense(description=args.description, amount=args.amount,  date=datetime.now()))
    elif args.action == "view":
        expenses.view_expenses()
    elif args.action == "edit" and args.description and args.amount:
        expenses.edit_expense(Expense(description=args.description, amount=args.amount,  date=""))
    elif args.action == "remove" and args.description:
        pass 
    else:
        print("invalid command")

if __name__ == "__main__":
    main()