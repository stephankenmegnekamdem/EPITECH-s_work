def letter_frequency(input_word):
    letter_frequency_dict = {}
    for letter in input_word:
        if letter not in letter_frequency_dict:
            letter_frequency_dict[letter] = 1
        else:
            letter_frequency_dict[letter] += 1
    return letter_frequency_dict

def most_frequent_letter(input_word):
    input_dict = letter_frequency(input_word)
    highest_freq=0
    highest_freq_letters=[]
    most_frequent=""
    for letter in input_dict:
        if input_dict[letter] > highest_freq:
            highest_freq=input_dict[letter]
            highest_freq_letters.append(letter)
    most_frequent=min(highest_freq_letters)
    print(most_frequent)

most_frequent_letter("banana")