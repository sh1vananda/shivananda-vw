def factorial(num):
    if num in (0, 1):
        return 1
    res = 1
    for i in range(2, num + 1):
        res *= i
    return res

for i, n in enumerate(range(11), start = 0):
    print(f"factorial of {i}: {factorial(n)}")

