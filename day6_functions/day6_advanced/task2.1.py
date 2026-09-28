def find_longest_word(words):
    length=[]
    max=0
    for i in words:
        count=len(i)
        length.append(count)
        if count>max:
            max=count
    j=length.index(max)
    print(words[j])

find_longest_word(['hello', 'hi', 'who are you', 'who am  you'])



