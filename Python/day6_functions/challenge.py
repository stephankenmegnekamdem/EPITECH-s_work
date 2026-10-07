def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        if exponent % 2 == 0:
            half = power(base, exponent//2)
            return half * half
        else:
            ans = base * power(base, exponent-1)
            return ans


print(power(42, 84))