# word_scramble
import random
def random_word():
    with open ("word_list.txt", "r") as file:
        words = file.read().splitlines()
    my_word = random.choice(words)
    return my_word

def word_shuffler(input_word):
    if len(input_word) == 0:
        return ""

    i = random.randint(0, len(input_word) - 1)

    letter = input_word[i]

    input_word = input_word[:i] + input_word[i + 1:]

    return letter + word_shuffler(input_word)
word_to_guess = random_word()
shuffled_word = word_shuffler(word_to_guess)

while word_to_guess == shuffled_word:
    shuffled_word = word_shuffler(word_to_guess)

print("What's the original word from which", shuffled_word, "was made")
for i in range(12):

    user_guess=input("Enter a word")
    if user_guess == word_to_guess:
        print("Correct!")
        break
    else:
        print("Sorry, but that is not the word")
        print("You have ", 12-i, " guesses left.")
