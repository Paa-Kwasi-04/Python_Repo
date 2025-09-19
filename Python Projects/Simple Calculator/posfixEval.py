import operator
import math


ops = {
    '+':operator.add,
    '-':operator.sub,
    '*':operator.mul,
    '/':operator.floordiv,
    '^':math.pow
}

def postfix_eval(expression:str)->int:
    stack:list = []
    exp: str = expression.split()

    for token in (exp):

        if token.isdigit():
            print(f'Pushing {token} to stack')
            stack.append(int(token))
        
        elif token == '+':
            var1 = stack.pop()
            var2 = stack.pop()
            print(f'Adding {var1} and {var2}')
            stack.append(ops[token](var2,var1))
            print(f'Putting addition result in stack')

        elif token == '-':
            var1 = stack.pop()
            var2 = stack.pop()
            print(f'Subtracting {var1} from {var2}')
            stack.append(ops[token](var2,var1))
            print(f'Putting subtraction result in stack')

        elif token == '*':
            var1 = stack.pop()
            var2 = stack.pop()
            print(f'Multiplying {var1} and {var2}')
            stack.append(ops[token](var2, var1))
            print(f'Putting multiplication result in stack')

        elif token == '/':
            var1 = stack.pop()
            var2 = stack.pop()
            print(f'Dividing {var2} by {var1}')
            stack.append(ops[token](var2, var1))
            print(f'Putting multiplication result in stack')

        elif token == '^':
            var1 = stack.pop()
            var2 = stack.pop()
            print(f'Raising {var2} to power {var1}')
            stack.append(ops[token](var2, var1))
            print(f'Putting multiplication result in stack')

    if stack :
        return int(stack.pop())


def main():
    while True:
        exp:str = input(f'Enter posfix expression: ')
        print(f'{exp} = {postfix_eval(exp)}')

        while True:
            try:
                again:str = input('Will you go again (y/n): ').strip().lower()
                if again not in ['y','n']:
                    raise ValueError('Invalid Response (y/n)')
                else:
                    break
            except Exception as e:
                print(e)
        if again == 'n':
            break

if __name__ == '__main__':
    main()
    print('Program has ended')
