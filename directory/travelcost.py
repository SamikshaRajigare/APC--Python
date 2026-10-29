import os

os.makedirs("Travel", exist_ok=True)

distance = float(input("Enter distance in km: "))
rate = float(input("Enter cost per km: "))

cost = distance * rate

with open("Travel/cost.txt", "w") as f:
    f.write(f"Distance: {distance} km\n")
    f.write(f"Rate: Rs. {rate} per km\n")
    f.write(f"Total cost: Rs. {cost}")

print("Travel cost saved")