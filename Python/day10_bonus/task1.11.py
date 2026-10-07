def my_count(stop, start=0, step=1):

    if  not isinstance(stop, (int, float)):
        raise ValueError("stop must be an integer or float")

    if step!=0:
        if step >= 1 :
            if start > stop:
                temp = start
                start = stop
                stop = temp
            while start < stop:
                print(start)
                start += step
        else:
            if step<= -1:
                if start < stop:
                    temp = start
                    start = stop
                    stop = temp
                while start > stop:
                    print(start)
                    start += step


    else:
        print(start)

my_count(100, -100, -42)