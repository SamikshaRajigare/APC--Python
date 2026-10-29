try:
    n = int(input("Enter a number: "))

    if n % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

except ValueError:
    print("Invalid input! Enter an integer.")