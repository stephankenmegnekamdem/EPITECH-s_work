def decrypt(str, key):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    alphabet=alphabet[::-1]
    alphabet2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet2 = alphabet2[::-1]
    new_str=""
    for i in range(len(str)):
        if str[i].isalpha():
            flag=0
            j=alphabet.find(str[i])
            if j==-1:
                flag=1
                j=alphabet2.find(str[i])
            j=j+key
            if j>=25:
                j=j-26
            if flag == 0:
                new_str = new_str + alphabet[j]
            else:
                new_str = new_str + alphabet2[j]
        else:
            new_str+=str[i]

    return new_str

key=input("Enter the key")
key=int(key)
str=input("Enter your sentence")
ans=decrypt(str, key)
print(ans)
