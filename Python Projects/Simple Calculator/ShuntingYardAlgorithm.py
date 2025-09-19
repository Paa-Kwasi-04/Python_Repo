import tkinter as tk
import math


class Calculator:
    """
    A calculator that evaluates mathematical expressions, including functions,
    using the Shunting-Yard algorithm with stacks.
    """

    def __init__(self):
        # Define operator precedence. Higher number means higher precedence.
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '%': 2, '//': 2}
        # Define single-argument mathematical functions.
        self.functions = {
            'sin': math.sin, 'cos': math.cos, 'tan': math.tan,
            'sqrt': math.sqrt, 'log': math.log, 'floor': math.floor
        }

    def _get_precedence(self, op):
        """Helper method to get operator precedence."""
        return self.precedence.get(op, 0)

    def _apply_op(self, op, b, a):
        """Helper method to perform a binary operation."""
        if op == '+':
            return a + b
        if op == '-':
            return a - b
        if op == '*':
            return a * b
        if op == '/':
            if b == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            return a / b
        if op == '%':
            return a % b
        if op == '//':
            return a // b

    def _apply_func(self, func, a):
        """Helper method to apply a single-argument function."""
        if func in self.functions:
            return self.functions[func](a)
        else:
            raise ValueError(f"Unknown function: {func}")

    def evaluate(self, expression):
        """
        Evaluates a mathematical expression given as a string.
        """
        tokens = expression.replace(" ", "")
        values = []
        ops = []
        i = 0

        while i < len(tokens):
            token = tokens[i]

            if token.isdigit() or token == '.':
                num_str = ""
                while i < len(tokens) and (tokens[i].isdigit() or tokens[i] == '.'):
                    num_str += tokens[i]
                    i += 1
                values.append(float(num_str))
                i -= 1

            elif token == '(':
                ops.append(token)

            elif token == ')':
                while ops and ops[-1] != '(':
                    op = ops.pop()
                    if op in self.functions:
                        val = values.pop()
                        values.append(self._apply_func(op, val))
                    else:
                        val2 = values.pop()
                        val1 = values.pop()
                        values.append(self._apply_op(op, val2, val1))
                if ops:
                    ops.pop()

            elif token.isalpha():
                func_name = ""
                while i < len(tokens) and tokens[i].isalpha():
                    func_name += tokens[i]
                    i += 1
                ops.append(func_name)
                i -= 1

            else:
                while ops and self._get_precedence(ops[-1]) >= self._get_precedence(token) and ops[-1] != '(':
                    op = ops.pop()
                    val2 = values.pop()
                    val1 = values.pop()
                    values.append(self._apply_op(op, val2, val1))
                ops.append(token)

            i += 1

        while ops:
            op = ops.pop()
            if op in self.functions:
                val = values.pop()
                values.append(self._apply_func(op, val))
            else:
                val2 = values.pop()
                val1 = values.pop()
                values.append(self._apply_op(op, val2, val1))

        return values[0] if values else None


class CalculatorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Advanced Calculator")
        master.geometry("300x400")
        master.configure(bg="#333333")

        self.calculator = Calculator()
        self.expression = ""

        self.display = tk.Entry(master, width=20, font=(
            "Arial", 20), bd=5, relief=tk.RIDGE, justify="right", bg="#555555", fg="white")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        buttons = [
            'sin(', 'cos(', 'tan(', '(',
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '%', '+',
            'sqrt(', 'floor(', '//', ')'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(master, text=button, padx=15, pady=15, font=("Arial", 14), bg="#777777", fg="white",
                      command=lambda btn=button: self.click_button(btn)).grid(row=row_val, column=col_val, padx=5, pady=5)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        tk.Button(master, text="C", padx=15, pady=15, font=("Arial", 14), bg="#ff7f50", fg="white",
                  command=self.clear_expression).grid(row=row_val, column=0, columnspan=2, padx=5, pady=5, sticky="ew")
        tk.Button(master, text="=", padx=15, pady=15, font=("Arial", 14), bg="#4CAF50", fg="white",
                  command=self.calculate).grid(row=row_val, column=2, columnspan=2, padx=5, pady=5, sticky="ew")

    def click_button(self, button_text):
        if button_text in ('sin(', 'cos(', 'tan(', 'sqrt(', 'floor('):
            self.expression += button_text
        else:
            self.expression += button_text
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)

    def clear_expression(self):
        self.expression = ""
        self.display.delete(0, tk.END)

    def calculate(self):
        try:
            result = self.calculator.evaluate(self.expression)
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
            self.expression = str(result)
        except Exception as e:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")
            self.expression = ""


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.mainloop()
