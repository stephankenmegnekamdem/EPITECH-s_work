def encrypt(key, str):
    alphabet1='abcdefghijklmnopqrstuvwxyz'
    alphabet2='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_str=""
#to replace all letters
    for i in range(len(str)):
        flag = 0
        #is ita character
        if str[i].isalpha():
#position of character on reference

            j=alphabet1.find(str[i])
# verify if it is capital or low case letter/
            if j==-1:
                flag=1
                j=alphabet2.find(str[i])
    # add key to index of letter
            j=j+key
            if j>=25:
                j=j-26
            if flag==0:
                new_str=new_str+alphabet1[j]
            else:
                new_str=new_str+alphabet2[j]
        else:
            new_str=new_str+str[i]
    print(new_str)

key=input("Enter the key")
key=int(key)
str=input("Enter your sentence")
encrypt(key,str)