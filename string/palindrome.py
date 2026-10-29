string = input("Enter a string: ")
reverse = ""
for i in range(len(string) - 1, -1, -1):
    reverse += string[i]
if string == reverse:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")