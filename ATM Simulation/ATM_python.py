class ATM:
    def __init__(self):
        self.balance:float = 0

    def check_balance(self):
        return self.balance

    def deposit_money(self,amount):
        if amount <= 0:
            raise ValueError('Deposit amount must be positive.')
        
        self.balance += amount

    def withdraw_money(self,amount):
        if amount > self.balance:
            raise ValueError('Insufficient funds.')
        
        if amount <= 0:
            raise ValueError('Withdrawal amount must be positive.')

        self.balance -= amount


class ATM_UI:
    def __init__(self):
        self.atm = ATM()

    def display_menu(self):
        while True:
            print('Welcome to the ATM!')
            print('1.\tCheck Balance')
            print('2.\tDeposit')
            print('3.\tWithdraw')
            print('4.\tExit')

            try:
                option = int(input('Please choose an option: '))
                if option < 1 or option > 4:
                    print('Enter a valid option from 1 to 4.')
                    continue
                return option
            except ValueError:
                print('Enter a valid integer option (1-4).')
                continue


    def get_amount(self, prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print('Please enter a valid number.')
                continue

    def check_balance(self):
        balance = self.atm.check_balance()
        print(f'Your current balance is: ${balance}')

    def deposit_money(self):
        while True:
            try:
                amount = self.get_amount('Enter amount to deposit: ')
                self.atm.deposit_money(amount)
                print(f'${amount} deposited successfully.')
                break
            except ValueError as error:
                print(error)

    def withdraw_money(self):
        while True:
            try:
                amount = self.get_amount('Enter amount to withdraw: ')
                self.atm.withdraw_money(amount)
                print(f'${amount} withdrawn successfully.')
                break
            except ValueError as error:
                print(error)

    def run(self):
        while True:
            option = self.display_menu()

            if option == 1:
                self.check_balance()
            elif option == 2:
                self.deposit_money()
            elif option == 3:
                self.withdraw_money()
            else:
                break
        



def main():
    atm = ATM_UI()
    atm.run()
    print('Thank you for using the ATM. Goodbye!')


if __name__ =='__main__':   
    main()