import num2words
def count_letters(num):
    count = 0
    for i in range(1,num+1):
        num_in_letters= num2words.num2words(i, lang="en")
        for letter in num_in_letters:
            if letter.isalpha():
                count += 1
    return count
print(count_letters(1000))
