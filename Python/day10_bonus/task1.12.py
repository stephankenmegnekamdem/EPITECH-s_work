def my_division(num , den, acc=1):
    if acc <  1:
        acc=1
    ans = num / den
    return round(ans, acc)
print(my_division(8.4, 13, 6))