def summing(n):
    if n <= 0:
        return n
    else:
        return n + summing(n-1)

print(summing(42))