from datetime import datetime
import os
import pandas as pd
import re


class ExpenseTracker:
    def __init__(self):
        self.__FILEPATH = 'Expense.csv'

        self.__CATEGORIES = {
            1: 'Utilities',
            2: 'Groceries',
            3: 'Transport',
            4: 'Health',
            5: 'Travel',
            6: 'Savings',
            7: 'Education'
        }

    def csv_read(self) -> pd.DataFrame:
        # Check if file exists
        if not os.path.isfile(self.__FILEPATH):
            # Return empty DataFrame with correct columns if file doesn't exist
            return pd.DataFrame(columns=['Datetime', 'Category', 'Amount'])
        
        # Read CSV and sort by date descending
        df = pd.read_csv(self.__FILEPATH)
        if not df.empty:
            df['Datetime'] = pd.to_datetime(df['Datetime'])
            df = df.sort_values('Datetime', ascending=False)
        return df

    def csv_write(self, Amount: float, Category: str, Date: datetime.date) -> None:
        file_exists = os.path.isfile(self.__FILEPATH)

        # Format amount to 2 decimal places
        formatted_amount = round(Amount, 2)

        dbw = pd.DataFrame({
            'Datetime': [Date], 
            'Category': [Category], 
            'Amount': [formatted_amount]
        })

        if not file_exists:
            dbw.to_csv(self.__FILEPATH, index=False)
        else:
            dbw.to_csv(self.__FILEPATH, mode='a', index=False, header=False)

    def add_expense(self):
        amount: int = self.ask_amount()
        category: str = self.ask_category()
        date: datetime.date = self.date_handler()
        self.csv_write(
            Amount=amount,
            Category=category,
            Date=date
        )

    def ask_amount(self) -> float:
        while True:
            try:
                amount: str = input('Enter Expense Amount: ').strip()
                
                # Validate amount format using regex (allows decimals)
                if not re.match(r'^\d+(\.\d{0,2})?$', amount):
                    raise ValueError('Invalid amount format. Use numbers with up to 2 decimal places (e.g., 10.99)')
                
                amount_float = float(amount)
                if amount_float <= 0:
                    raise ValueError('Amount must be greater than zero')
                
                return amount_float

            except ValueError as e:
                print(e)

    def ask_category(self) -> str:
        for key, category in self.__CATEGORIES.items():
            print(f'{key}: {category}')
        print()
        while True:
            try:
                category: int = int(input('Enter Expense Category: '))
                if category not in self.__CATEGORIES.keys():
                    raise ValueError('Invalid Category try again')
                return self.__CATEGORIES[category]
            except ValueError as e:
                print(e)

    def date_handler(self) -> datetime.date:
        while True:
            try:
                now_date: datetime.date = datetime.now().date()
                if now_date is None:
                    raise AttributeError('No datetime returned')
                return now_date
            except AttributeError as e:
                print(e)

    def view_expense(self):
        try:
            db: pd.DataFrame = self.csv_read()
            if db.empty:
                print("No expenses recorded yet.")
                return
            
            # Format the display
            display_df = db.copy()
            display_df['Amount'] = display_df['Amount'].apply(lambda x: f"${x:.2f}")
            display_df['Datetime'] = pd.to_datetime(display_df['Datetime']).dt.strftime('%Y-%m-%d')
            
            print("\nExpense List (Sorted by Date)")
            print("=" * 60)
            print(display_df.to_string(index=True))
            print("\nTotal Expenses: ${:.2f}".format(db['Amount'].sum()))
            
        except Exception as e:
            print(f"Error viewing expenses: {e}")

    def delete_expense(self):
        db: pd.DataFrame = self.csv_read()
        if db.empty:
            print("No expenses to delete.")
            return
        num_rows: int = db.shape[0]
        self.view_expense()
        print()
        while True:
            try:
                deleted_row: int = int(
                    input('Enter Data row you want to delete: '))
                if deleted_row not in range(0, num_rows):
                    raise ValueError('Row out of range, try again')
                verify: str = input('Are you sure (y/n):').strip().lower()
                if verify != 'y':
                    print('You cancelled the deletion')
                    return
                db = db.drop(db.index[deleted_row])
                db.to_csv(self.__FILEPATH, index=False)
                print('Row deleted successfully!')
                break

            except ValueError as e:
                print(e)

    def expense_summary(self):
        try:
            db: pd.DataFrame = self.csv_read()
            if db.empty:
                print("No expenses recorded yet.")
                return

            # Summary based on categories
            category_summary = db.groupby('Category')['Amount'].sum().sort_values(ascending=False)

            # Summary of total amount spent
            total_amount = db['Amount'].sum()

            print('\nCategory Summary')
            print('=' * 50)
            for category, amount in category_summary.items():
                print(f"{category:<20} ${amount:>10.2f}")
            
            print('\nTotal Amount')
            print('=' * 50)
            print(f'Total Expenses: ${total_amount:.2f}')
            
            # Add date range information
            if not db.empty:
                start_date = db['Datetime'].min().strftime('%Y-%m-%d')
                end_date = db['Datetime'].max().strftime('%Y-%m-%d')
                print(f"\nDate Range: {start_date} to {end_date}")
                
        except Exception as e:
            print(f"Error generating summary: {e}")


def main():
    tracker = ExpenseTracker()

    while True:
        menu_dict: dict = {
            1: 'Add Expense',
            2: 'View Expenses',
            3: 'View Expense Summary',
            4: 'Delete an Expense',
            5: 'Exit'
        }
        print("\nExpense Tracker Menu")
        print("===================")
        for num, menu_item in menu_dict.items():
            print(f'{num} {menu_item}')

        print()
        try:
            choice = input(f"\nEnter your choice (1-{len(menu_dict)}): ")
            if not (choice.isdigit() or (0 < int(choice) < (len(menu_dict)+1))):
                raise ValueError(
                    f'Wrong Choice, Enter btn 1 and {len(menu_dict)}')

            if choice == '1':
                tracker.add_expense()
            elif choice == '2':
                tracker.view_expense()
            elif choice == '3':
                tracker.expense_summary()
            elif choice == '4':
                tracker.delete_expense()
            elif choice == '5':
                print("Thank you for using Expense Tracker!")
                break
            else:
                print(
                    f"Invalid choice. Please enter a number between 1 and {len(menu_dict)}.")

        except ValueError as e:
            print(e)


if __name__ == "__main__":
    main()
