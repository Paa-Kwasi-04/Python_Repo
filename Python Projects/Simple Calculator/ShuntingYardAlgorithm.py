

class ShuntingYardAlgo:
    def __init__(self):
        self.ops_precedence = {
            '^':3,
            '*':2,
            '/':2,
            '+':1,
            '-':1    
        }

    def shunting_yard(self,infix_exp:str):
        operator:list = []
        output:list = []

        tokens = infix_exp.split()

        for token in tokens:
            if token.isdigit():
                output.append(token)
            elif token == '(':
                operator.append(token)
            elif token == ')':
                while operator and operator[-1] != '(':
                    ops = operator.pop()
                    output.append(ops)
                if operator:
                    operator.pop()
            elif token in self.ops_precedence:
                while (operator and
                       operator[-1] != '(' and
                       operator[-1] in self.ops_precedence and
                       self.ops_precedence[operator[-1]] >= self.ops_precedence[token]):
                    ops = operator.pop()
                    output.append(ops)
                operator.append(token)
            else:
                operator.append(token)
        
        
        while operator:
            ops = operator.pop()
            if ops != '(':
                output.append(ops)

        return ' '.join(output)


def main():
    SYA = ShuntingYardAlgo()
    while True:
        exp: str = input(f'Enter infix expression: ')
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
