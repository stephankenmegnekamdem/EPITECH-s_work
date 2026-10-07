# you can assigned a predefined value to  a function  then later give it a value if you want or use the default value
def my_count(*args):
    stop=args[0]
    if len(args)==1:
        start=0
    else:
        start=args[1]
    for i in range(start, stop+1):
        print(i)

def my_count_2(stop, start=0):
    for i in range(start, stop + 1):
        print(i)

my_count_2(50)
