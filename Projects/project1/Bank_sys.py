class BankAcount:
    def __init__(self, balance: float = 0.0) -> None:
        self.balance = balance
        self.transaction = []

    def deposit(self, amount: float) -> None:
        if amount > 0:
            self.balance += amount
            self.transaction.append(f"Deposit ${amount: 2f}")
            print(
                f"Deposited ${amount: .2f}, Current balance ${self.balance: .2f}")
        else:
            print("Value must be positive")

    def withdraw(self, amount: float) -> None:
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                self.transaction.append(f"Withdraw ${amount: 2f}")
                print(
                    f"withdrawn ${amount: .2f}, Current balance ${self.balance: .2f} ")
            else:
                print("Insufficient_balance")
        else:
            print("Withdraw amount must be positive")

    def history(self) -> None:
        print("--Transaction-History-- \n")
        if not self.transaction:
            print("No transactions yet")
        else:
            for t in self.transaction:
                print(t)
        print(f"Current balance ${self.balance: .2f}")

    def check_balance(self) -> None:
        #  self.transaction.append(f"Withdraw ${self.balance: .2f}")
        print(f"Current balance ${self.balance: .2f}")


def main() -> None:

    account = BankAcount(1000.0)
    while True:
        print("\n--Banking System--")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check_Balance")
        print("4. Transaction_history")
        print("5. Exit")
        choice = (input("chose option: "))
        if choice == '1':
            try:
                amount = float(input("Enter amount: $"))
                account.deposit(amount)
            except ValueError:
                print("Invalid input try again")
        elif choice == '2':
            try:
                amount = float(input("Enter amount: $"))
                account.withdraw(amount)
            except ValueError:
                print("Invalid input try again")
        elif choice == '3':
            try:
                account.check_balance()
            except ValueError:
                print("Invalid input try again")
        elif choice == '4':
            try:
                account.history()
            except ValueError:
                print("Invalid input try again")
        elif choice == '5':

            print("Goodbye!")
            break
        else:
            print("Invalid input")


if __name__ == "__main__":
    main()
