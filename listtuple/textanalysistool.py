text = input("Enter a text: ")
words = text.lower().split()
total_words = len(words)
frequency = {}
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1
print("\nWord Frequency:")
for word, count in frequency.items():
    print(word, ":", count)
top_3 = sorted(frequency.items(), key=lambda x: x[1], reverse=True)[:3]
print("\nTop 3 Most Frequent Words:")
for word, count in top_3:
    print(word, ":", count)
vowels = "aeiou"
vowel_count = 0
for char in text.lower():
    if char in vowels:
        vowel_count += 1
print("\nTotal number of words:", total_words)
print("Total number of vowels:", vowel_count)
