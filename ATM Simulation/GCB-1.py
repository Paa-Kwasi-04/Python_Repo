class ATM:
    def __init__(self):
        self.name = ""
        self.pin = 0
        self.amount = 0.0


class Node(ATM):
    def __init__(self):
        super().__init__()
        self.prev = None
        self.atm = [ATM() for _ in range(30)]
        self.next = None

    def search(self, pin, y):
        temp = y
        while temp.atm.pin != pin:
            temp = temp.next

        return temp

    def create_account(self, y):
        global choice
        while True:
            new_node = ATM()
            new_node.atm.name = input("Enter your Full name: ")
            new_node.atm.pin = int(input("Enter a four-digit pin number: "))
            new_node.atm.amount = float(
                input("Enter initial deposit amount: "))

            if y is None:
                y = temp = new_node
                new_node.prev = None
                new_node.next = None
            else:
                temp.next = new_node
                new_node.prev = temp
                new_node.next = None
                temp = new_node

            choice = int(input("Create another bank account (0 to stop): "))
            if choice == 0:
                break

        return y

    def delete_account(self, y):
        temp = y
        pin = int(input("Enter Account to be deleted: "))

        while temp.atm.pin != pin:
            pretemp = temp
            temp = temp.next

        pretemp.next = temp.next
        temp.next.prev = pretemp

        return y

    def deposit(self, y):
        pin = int(input("Enter your pin number: "))
        ptr = search(pin, y)

        amount = float(input("Enter amount to be deposited: "))
        ptr.atm.amount += amount

        return y

    def withdrawal(self, y):
        pin = int(input("Enter your pin number: "))
        ptr = search(pin, y)

        amount = float(input("Enter amount to be withdrawn: "))
        ptr.atm.amount -= amount

        return y

    def check_balance(self, y):
        pin = int(input("Enter your pin number: "))
        ptr = search(pin, y)

        return ptr.atm.amount


def main():
    global ans, x
    head = None

    while True:
        print("Welcome To GCB Bank PLC Limited\n")

        print("\n\n----ATM Services----\n"
              "\n1. Create bank account"
              "\n2. Deposit Cash"
              "\n3. Withdraw Money"
              "\n4. Check Balance"
              "\n5. Delete Account"
              "\n6. Exit")

        ans = int(input("\nWhich of the Services do You require: "))

        if ans == 1:
            head = create_account(head)
            print("Accounts have been created")
        elif ans == 2:
            head = deposit(head)
            print("Amount has been credited")
        elif ans == 3:
            head = withdrawal(head)
            print("Amount has been debited")
        elif ans == 4:
            x = check_balance(head)
            print("Your balance is: {}".format(x))
        elif ans == 5:
            head = delete_account(head)
            print("Account has been deleted")
        elif ans == 6:
            break
        else:
            print("Invalid response\nTry again")


if __name__ == "__main__":
    main()
