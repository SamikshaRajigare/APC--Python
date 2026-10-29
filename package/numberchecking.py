def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def is_armstrong(n):
    if n < 0:
        return False
    digits = str(n)
    return sum(int(d) ** len(digits) for d in digits) == n
def is_palindrome(n):
    return str(n) == str(n)[::-1]

print(". Number Checking")
n = int(input("Enter an integer: "))

print("Prime:", is_prime(n))
print("Armstrong:", is_armstrong(n))
print("Palindrome:", is_palindrome(n))


