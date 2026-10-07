def check_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

a=[1, 2, 3, 4, 5, 6]
a=list(filter(check_even, a))
print(a)
