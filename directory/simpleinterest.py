import os

os.makedirs("Interest", exist_ok=True)

p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time in years: "))

si = (p * r * t) / 100

with open("Interest/interest.txt", "w") as f:
    f.write(f"Simple Interest: {si}\n")
    f.write(f"Total Amount: {p+si}")

print("Interest details saved")