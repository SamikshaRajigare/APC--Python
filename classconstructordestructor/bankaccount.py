class BankAccount:
    account_counter = 1000
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0

        BankAccount.account_counter += 1
        self.account_number = BankAccount.account_counter

        print(f"Account created for {self.account_holder}")
        print(f"Account Number: {self.account_number}")
    def deposit(self, amount):
        self.balance += amount
        print(f"₹{amount} deposited.")
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn.")
        else:
            print("Error: Insufficient funds.")
    def display_balance(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: ₹{self.balance}")
    def transfer(self, amount, other_account):
        if amount <= self.balance:
            self.balance -= amount
            other_account.balance += amount
            print(
                f"₹{amount} transferred from "
                f"{self.account_holder} to {other_account.account_holder}."
            )
        else:
            print("Error: Insufficient funds for transfer.")
    def __del__(self):
        print(f"Account of {self.account_holder} is destroyed.")
account1 = BankAccount("Rahul")
account2 = BankAccount("Priya")
print("\nDeposits ")
account1.deposit(5000)
account2.deposit(3000)
print("\n Withdrawals ")
account1.withdraw(1000)
account2.withdraw(500)
print("\nTransfer ")
account1.transfer(1500, account2)
print("\nFinal Balances ")
account1.display_balance()
account2.display_balance()
del account1
del account2

