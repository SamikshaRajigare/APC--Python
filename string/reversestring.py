string = input("Enter a string: ")
reverse = ""
for i in range(len(string) - 1, -1, -1):
    reverse += string[i]
print("Reversed string:", reverse)