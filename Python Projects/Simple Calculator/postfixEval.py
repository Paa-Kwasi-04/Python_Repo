import operator
import math

class PostfixEval:
    """
    A class to evaluate postfix expressions.

    This class implements a postfix (Reverse Polish Notation) calculator
    that supports basic arithmetic operations.

    Attributes
    ----------
    _ops : dict
        Dictionary mapping operator symbols to their corresponding functions

    Methods
    -------
    postfix_eval(expression: str) -> int
        Evaluates a postfix expression and returns the result
    """

    def __init__(self):
        """
        Initialize PostfixEval with supported operators.

        The supported operators are:
        +  : Addition
        -  : Subtraction
        *  : Multiplication
        /  : Floor Division
        ^  : Exponentiation
        """
        
        self._ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.floordiv,
            '^': math.pow
        }

    def postfix_eval(self, expression: str) -> int:
        """
        Evaluate a postfix expression.

        Parameters
        ----------
        expression : str
            The postfix expression to evaluate. Tokens should be space-separated.

        Returns
        -------
        int
            The result of evaluating the expression

        Examples
        --------
        >>> calc = PostfixEval()
        >>> calc.postfix_eval("2 3 +")
        5
        >>> calc.postfix_eval("2 3 4 * +")
        14

        Notes
        -----
        The expression must be in valid postfix notation with space-separated tokens.
        Supported operators are +, -, *, /, and ^.
        """
        stack: list = []
        exp: str = expression.split()

        for token in exp:
            if token.isdigit():
                stack.append(int(token))
            elif token in self._ops:
                var1 = stack.pop()
                var2 = stack.pop()
                stack.append(self._ops[token](var2, var1))

        if stack:
            return int(stack.pop())


def main():
    """
    Main function to run the postfix calculator interactively.

    Allows users to input postfix expressions and see their results.
    Continues until user chooses to stop.
    """
    pos_eval = PostfixEval()
    while True:
        exp: str = input('Enter postfix expression: ')
        print(f'{exp} = {pos_eval.postfix_eval(exp)}')

        while True:
            try:
                again: str = input('Will you go again (y/n): ').strip().lower()
                if again not in ['y', 'n']:
                    raise ValueError('Invalid Response (y/n)')
                else:
                    break
            except Exception as e:
                print(e)
        if again == 'n':
            break


if __name__ == '__main__':
    main()
