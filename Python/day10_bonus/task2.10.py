def letter_frequency(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            frequency={}
            for word in content.split():
                word = word.lower()
                for letter in word:
                    if letter not in frequency:
                        frequency[letter] = 1
                    else:
                        frequency[letter] += 1
            frequency = dict(sorted(frequency.items(), key=lambda item: item[0]))
            return frequency
    except FileNotFoundError:
        print("File not found")
    except PermissionError:
        print("Permission denied")
    except UnicodeDecodeError:
        print("Unicode error")


print(letter_frequency("zen.txt"))


