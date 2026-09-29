#2.1
import random
from english_words import english_words_lower_set
def n_long_words(input_dict, n):
    n_word_list = []
    for i in input_dict:
        if len(i) == n:
            yield i

def letter_only_words(input_dict):
    for i in input_dict:
        flag=0
        for letter in i:
            if not letter.isalpha():
                flag=1
                break
        if flag==0:
            yield i

def group_words_by_length(input_dict):
    ordered_dict = {}
    max=1
    for i in input_dict:
        if len(i) > max:
            max = len(i)
    for i in range(1, max+1):
        ordered_dict[i]=[]
        for word in input_dict:
            if len(word) == i:
                ordered_dict[i].append(word)

word_length=int(input("Enter a number"))
user_list=list(n_long_words(english_words_lower_set, word_length)) # add list because with yield in function, it works like a generator
print(random.choice(user_list))


