import csv
n = int(input("Enter number of transactions: "))
with open("transactions.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["TransactionType", "Amount"])
    for i in range(n):
        print("\nEnter transaction", i + 1)
        transaction_type = input(
            "Enter transaction type (Deposit/Withdrawal): "
        )
        amount = float(input("Enter amount: "))
        writer.writerow([transaction_type, amount])
def read_transactions():
    with open("transactions.csv", "r") as file:
        reader = csv.DictReader(file)
        return list(reader)
def total_deposits():
    transactions = read_transactions()
    total = 0
    for transaction in transactions:
        if transaction["TransactionType"].lower() == "deposit":
            total += float(transaction["Amount"])
    return total
def total_withdrawals():
    transactions = read_transactions()
    total = 0
    for transaction in transactions:
        if transaction["TransactionType"].lower() == "withdrawal":
            total += float(transaction["Amount"])
    return total
def final_balance():
    deposits = total_deposits()
    withdrawals = total_withdrawals()
    balance = deposits - withdrawals
    return balance
def largest_transaction():
    transactions = read_transactions()
    transaction = max(
        transactions,
        key=lambda x: float(x["Amount"])
    )
    return transaction
print("\nTotal Deposits:", total_deposits())
print("Total Withdrawals:", total_withdrawals())
print("Final Balance:", final_balance())
largest = largest_transaction()
print("\nLargest Transaction:")
print("Type:", largest["TransactionType"])
print("Amount:", largest["Amount"])
