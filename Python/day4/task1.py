#task1.1
#(42>12) has true, it compares 2 integers and prints true or false
#12=12 assigns the value 12 to 12 == error because 12 is not a valid variable name
#12 == 12 verifies if both integers are equal, prints true
#”hello” == ”world” checks if both strings are equal, false
#218 >= 118 evaluates if 218 is greater than or equal to 118, true
#”a”.upper() == ”A” converts a to upper case and then compares to A hence true
#1 ∗ 2 ∗ 3 ∗ 4 <= 9 so 1*2*3*4=24 which is not less than or equal to 9 so false
#”z” in ”azerty” checks if z is in azerty hence true

#task1.2
num=input("Enter a number: ")
num=int(num)
if num==42:
    print("This is correct!")

#task1.3
def odd_or_even(num):
    if(num%2==0):
        print("Even")
    else:
        print("Odd")
num1=input("Enter a number:")
num1=int(num1)
odd_or_even(num1)

#task1.4
sen=input("Enter a sentence:")
if(sen=='open sesame'):
     print("access granted")
else:
    if(sen=='will you open, you goddamn !@&/°'):
       print("access fucking granted")
    else:
       print("permission denied")

#task1.5
num=input("Enter a number:")
num=int(num)
flag=0 #to verify if any of conditions are not met
if num==42:
    print("a")
    flag=1

if num<=21:
    flag=1
    print("b")

if num%2==0:
    flag=1
    print("c")

if (num/2)<21:
    flag=1
    print("d")

if num%2==0:
    if num>=45:
        flag=1
        print("e")

if flag==0:
    print("f")

#task1.6
#a == 42
a=42
#b == 41
b = 41
#if a = b
if a == b :
#print("A and B is the sames")
    print("A and B are the same")
#if b =< a
if b <= a :
#print("B is equal or lower as A")
    print("B is equal to or lower than A")
#if b =! a
if b != a :
#print("B his different from A")
    print("B is different from A")



