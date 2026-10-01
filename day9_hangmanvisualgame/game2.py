import sys
import random

def load_words(path):
    try:
        words = []
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                word = line.strip()
                #print(repr(word))   # temporary, to see what each line looks like
                if word.isalpha():
                    words.append(word.lower())

#except OSError catches a whole family at once: file not found, path is a folder, permission denied. e.strerror gives a short readable reason like "No such file or directory".
    except OSError as e:
        print(f"Error: cannot read '{path}': {e.strerror}", file=sys.stderr)
        sys.exit(1)
#except UnicodeDecodeError catches files that aren't text (an image renamed to .txt, for example).
    except UnicodeDecodeError:
        print(f"Error: '{path}' is not a valid text file", file=sys.stderr)
        sys.exit(1)
#if not words: handles the case where the file opens fine but contains nothing usable. No exception happens there, so you must check it yourself. Without it, the next step (random.choice) would crash.
    if not words:
        print(f"Error: no valid words in '{path}'", file=sys.stderr)
        sys.exit(1)

    return words

# to end the game when you are out of trials
def you_lose(num):
    if num>=12:
        print("You lose!")
        return 1
    else:
        print("You have", 12-num, "chances")
        return 0

#At each step display found letters and spaces for what is to be found
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

def compare_results(past_results, hidden_word, num_attempts):

        if (num_attempts < past_results[0]) or (not past_results):
            print("Best ever! You guessed ", hidden_word, "in ", num_attempts, "attempts")
        else:
            print("The best ever was: ", past_results[0], " attempts")
        return 0


def play(unknown_word):
    return 0

def main():
    if len(sys.argv) < 2:
        print("Error: missing argument", file=sys.stderr)
        sys.exit(1)

    path = sys.argv[1]
    words = load_words(path)
    word_to_guess= random.choice(words)
    print("File given:", path)   # temporary line, just to see it works

if __name__ == "__main__":
    main()