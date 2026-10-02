def my_division(num1, divisor):
    if divisor == 0:
        raise ZeroDivisionError
    else:
        quotient = num1 // divisor
        remainder =num1 % divisor
        return quotient, remainder

print(my_division(42, 4))