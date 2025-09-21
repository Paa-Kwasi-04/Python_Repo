"""
Simple Calculator Main Module

This module provides a command-line interface for a calculator that converts
infix expressions to postfix notation and evaluates them.

The calculator supports:
- Basic arithmetic operations (+, -, *, /, ^)
- Parentheses for grouping
- Both command-line and interactive input
- Flexible input format (handles arbitrary whitespace)

Examples
--------
Command line usage:
    python main.py "3+4*2"
    python main.py "3 + 4 * 2"
    python main.py "3+  4  *2"

Interactive usage:
    python main.py
    Enter an infix expression: 3+4*2
"""

import sys
import re
from ShuntingYardAlgorithm import ShuntingYardAlgo
from postfixEval import PostfixEval


def format_expression(expression: str) -> str:
    """
    Format mathematical expression to have proper spacing.

    Parameters
    ----------
    expression : str
        Raw input expression with arbitrary spacing

    Returns
    -------
    str
        Formatted expression with single spaces between tokens

    Examples
    --------
    >>> format_expression("3+4*2")
    "3 + 4 * 2"
    >>> format_expression("(1+  2)*3")
    "( 1 + 2 ) * 3"
    """
    # Remove all whitespace first
    expression = "".join(expression.split())
    
    # Add space around operators and parentheses
    # Look for numbers, operators, or parentheses
    tokens = re.findall(r'(?:\d*\.?\d+)|[()+\-*/^]', expression)
    
    # Join tokens with single spaces
    return " ".join(tokens)


def main():
    """Main entry point for the calculator application."""
    if len(sys.argv) > 1:
        # Join all arguments and format
        raw_expression = "".join(sys.argv[1:])
    else:
        raw_expression = input("Enter an infix expression: ")
    
    try:
        # Format the expression with proper spacing
        expression = format_expression(raw_expression)
        
        SYA = ShuntingYardAlgo()
        PFE = PostfixEval()
        
        postfix_exp = SYA.shunting_yard(expression)
        result = PFE.postfix_eval(postfix_exp)
        
        print(f"Expression: {expression}")
        print(f"Postfix: {postfix_exp}")
        print(f"Result: {result}")
        
    except KeyboardInterrupt:
        print("\nCalculation cancelled by user")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    main()