import sys
from ShuntingYardAlgorithm import ShuntingYardAlgo
from postfixEval import PostfixEval


def main():
    if len(sys.argv) > 1:
        expression = " ".join(sys.argv[1:])
    else:
        expression = input("Enter an infix expression: ")
    try:
        SYA = ShuntingYardAlgo()
        PFE = PostfixEval()
        postfix_exp = SYA.shunting_yard(expression)
        result = PFE.postfix_eval(postfix_exp)
        print(f"Infix: {expression}")
        print(f"Postfix: {postfix_exp}")
        print(f"Result: {result}")
    except KeyboardInterrupt:
        print("\nCalculation cancelled by user")
    except Exception as e:
        print(e)



if __name__ == '__main__':
    main()