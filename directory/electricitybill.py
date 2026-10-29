import os

os.makedirs("Electricity", exist_ok=True)

units = float(input("Enter units consumed: "))
bill = units * 5

with open("Electricity/bill.txt", "w") as f:
    f.write(f"Units: {units}\n")
    f.write(f"Rate per unit: Rs. 5\n")
    f.write(f"Total bill: Rs. {bill}")

print("Bill saved in Electricity directory")