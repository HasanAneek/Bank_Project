from bank_account import *

John = BankAccount(5000, 'John')
Smith = BankAccount(3000, 'Smith')

John.get_balance()
Smith.get_balance()

Smith.deposit(500)

John.withdraw(1000)

John.transfer(50, Smith)


Jim = InterestReward(1000, "Jim")

Jim.get_balance()

Jim.deposit(100)

Jim.transfer(100, John)

Blaze = SavingsAccount(1000, "Blaze")

Blaze.get_balance()

Blaze.deposit(100)

Blaze.transfer(10000, Smith)
Blaze.transfer(1000, Smith)






