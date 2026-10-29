try:
    balance = 5000
    amount = float(input("Enter withdrawal amount: "))

    if amount < 0:
        raise ValueError("Amount cannot be negative.")
    elif amount > balance:
        raise ValueError("Insufficient balance.")
    else:
        balance -= amount
        print("Withdrawal successful.")
        print("Remaining balance =", balance)
except ValueError as e:
    print("Error:", e)