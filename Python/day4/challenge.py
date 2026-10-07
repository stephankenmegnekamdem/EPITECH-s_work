def contains_vowel(str):
    for letter in str:
        if letter in 'aeiouAEIOU':
            return True
def is_greater(num):
    if num>=42:
        return True
print("Enter a sentence and a number")
s=input()
num=input()
num=int(num)
while num!=0:
    if contains_vowel(s):
        print (num)
        break
    else:
        if is_greater(num):
            print(num)
            break
        else:
            print(s)
            break
