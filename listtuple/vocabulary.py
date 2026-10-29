book1 = input("Enter words of Book 1: ").lower().split()
book2 = input("Enter words of Book 2: ").lower().split()

set1 = set(book1)
set2 = set(book2)
print("\nUnique words in Book 1:", set1)
print("Unique words in Book 2:", set2)

print("\nAll unique words:", set1 | set2)
print("Total unique words:", len(set1 | set2))

print("\nCommon words:", set1 & set2)

print("Words only in Book 1:", set1 - set2)
print("Words only in Book 2:", set2 - set1)
