class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self, initial_amount, account_name):
        self.balance = initial_amount
        self.name = account_name
        print(f"\nAccount '{self.name}' created. Balance= ${self.balance:.2f}")

    def get_balance(self):
        print(f"\nAccount '{self.name}' Balance: ${self.balance:.2f}")


    def deposit(self, amount):
        self.balance = self.balance + amount
        print("\nDeposit complete.")
        self.get_balance()

    def viable_transaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry account '{self.name}' only have ${self.balance:.2f}"
            )

    def withdraw(self, amount):
        try:
            self.viable_transaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw Successfully Completed!")
            self.get_balance()
        except BalanceException as error:
            print(f'\nWithdraw Interrupted: {error}')


    def transfer(self, amount, account):
        try:
            print("\nTransfer Started...")
            self.viable_transaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\nTransfer Successfully Completed!!!")
        except BalanceException as error:
            print(f'\nTransfer Invalid: {error}')



class InterestReward(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit Complete")
        self.get_balance()



class SavingsAccount(InterestReward):
    def __init__(self, initial_amount, account_name):
        super().__init__(initial_amount, account_name)
        self.fee = 5


    def withdraw(self, amount):
        try:
            self.viable_transaction(self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdraw Completed")
            self.get_balance()
        except BalanceException as error:
            print(f"\nWithdraw Interrupted: {error}")




