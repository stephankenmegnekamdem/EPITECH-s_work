def characters_2times(s):
    s1=""
    for letter in s:
        for i in range(2):
            s1=s1+letter
    print(s1)
sen=input("Enter a sentence:")
characters_2times(sen)