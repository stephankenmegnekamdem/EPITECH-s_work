def word_frequency(file_name):
    try:
        with open(file_name, "r") as file:
            content=file.read()
            frequency = {}
            for word in content.split():
                word.lower()
                for letter in word:
                    if not letter.isalpha():
                        word = word.replace(letter, "")
                if word in frequency:
                    frequency[word] += 1
                else:

                    frequency[word] = 1
        return frequency
    except FileNotFoundError:
        print("File not found")
    except UnicodeDecodeError:
        print("UnicodeDecodeError")

print(word_frequency("zen.txt"))




