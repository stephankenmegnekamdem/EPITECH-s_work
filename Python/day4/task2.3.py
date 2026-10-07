def is_divisible_by(num, div):
    return num % div == 0
def numbers_from_10000_to_1(val):
    if is_divisible_by(val, 7):
        print (val)
i=10000
while  i>1 :
    numbers_from_10000_to_1(i)
    i=i-1
