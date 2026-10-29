def simple_interest(p, r, t):
    si = (p * r * t) / 100
    return si
p = float(input("Enter Principal amount: "))
r = float(input("Enter Rate of interest: "))
t = float(input("Enter Time: "))
print("Simple Interest:", simple_interest(p, r, t))
