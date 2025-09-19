import operator
import math 

class Calculator:
    def __init__(self):
        self._ops = {
            '+': operator.add,
            '-': operator.sub,
            'x': operator.mul,
            '/': operator.truediv,  # truediv for standard float division
            '%': operator.mod
        }
        self._func = {} # func like pow in the math lib etc
        self.menu()

    def menu(self) -> int:
        menu: str = '1. Addition\n' \
            '2. Subtraction\n' \
            '3. Multiplication\n' \
            '4. Division\n' \
            '5. Modular' \
            '6. Exit'
        menu_len = len(menu.splitlines())
        print(menu)

        while True:
            try:
                opt: int = int(input(f'Enter Operation (1-{menu_len}): '))
                return opt
            except ValueError as e:
                print(e)

    def add(self) -> int:
        sums: int = 0
        while True:
            try:
                add_num: str = input('Enter: ')
                add_num = "".join(add_num.split())
                if '+' not in add_num:
                    raise ValueError('wrong format')
                break
            except Exception as e:
                print(e)

        for num in add_num:
            num = num.strip()
            if num != '+':
                sums += int(num)

        return sums

    def subtract(self) -> int:
        diffs: int = 0
        while True:
            try:
                sub_num: str = input(
                    'Subtract numbers (a-b): ').strip().split(sep='-')
                if '-' not in sub_num:
                    raise ValueError('wrong format')
                break
            except Exception as e:
                print(e)

        for num in sub_num:
            num = num.strip()
            if num != '-':
                diffs -= int(num)

        return diffs

    def multiple(self):
        mux: int = 1
        while True:
            try:
                mux_num: str = input('Subtract numbers (axb): ').strip().split(sep='x')
                if 'x' not in mux_num:
                    raise ValueError('wrong format')
                break
            except Exception as e:
                print(e)

        for num in mux_num:
            num = num.strip()
            if num != 'x':
                mux *= int(num)

        return mux

    def divide(self):
        div: int = 0
        while True:
            try:
                div_num: str = input('Subtract numbers (a/b): ').strip().split(sep='/')
                if '/' not in div_num:
                    raise ValueError('wrong format')
                break
            except ValueError as e:
                print(e)
            except ZeroDivisionError as e:
                print(e)

        for num in div_num:
            num = num.strip()
            if num != '/':
                div /= int(num)

        return div
