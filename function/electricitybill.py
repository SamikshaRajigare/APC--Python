def calculate_energy_charge(units):
    if units <= 100:
        charge = units * 5
    elif units <= 200:
        charge = (100 * 5) + ((units - 100) * 7)
    else:
        charge = (100 * 5) + (100 * 7) + ((units - 200) * 10)
    return charge
def calculate_fixed_charge():
    return 100
def calculate_tax(amount):
    return amount * 0.05
def calculate_discount(amount):
    if amount > 2000:
        return amount * 0.10
    else:
        return 0
def calculate_bill(units):
    energy_charge = calculate_energy_charge(units)
    fixed_charge = calculate_fixed_charge()

    subtotal = energy_charge + fixed_charge
    tax = calculate_tax(subtotal)
    discount = calculate_discount(subtotal)

    total = subtotal + tax - discount

    print("\nElectricity Bill")
    print("Energy Charge:", energy_charge)
    print("Fixed Charge:", fixed_charge)
    print("Tax:", tax)
    print("Discount:", discount)
    print("Total Bill:", total)
units = int(input("Enter electricity units consumed: "))
calculate_bill(units)
