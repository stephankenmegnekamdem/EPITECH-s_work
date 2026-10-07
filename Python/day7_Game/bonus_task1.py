#task1.1
#counting how many vowels and consonants there are in a sentence
def count_types(sentence):
    vowel_num = 0
    consonant_num = 0
    for letter in sentence:

        if letter.isalpha():

            if letter in "aeiouAEIOU":
                vowel_num += 1
            else:
                consonant_num += 1
    print(vowel_num, "vowels, ", consonant_num, "consonants")
count_types("Hello world!")

#task2.1
#palindrome words
def is_palindrome(input_word):
    i = len(input_word) - 1
    flag=0
    for j in range(len(input_word)):
        if input_word[j] != input_word[i]:
            flag=1
            return False
        else:
            i = i - 1

    if flag == 0 :
        return True

#task3.1
#anagram( 2 words consisting of the same letters
def is_anagram(word1, word2):
    flag = 0
    for i in word1:
        if i not in word2:
            flag = 1
            return False
    if flag == 0 :
        return True
print(is_anagram("listen", "silent"))



