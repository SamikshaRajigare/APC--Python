import os

os.makedirs("Arithmetic", exist_ok=True)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

with open("Arithmetic/result.txt", "w") as f:
    f.write(f"Addition: {a+b}\n")
    f.write(f"Subtraction: {a-b}\n")
    f.write(f"Multiplication: {a*b}\n")
    if b != 0:
        f.write(f"Division: {a/b}\n")

print("Results saved in Arithmetic directory")