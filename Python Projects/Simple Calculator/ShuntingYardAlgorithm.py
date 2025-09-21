class ShuntingYardAlgo:
    """
    Implementation of Dijkstra's Shunting Yard Algorithm.

    This class converts infix mathematical expressions to postfix notation
    (Reverse Polish Notation) using the Shunting Yard Algorithm.

    Attributes
    ----------
    ops_precedence : dict
        Dictionary mapping operators to their precedence levels:
        - ^ : 3 (highest)
        - *, / : 2
        - +, - : 1 (lowest)

    Methods
    -------
    shunting_yard(infix_exp: str) -> str
        Converts an infix expression to postfix notation
    """

    def __init__(self):
        """
        Initialize the ShuntingYardAlgo with operator precedence.

        The precedence levels are:
        ^  : 3 (highest)
        *, / : 2
        +, - : 1 (lowest)
        """
        self.ops_precedence = {
            '^': 3,
            '*': 2,
            '/': 2,
            '+': 1,
            '-': 1    
        }

    def shunting_yard(self, infix_exp: str) -> str:
        # Initialize stacks for operators and output
        operator: list = []  # Stack to hold operators during processing
        output: list = []    # Stack to build the postfix expression

        # Split input string into tokens (numbers and operators)
        tokens = infix_exp.split()

        # Process each token in the infix expression
        for token in tokens:
            # Case 1: If token is a number, add directly to output
            if token.isdigit():
                output.append(token)

            # Case 2: If token is an opening parenthesis, push to operator stack
            elif token == '(':
                operator.append(token)

            # Case 3: If token is a closing parenthesis
            elif token == ')':
                # Pop operators until matching '(' is found
                while operator and operator[-1] != '(':
                    ops = operator.pop()
                    output.append(ops)
                # Remove the '(' from operator stack
                if operator:
                    operator.pop()

            # Case 4: If token is an operator (+, -, *, /, ^)
            elif token in self.ops_precedence:
                # While there's an operator at the top of the stack with greater precedence
                while (operator and                                    # Stack is not empty
                       operator[-1] != '(' and                        # Top is not an opening parenthesis
                       operator[-1] in self.ops_precedence and        # Top is an operator
                       self.ops_precedence[operator[-1]] >= self.ops_precedence[token]):  # Top has higher/equal precedence
                    # Pop the operator from the stack and add to output
                    ops = operator.pop()
                    output.append(ops)
                # Push the current operator to the stack
                operator.append(token)

            # Case 5: Unknown token (should not occur with valid input)
            else:
                operator.append(token)
        
        # After all tokens are processed, pop remaining operators to output
        while operator:
            ops = operator.pop()
            # Ignore any remaining parentheses
            if ops != '(':
                output.append(ops)

        # Join the output list with spaces to create the final postfix expression
        return ' '.join(output)


def main():
    """
    Main function to run the Shunting Yard Algorithm interactively.

    Allows users to input infix expressions and see their postfix equivalents.
    Continues until user chooses to stop.
    """
    SYA = ShuntingYardAlgo()
    while True:
        exp: str = input('Enter infix expression: ')
        print(f'{exp} = {SYA.shunting_yard(exp)}')

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
