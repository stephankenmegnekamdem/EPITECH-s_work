import random
import time
start_time = time.time()
from english_words import english_words_lower_set # python3 -m pip  install english-words==1.1.0 to download package
# PIP (Package Installer for Python) to install packages
#use good variable name


# first brick
def you_lose(num):
    if num>=12:
        print("You lose!")
        return 1
    else:
        print("You have", 12-num, "chances")
        return 0


# next brick
def random_value(sen):
    length = len(sen)
    index = random.randint(0,(length-1))  #returns a random number
    return sen[index]


# import package
def random_word():
    #choosing a random word from english_word_lower_set:
    # word = random.choice(list(english_words_lower_set))
    with open("word_list.txt", "r") as file:
        words = file.read().splitlines()

    my_word = random.choice(words)
    return my_word


#another brick
def display_correctly_guessed(letters_guessed, my_word, user_guess):
    letters_guessed = letters_guessed.replace(" ", "")
    new_string = ""

    for i in range(len(my_word)):
        if user_guess == my_word[i]:
            new_string += user_guess
        else:
            if letters_guessed[i] == my_word[i]:
                new_string += my_word[i]
            else:
                new_string += "_ "

    return new_string



#program start(main)
trials=0
word_to_guess = random_word()
current_guess = ""
temporary= ""
for i in range(len(word_to_guess)):
    temporary= temporary + "_"
passed_guess = display_correctly_guessed(temporary, word_to_guess, current_guess)
penalty=0
Stop=0

print("Let's get started: Here's the word: ", passed_guess)

while passed_guess != word_to_guess and Stop==0:
        count=0


        #time constraint
        if time.time() - start_time >= 30 * 60:

            print("Time's up!")

            break

        if (trials != 0):
            trials += 1
            print("Let's continue")
            current_guess=input("What's your next guess ?")
        else:
            trials = trials + 1
            print("Let's get started")
            current_guess = input("What's your first guess ?")

        if current_guess in passed_guess:
            print("You already tried this letter")
            print('Try a different letter')
            continue




        if  (len(current_guess)>1):
            full_word=current_guess.lower()

            if (full_word == word_to_guess):
                passed_guess = full_word
                break
            else:
                print(current_guess, ": incorrect guess")
                print("You got -5 for wrong word")
                penalty+=5
                Stop = you_lose(penalty)
                print(passed_guess)
#bonus task2.3 a hint part to help find the word

        else:
            if (current_guess == "?"):
                if (penalty >= 10):
                    print("Sorry, you cant use the hint now")
                    Stop = you_lose(penalty)
                    continue
                else:
                    count = passed_guess.count("_")
                    if count == 1:
                        print("Sorry, you cant use hint now, you have just one letter to find")
                        Stop = you_lose(penalty)
                        continue
                    else:
                        penalty += 2
                        temporary = passed_guess
                        temporary = temporary.replace(" ", "")
                        possible_letters=[]
                        for i in range(len(word_to_guess)):
                            if passed_guess[i] == "_" :
                                possible_letters.append(word_to_guess[i])

                        current_guess = random.choice(possible_letters)
                        print("Here's letter ", current_guess)
                        temporary = passed_guess
                        passed_guess = display_correctly_guessed(temporary, word_to_guess, current_guess)
                        print(passed_guess)
                        Stop = you_lose(penalty)
                        continue

#end of  hint

            else:


                if current_guess in word_to_guess:
                    for i in word_to_guess:
                        if i == current_guess:
                            count += 1
                    print("Great you found", count, "letter: ", current_guess)
                    temporary = passed_guess
                    passed_guess = display_correctly_guessed(temporary, word_to_guess, current_guess)
                    print(passed_guess)
                    Stop = you_lose(penalty)


                else:
                    print("Sorry wrong guess:")
                    penalty += 1
                    Stop = you_lose(penalty)
                    print(passed_guess)



if    (passed_guess == word_to_guess):
    print("Congrats! you made it after", trials, "trials")
else:
    print("The word was", word_to_guess)
