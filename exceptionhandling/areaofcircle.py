try:
    r = float(input("Enter radius: "))
    if r < 0:
        raise ValueError("Radius cannot be negative.")

    print("Area =", 3.14 * r * r)
except ValueError as e:
    print("Error:", e)