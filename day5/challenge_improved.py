import random
import time

### generate a random list of 100000 integers from 1 to 100
def random_list_create(num):
    my_random_list=[]
    for i in range(num):
        gen_num=random.randint(1,10000)
        my_random_list.append(gen_num)
    return(my_random_list)

### Sorts my_list (Stores in dict each number and its frequency)
def quick_sort(my_list):
    freq={}   #dictionary to store the frequency of each number and the number

# store each number and frequency in list
    for i in my_list:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

# Create new list (which will be the sorted list)
    new_list=[]
    maxi=0
    mini=0

# Max and Min are used to create the range (this way we iterate over every value in the dictionary)
   #find the smallest number
    for i in freq:
        if i>maxi:
            maxi=i

   #find the biggest number
    for i in freq:
        if i<mini:
            mini=i

    for i in range(mini, maxi+1):
        if i in freq:
            new_list.append(i)


    final_list=[]
    for i in new_list:
            for k in range(freq[i]):
                final_list.append(i)

    return final_list

### Initializations
num=100000
my_random_list=random_list_create(num)
start=time.time()

### Get List
my_list=quick_sort(my_random_list)

print(my_random_list)
print(my_list)
print(time.time()-start)


#i could still look for the largest number, calculate frequency of each number and from 1 to that big nnumber, if in dictionary, append to newsttring