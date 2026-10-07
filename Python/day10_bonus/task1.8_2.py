def my_sum(*args):
        total = 0
        for x in args:
            if  not isinstance(x , (float, int)):

                raise ValueError("Arguments must be numbers")

            total += x
        print(total)




