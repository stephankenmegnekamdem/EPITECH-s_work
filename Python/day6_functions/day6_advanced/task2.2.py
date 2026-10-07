def count_digits(n):
     if n // 10 == 0:
         return 1
     else:
         return 1 + count_digits(n // 10)

print(count_digits(42000))
