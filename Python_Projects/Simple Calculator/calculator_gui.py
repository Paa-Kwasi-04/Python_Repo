"""
Tkinter GUI for Shunting Yard Calculator

This module provides a graphical user interface for the calculator using tkinter.
Integrates with the ShuntingYardAlgorithm and PostfixEval modules.
"""

import tkinter as tk
from tkinter import ttk, messagebox
import re
from ShuntingYardAlgorithm import ShuntingYardAlgo
from postfixEval import PostfixEval


class CalculatorGUI:
    """
    A GUI calculator application using tkinter.
    
    This class creates a graphical interface for converting infix expressions
    to postfix notation and evaluating them using the Shunting Yard Algorithm.
    """
    
    def __init__(self, root):
        """
        Initialize the calculator GUI.
        
        Parameters
        ----------
        root : tk.Tk
            The root tkinter window
        """
        self.root = root
        self.root.title("Shunting Yard Calculator")
        self.root.geometry("500x700")
        self.root.resizable(False, False)
        
        # Initialize calculator components
        self.shunting_yard = ShuntingYardAlgo()
        self.postfix_eval = PostfixEval()
        
        # History storage
        self.history = []
        
        # Configure style
        self.setup_styles()
        
        # Create GUI components
        self.create_widgets()
        
        # Bind keyboard events
        self.root.bind('<Return>', lambda e: self.calculate())
        self.root.bind('<Escape>', lambda e: self.clear())
        
    def setup_styles(self):
        """Configure the visual styles for the application."""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure colors
        self.bg_color = "#f0f0f0"
        self.button_color = "#4a90e2"
        self.button_hover = "#357abd"
        self.operator_color = "#e67e22"
        self.equal_color = "#27ae60"
        
        self.root.configure(bg=self.bg_color)
        
    def create_widgets(self):
        """Create all GUI widgets."""
        # Title
        title_frame = tk.Frame(self.root, bg="#4a90e2", height=60)
        title_frame.pack(fill=tk.X, pady=(0, 10))
        title_frame.pack_propagate(False)
        
        title_label = tk.Label(
            title_frame, 
            text="🧮 Shunting Yard Calculator",
            font=("Arial", 18, "bold"),
            bg="#4a90e2",
            fg="white"
        )
        title_label.pack(expand=True)
        
        subtitle = tk.Label(
            title_frame,
            text="Infix → Postfix → Result",
            font=("Arial", 10),
            bg="#4a90e2",
            fg="white"
        )
        subtitle.pack()
        
        # Main container
        main_frame = tk.Frame(self.root, bg=self.bg_color)
        main_frame.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)
        
        # Expression entry
        entry_frame = tk.Frame(main_frame, bg=self.bg_color)
        entry_frame.pack(fill=tk.X, pady=(0, 10))
        
        tk.Label(
            entry_frame,
            text="Enter Expression:",
            font=("Arial", 11, "bold"),
            bg=self.bg_color
        ).pack(anchor=tk.W)
        
        self.expression_var = tk.StringVar()
        self.expression_entry = tk.Entry(
            entry_frame,
            textvariable=self.expression_var,
            font=("Arial", 16),
            relief=tk.SOLID,
            borderwidth=2
        )
        self.expression_entry.pack(fill=tk.X, ipady=8)
        
        # Button pad
        button_frame = tk.Frame(main_frame, bg=self.bg_color)
        button_frame.pack(pady=10)
        
        # Button layout
        buttons = [
            ['7', '8', '9', '/', '('],
            ['4', '5', '6', '*', ')'],
            ['1', '2', '3', '-', '^'],
            ['0', '.', 'C', '+', '=']
        ]
        
        for row_idx, row in enumerate(buttons):
            for col_idx, btn_text in enumerate(row):
                btn = tk.Button(
                    button_frame,
                    text=btn_text,
                    font=("Arial", 14, "bold"),
                    width=5,
                    height=2,
                    relief=tk.RAISED,
                    borderwidth=2
                )
                
                # Set button colors and commands
                if btn_text == '=':
                    btn.configure(bg="#27ae60", fg="white", command=self.calculate)
                elif btn_text == 'C':
                    btn.configure(bg="#e74c3c", fg="white", command=self.clear)
                elif btn_text in ['+', '-', '*', '/', '^', '(', ')']:
                    btn.configure(bg="#e67e22", fg="white", 
                                command=lambda t=btn_text: self.add_to_expression(t))
                else:
                    btn.configure(bg="#ecf0f1", 
                                command=lambda t=btn_text: self.add_to_expression(t))
                
                btn.grid(row=row_idx, column=col_idx, padx=3, pady=3)
        
        # Results frame
        results_frame = tk.Frame(main_frame, bg=self.bg_color)
        results_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Postfix result
        postfix_frame = tk.LabelFrame(
            results_frame,
            text="Postfix Notation",
            font=("Arial", 10, "bold"),
            bg="#e8f4f8",
            relief=tk.SOLID,
            borderwidth=2
        )
        postfix_frame.pack(fill=tk.X, pady=5)
        
        self.postfix_label = tk.Label(
            postfix_frame,
            text="",
            font=("Courier", 12),
            bg="#e8f4f8",
            fg="#2c3e50",
            anchor=tk.W,
            wraplength=450
        )
        self.postfix_label.pack(padx=10, pady=10, fill=tk.X)
        
        # Final result
        result_frame = tk.LabelFrame(
            results_frame,
            text="Result",
            font=("Arial", 10, "bold"),
            bg="#d5f4e6",
            relief=tk.SOLID,
            borderwidth=2
        )
        result_frame.pack(fill=tk.X, pady=5)
        
        self.result_label = tk.Label(
            result_frame,
            text="",
            font=("Arial", 20, "bold"),
            bg="#d5f4e6",
            fg="#27ae60"
        )
        self.result_label.pack(padx=10, pady=10)
        
        # History
        history_frame = tk.LabelFrame(
            results_frame,
            text="Recent Calculations",
            font=("Arial", 10, "bold"),
            bg="white",
            relief=tk.SOLID,
            borderwidth=2
        )
        history_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Scrollable history
        history_canvas = tk.Canvas(history_frame, bg="white", height=100)
        scrollbar = ttk.Scrollbar(history_frame, orient="vertical", command=history_canvas.yview)
        self.history_frame_inner = tk.Frame(history_canvas, bg="white")
        
        self.history_frame_inner.bind(
            "<Configure>",
            lambda e: history_canvas.configure(scrollregion=history_canvas.bbox("all"))
        )
        
        history_canvas.create_window((0, 0), window=self.history_frame_inner, anchor="nw")
        history_canvas.configure(yscrollcommand=scrollbar.set)
        
        history_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Instructions
        info_label = tk.Label(
            main_frame,
            text="Supports: + - * / ^ ( )  |  Press Enter to calculate, Esc to clear",
            font=("Arial", 8),
            bg=self.bg_color,
            fg="#7f8c8d"
        )
        info_label.pack(pady=5)
        
    def format_expression(self, expression):
        """
        Format mathematical expression to have proper spacing.
        
        Parameters
        ----------
        expression : str
            Raw input expression
            
        Returns
        -------
        str
            Formatted expression with spaces between tokens
        """
        expression = "".join(expression.split())
        tokens = re.findall(r'(?:\d*\.?\d+)|[()+\-*/^]', expression)
        return " ".join(tokens) if tokens else ""
    
    def add_to_expression(self, char):
        """Add a character to the expression entry."""
        current = self.expression_var.get()
        self.expression_var.set(current + str(char))
        
    def clear(self):
        """Clear all fields."""
        self.expression_var.set("")
        self.postfix_label.config(text="")
        self.result_label.config(text="")
        
    def calculate(self):
        """Calculate the result of the expression."""
        try:
            raw_expression = self.expression_var.get().strip()
            
            if not raw_expression:
                messagebox.showwarning("Empty Expression", "Please enter an expression")
                return
            
            # Format the expression
            formatted_expr = self.format_expression(raw_expression)
            
            # Convert to postfix
            postfix_expr = self.shunting_yard.shunting_yard(formatted_expr)
            
            # Evaluate
            result = self.postfix_eval.postfix_eval(postfix_expr)
            
            # Display results
            self.postfix_label.config(text=postfix_expr)
            self.result_label.config(text=str(result))
            
            # Add to history
            self.add_to_history(formatted_expr, postfix_expr, result)
            
        except ZeroDivisionError:
            messagebox.showerror("Error", "Division by zero")
        except Exception as e:
            messagebox.showerror("Error", f"Invalid expression: {str(e)}")
    
    def add_to_history(self, expression, postfix, result):
        """
        Add calculation to history.
        
        Parameters
        ----------
        expression : str
            The infix expression
        postfix : str
            The postfix notation
        result : int/float
            The calculated result
        """
        # Add to history list (keep last 5)
        self.history.insert(0, (expression, postfix, result))
        self.history = self.history[:5]
        
        # Clear existing history display
        for widget in self.history_frame_inner.winfo_children():
            widget.destroy()
        
        # Display history
        for idx, (expr, pf, res) in enumerate(self.history):
            history_item = tk.Frame(self.history_frame_inner, bg="#ecf0f1", relief=tk.RAISED, borderwidth=1)
            history_item.pack(fill=tk.X, padx=5, pady=2)
            
            # Make clickable
            history_item.bind("<Button-1>", lambda e, ex=expr: self.load_from_history(ex))
            
            expr_label = tk.Label(
                history_item,
                text=f"{expr} = {res}",
                font=("Courier", 9, "bold"),
                bg="#ecf0f1",
                anchor=tk.W
            )
            expr_label.pack(fill=tk.X, padx=5, pady=2)
            expr_label.bind("<Button-1>", lambda e, ex=expr: self.load_from_history(ex))
            
            postfix_label = tk.Label(
                history_item,
                text=f"Postfix: {pf}",
                font=("Courier", 8),
                bg="#ecf0f1",
                fg="#7f8c8d",
                anchor=tk.W
            )
            postfix_label.pack(fill=tk.X, padx=5, pady=(0, 2))
            postfix_label.bind("<Button-1>", lambda e, ex=expr: self.load_from_history(ex))
    
    def load_from_history(self, expression):
        """Load an expression from history."""
        self.expression_var.set(expression.replace(" ", ""))
        self.calculate()


def main():
    """Main entry point for the GUI application."""
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.mainloop()


if __name__ == '__main__':
    main()