# task1.1(Learning list declaration)
list=[1, 2, 3, 4, 5]
print(list[0])


 # task1.2(printing last element of list)
i=list[-1]
print(i)


# task1.3(adding an element at end of list and a string)
list.append(42)
list.append('forty-two')


# task1.4(Displaying the entire list then element by element)
print(list)
for i in list:
    print(i)


# task1.5(deleting elements)del list[],del list[:], list.pop(), list.clear(), list.remove(element)
del list[-1]
print(list)


# task1.6(adding an element to beginning)
list.insert(0, 'hello')
print(list)


#task1.7(displaying elements form a particular index)
print(list[1:4])


#task1.8(displaying reversed list)
reversed_list = list[::-1]
print(reversed_list)


#task1.9(adding from 11 to 20 at end of list)
for i in range (11,21):
    list.append(i)

print(list)

#task1.10(understanding codes)

#my_first_list = [4, 5, 6]
        #creating a variable
#my_second_list = [1, 2, 3]
        #creating a second variable
#my_first_list.extend(my_second_list)
        #adding all variables of (my_second_list) to my_first_list starting from the end


#my_first_list = [7, 8, 9]
        #creating a variable
#my_second_list = [4, 5, 6]
        #creating a second variable
#my_first_list = [*my_first_list, *my_second_list]
        # join two lists according to the order given and stores in a list
#re.match(r'^1?$|^(11+?)\1+$', '1'*n) does nothing

#task1.11: Multiplying all elements of a list
list=[]
for i in range (5):
    list.append(i+1)  #use .append to add elements in lists

multiple=1
for i in list:      # for every element(i) in list
    multiple=multiple*i

print(multiple)

# task1.12: testing

print([x + 10 for x in [3, 2, 6, 7, 1, 4]])   #code adds 10 to each elemnet x in the list [3, 2, 6, 7, 1, 4]

# task1.13: finding smallest and biggest elements in a list
list=[4, 2, 8, 4, 6]
min=list[0]
max=list[0]
for i in list:
    if i<min:
        min=i
    if i>max:
        max=i

print(min, max)

#task1.14: sorting in descending order(search_sort, buble_sort
list=[10, 2, 7, 3, 11, 3, 14, 12, 5, 6, 7, 8, 9]

def search_sort(list):
    list_length=0
    for i in list:     #find length of list
        list_length+=1
    max=0
    temp=0

    for i in range(list_length-1): #for all elements - last one
        index = i+1
        max=list[i]

        for j in range(i+1, list_length): #verify the index of largest number
                if list[j]>max:
                    index=j
                    max=list[j]
        if index!=i+1:           #do the swapping if neccessary
                temp=list[index]
                list[index]=list[i]
                list[i]=temp

    print(list)

search_sort(list)

#task1.15: testing [x // 2 if x % 2 == 0 else x * 2 for x in [42, 3, 4, 18, 3, 10]]
print([x // 2 if x % 2 == 0 else x * 2 for x in [42, 3, 4, 18, 3, 10]])
#so for every x in list [42, 3, 4, 18, 3, 10] if c is even(x%2) do floor division of x by 2 else do x * 2


#task1.16: deleting duplicated elements


list1=[1,1,1,1,2,2,2,2,2]
list2=[42,'42', 42.0, 21+21, 42*10/10]

def delete_duplicated(my_list):
        new_list=[]
        for i in my_list:
            if i not in new_list:
                new_list.append(i)

        print(new_list)


delete_duplicated(list1)
delete_duplicated(list2)



