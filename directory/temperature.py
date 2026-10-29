import os

os.makedirs("Temperature", exist_ok=True)

c = float(input("Enter temperature in Celsius: "))
f = (c * 9/5) + 32

with open("Temperature/temp.txt", "w") as file:
    file.write(f"Celsius: {c}\nFahrenheit: {f}")

print("Temperature result saved")