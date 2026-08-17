def fibonacci_iterative(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1

    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c

    return b


n = int(input("Enter n: "))
print("Fibonacci number:", fibonacci_iterative(n))
