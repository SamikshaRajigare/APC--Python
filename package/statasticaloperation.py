def mean(numbers):
    return sum(numbers) / len(numbers)

def maximum(numbers):
    return max(numbers)

def minimum(numbers):
    return min(numbers)

print(" Statistical Operations")
numbers = list(map(float, input(
    "Enter numbers separated by spaces: "
).split()))

if numbers:
    print("Mean:", mean(numbers))
    print("Maximum:", maximum(numbers))
    print("Minimum:", minimum(numbers))
else:
    print("Please enter at least one number.")