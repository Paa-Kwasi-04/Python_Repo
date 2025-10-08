"""
expense_tracker_gui.py
A GUI interface for the ExpenseTracker class using Tkinter.

Usage:
    Simply run this file: python expense_tracker_gui.py
"""

from datetime import datetime
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import font as tkfont
import pandas as pd  # Importing pandas for date formatting

# Import the ExpenseTracker from your main file
# Make sure the file with ExpenseTracker class is named accordingly
try:
    from main import ExpenseTracker
except ImportError:
    print("Error: Could not import ExpenseTracker.")
    print("Make sure your ExpenseTracker class is in 'main.py'")
    exit(1)


class ExpenseTrackerGUI:
    def __init__(self, root, tracker):
        """
        Initialize the GUI with a root window and an ExpenseTracker instance.
        
        Args:
            root: Tkinter root window
            tracker: ExpenseTracker instance
        """
        self.root = root
        self.tracker = tracker

        self.root.title("Expense Tracker")
        self.root.geometry("900x600")
        self.root.configure(bg='#f0f0f0')

        # Custom fonts
        self.title_font = tkfont.Font(
            family="Helvetica", size=16, weight="bold")
        self.label_font = tkfont.Font(family="Helvetica", size=10)

        # Color scheme
        self.primary_color = '#2c3e50'
        self.secondary_color = '#3498db'
        self.success_color = '#27ae60'
        self.danger_color = '#e74c3c'
        self.bg_color = '#ecf0f1'

        self.create_widgets()
        self.refresh_expenses()

    def create_widgets(self):
        # Title
        title_frame = tk.Frame(self.root, bg=self.primary_color, height=60)
        title_frame.pack(fill=tk.X)
        title_label = tk.Label(title_frame, text="💰 Expense Tracker",
                               font=self.title_font, bg=self.primary_color,
                               fg='white', pady=15)
        title_label.pack()

        # Main container
        main_container = tk.Frame(self.root, bg='#f0f0f0')
        main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Left panel - Add Expense
        left_panel = tk.LabelFrame(main_container, text="Add New Expense",
                                   font=self.label_font, bg='white',
                                   fg=self.primary_color, padx=15, pady=15)
        left_panel.grid(row=0, column=0, sticky='nsew', padx=(0, 10))

        # Amount
        tk.Label(left_panel, text="Amount:", font=self.label_font,
                 bg='white').grid(row=0, column=0, sticky='w', pady=5)
        self.amount_entry = tk.Entry(
            left_panel, font=self.label_font, width=20)
        self.amount_entry.grid(row=0, column=1, pady=5, padx=5)

        # Category
        tk.Label(left_panel, text="Category:", font=self.label_font,
                 bg='white').grid(row=1, column=0, sticky='w', pady=5)
        self.category_var = tk.StringVar()

        # Get categories from tracker
        categories = self._get_categories_from_tracker()

        self.category_combo = ttk.Combobox(left_panel, textvariable=self.category_var,
                                           values=categories,
                                           font=self.label_font, width=18, state='readonly')
        self.category_combo.grid(row=1, column=1, pady=5, padx=5)
        if categories:
            self.category_combo.current(0)

        # Date (auto-filled with current date)
        tk.Label(left_panel, text="Date:", font=self.label_font,
                 bg='white').grid(row=2, column=0, sticky='w', pady=5)
        self.date_label = tk.Label(left_panel, text=datetime.now().date().strftime('%Y-%m-%d'),
                                   font=self.label_font, bg='white', fg=self.secondary_color)
        self.date_label.grid(row=2, column=1, sticky='w', pady=5, padx=5)

        # Add button
        add_btn = tk.Button(left_panel, text="Add Expense",
                            command=self.add_expense,
                            bg=self.success_color, fg='white',
                            font=self.label_font, cursor='hand2',
                            relief=tk.FLAT, padx=20, pady=8)
        add_btn.grid(row=3, column=0, columnspan=2, pady=15)

        # Summary section
        summary_frame = tk.LabelFrame(left_panel, text="Summary",
                                      font=self.label_font, bg='white',
                                      fg=self.primary_color, padx=10, pady=10)
        summary_frame.grid(row=4, column=0, columnspan=2, sticky='ew', pady=10)

        self.total_label = tk.Label(summary_frame, text="Total Expenses: $0",
                                    font=self.label_font, bg='white',
                                    fg=self.danger_color)
        self.total_label.pack()

        view_summary_btn = tk.Button(summary_frame, text="View Detailed Summary",
                                     command=self.show_summary,
                                     bg=self.secondary_color, fg='white',
                                     font=self.label_font, cursor='hand2',
                                     relief=tk.FLAT, padx=10, pady=5)
        view_summary_btn.pack(pady=5)

        # Right panel - Expense List
        right_panel = tk.LabelFrame(main_container, text="Expense List",
                                    font=self.label_font, bg='white',
                                    fg=self.primary_color, padx=10, pady=10)
        right_panel.grid(row=0, column=1, sticky='nsew')

        # Treeview
        tree_frame = tk.Frame(right_panel, bg='white')
        tree_frame.pack(fill=tk.BOTH, expand=True)

        # Scrollbars
        tree_scroll_y = ttk.Scrollbar(tree_frame)
        tree_scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

        tree_scroll_x = ttk.Scrollbar(tree_frame, orient=tk.HORIZONTAL)
        tree_scroll_x.pack(side=tk.BOTTOM, fill=tk.X)

        self.expense_tree = ttk.Treeview(tree_frame,
                                         columns=('Index', 'Date',
                                                  'Category', 'Amount'),
                                         show='headings',
                                         yscrollcommand=tree_scroll_y.set,
                                         xscrollcommand=tree_scroll_x.set)

        tree_scroll_y.config(command=self.expense_tree.yview)
        tree_scroll_x.config(command=self.expense_tree.xview)

        # Column headings
        self.expense_tree.heading('Index', text='#')
        self.expense_tree.heading('Date', text='Date')
        self.expense_tree.heading('Category', text='Category')
        self.expense_tree.heading('Amount', text='Amount')

        # Column widths
        self.expense_tree.column('Index', width=40, anchor='center')
        self.expense_tree.column('Date', width=100, anchor='center')
        self.expense_tree.column('Category', width=100, anchor='center')
        self.expense_tree.column('Amount', width=80, anchor='center')

        self.expense_tree.pack(fill=tk.BOTH, expand=True)

        # Buttons for actions
        button_frame = tk.Frame(right_panel, bg='white')
        button_frame.pack(fill=tk.X, pady=10)

        refresh_btn = tk.Button(button_frame, text="🔄 Refresh",
                                command=self.refresh_expenses,
                                bg=self.secondary_color, fg='white',
                                font=self.label_font, cursor='hand2',
                                relief=tk.FLAT, padx=15, pady=5)
        refresh_btn.pack(side=tk.LEFT, padx=5)

        delete_btn = tk.Button(button_frame, text="🗑️ Delete Selected",
                               command=self.delete_expense,
                               bg=self.danger_color, fg='white',
                               font=self.label_font, cursor='hand2',
                               relief=tk.FLAT, padx=15, pady=5)
        delete_btn.pack(side=tk.LEFT, padx=5)

        # Configure grid weights
        main_container.grid_columnconfigure(0, weight=1)
        main_container.grid_columnconfigure(1, weight=2)
        main_container.grid_rowconfigure(0, weight=1)

    def _get_categories_from_tracker(self):
        """Extract categories from the tracker instance."""
        try:
            # Try to access the private __CATEGORIES attribute
            categories_dict = self.tracker._ExpenseTracker__CATEGORIES
            return list(categories_dict.values())
        except AttributeError:
            # Fallback to default categories if attribute doesn't exist
            return ['Utilities', 'Groceries', 'Transport', 'Health',
                    'Travel', 'Savings', 'Education']

    def add_expense(self):
        amount_str = self.amount_entry.get().strip()
        category = self.category_var.get()

        if not amount_str:
            messagebox.showerror("Error", "Please enter an amount!")
            return

        try:
            # Convert and validate amount
            amount = float(amount_str)
            if amount <= 0:
                messagebox.showerror("Error", "Amount must be greater than zero!")
                return

            date = datetime.now().date()
            self.tracker.csv_write(Amount=amount, Category=category, Date=date)
            messagebox.showinfo("Success", "Expense added successfully!")
            self.amount_entry.delete(0, tk.END)
            self.refresh_expenses()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add expense: {str(e)}")

    def refresh_expenses(self):
        # Clear existing items
        for item in self.expense_tree.get_children():
            self.expense_tree.delete(item)

        # Load expenses
        df = self.tracker.csv_read()

        if not df.empty:
            # Format display
            for idx, row in df.iterrows():
                date = pd.to_datetime(row['Datetime']).strftime('%Y-%m-%d')
                amount = f"${row['Amount']:.2f}"
                self.expense_tree.insert('', tk.END,
                                     values=(idx, date,
                                            row['Category'], amount))

            # Update total with proper formatting
            total = df['Amount'].sum()
            self.total_label.config(text=f"Total Expenses: ${total:.2f}")
        else:
            self.total_label.config(text="Total Expenses: $0.00")

    def delete_expense(self):
        selected_item = self.expense_tree.selection()

        if not selected_item:
            messagebox.showwarning("Warning", "Please select an expense to delete!")
            return

        item_values = self.expense_tree.item(selected_item[0])['values']
        if not item_values:
            return

        row_index = item_values[0]  # Get the index from the tree

        confirm = messagebox.askyesno("Confirm Delete",
                                      f"Are you sure you want to delete this expense?\n\n"
                                      f"Date: {item_values[1]}\n"
                                      f"Category: {item_values[2]}\n"
                                      f"Amount: {item_values[3]}")

        if confirm:
            try:
                df = self.tracker.csv_read()
                if not df.empty and 0 <= row_index < len(df):
                    df = df.drop(index=row_index)
                    df.to_csv(self.tracker._ExpenseTracker__FILEPATH, index=False)
                    messagebox.showinfo("Success", "Expense deleted successfully!")
                    self.refresh_expenses()
                else:
                    messagebox.showerror("Error", "Invalid row index!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to delete expense: {str(e)}")

    def show_summary(self):
        summary_window = tk.Toplevel(self.root)
        summary_window.title("Expense Summary")
        summary_window.geometry("450x500")
        summary_window.configure(bg='white')

        # Title
        title = tk.Label(summary_window, text="Expense Summary by Category",
                         font=self.title_font, bg=self.primary_color,
                         fg='white', pady=15)
        title.pack(fill=tk.X)

        # Content scroll frame
        canvas = tk.Canvas(summary_window, bg='white')
        scrollbar = ttk.Scrollbar(summary_window, orient="vertical", command=canvas.yview)
        content_frame = tk.Frame(canvas, bg='white')

        canvas.configure(yscrollcommand=scrollbar.set)

        # Pack the scrollbar and canvas
        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True, padx=20)

        # Create a window inside the canvas
        canvas.create_window((0, 0), window=content_frame, anchor="nw")

        df = self.tracker.csv_read()

        if df.empty:
            tk.Label(content_frame, text="No expenses recorded yet.",
                     font=self.label_font, bg='white').pack(pady=20)
        else:
            # Date range
            start_date = pd.to_datetime(df['Datetime']).min().strftime('%Y-%m-%d')
            end_date = pd.to_datetime(df['Datetime']).max().strftime('%Y-%m-%d')
            date_range = tk.Label(content_frame,
                            text=f"Date Range: {start_date} to {end_date}",
                            font=self.label_font, bg='white')
            date_range.pack(pady=(20, 10))

            # Category summary with proper formatting
            category_summary = df.groupby('Category')['Amount'].sum().sort_values(ascending=False)
            
            # Create a frame for summary items
            summary_items_frame = tk.Frame(content_frame, bg='white')
            summary_items_frame.pack(fill=tk.X, expand=True)
            
            for category, amount in category_summary.items():
                item_frame = tk.Frame(summary_items_frame, bg='#ecf0f1',
                                   relief=tk.RAISED, borderwidth=1)
                item_frame.pack(fill=tk.X, pady=2)

                tk.Label(item_frame, text=category, font=self.label_font,
                        bg='#ecf0f1', anchor='w').pack(side=tk.LEFT, padx=10, pady=8)
                tk.Label(item_frame, text=f"${amount:.2f}", font=self.label_font,
                        bg='#ecf0f1', fg=self.danger_color,
                        anchor='e').pack(side=tk.RIGHT, padx=10, pady=8)

            # Total with proper formatting
            total = df['Amount'].sum()
            total_frame = tk.Frame(content_frame, bg=self.primary_color)
            total_frame.pack(fill=tk.X, pady=(20, 0))

            tk.Label(total_frame, text="TOTAL", font=self.title_font,
                    bg=self.primary_color, fg='white',
                    anchor='w').pack(side=tk.LEFT, padx=10, pady=10)
            tk.Label(total_frame, text=f"${total:.2f}", font=self.title_font,
                    bg=self.primary_color, fg='#2ecc71',
                    anchor='e').pack(side=tk.RIGHT, padx=10, pady=10)

        # Configure the scroll region after adding all widgets
        content_frame.update_idletasks()
        canvas.configure(scrollregion=canvas.bbox("all"))

        # Make the window modal
        summary_window.transient(self.root)
        summary_window.grab_set()


def launch_gui(tracker):
    """
    Convenience function to launch the GUI with an ExpenseTracker instance.
    
    Args:
        tracker: ExpenseTracker instance
    """
    root = tk.Tk()
    app = ExpenseTrackerGUI(root, tracker)
    root.mainloop()


if __name__ == "__main__":
    # Create ExpenseTracker instance and launch GUI
    tracker = ExpenseTracker()
    root = tk.Tk()
    app = ExpenseTrackerGUI(root, tracker)
    root.mainloop()
