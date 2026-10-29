import string
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
str1 = str1.lower()
str2 = str2.lower()

str1 = "".join(ch for ch in str1 if ch not in string.punctuation and ch != " ")
str2 = "".join(ch for ch in str2 if ch not in string.punctuation and ch != " ")

count1 = {}
count2 = {}

for ch in str1:
    count1[ch] = count1.get(ch, 0) + 1

for ch in str2:
    count2[ch] = count2.get(ch, 0) + 1

if count1 == count2:
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
