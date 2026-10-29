string = input("Enter a string: ")
if len(string) > 0:
    print("First character =", string[0])
    print("Last character =", string[len(string) - 1])
else:
    print("String is empty")