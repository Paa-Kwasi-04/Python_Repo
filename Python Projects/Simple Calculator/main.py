import argparse
from ShuntingYardAlgorithm import ShuntingYardAlgo
from postfixEval import PostfixEval


def main():
    parser = argparse.ArgumentParser(description='Calculates Infix Expressions')
    parser.add_argument(
        'expression', help='Infix expression to evaluate (use quotes)')
    args = parser.parse_args()

    SYA = ShuntingYardAlgo()
    PFE = PostfixEval()
    postfix_exp = SYA.shunting_yard(args.expression)
    result = PFE.postfix_eval(postfix_exp)
    print(f"Infix: {args.expression}")
    print(f"Postfix: {postfix_exp}")
    print(f"Result: {result}")


if __name__ == '__main__':
    main()