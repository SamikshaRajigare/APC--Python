import os

os.makedirs("Shopping", exist_ok=True)

price = float(input("Enter shopping amount: "))
discount = price * 0.10
final = price - discount

with open("Shopping/bill.txt", "w") as f:
    f.write(f"Original price: Rs. {price}\n")
    f.write(f"Discount: Rs. {discount}\n")
    f.write(f"Final amount: Rs. {final}")

print("Shopping bill saved")