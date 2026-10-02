def longest_word(file_name):
    try:
        with open(file_name, "r") as f:
            content = f.read()
            longest = max(content.split(), key=len)
            return longest
    except FileNotFoundError:
        return ""
print(longest_word("zen.txt"))