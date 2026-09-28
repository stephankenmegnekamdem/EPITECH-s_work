def palindrome(sentence):
    new_sentence = ""
    for letter in sentence:
        if letter.isalpha():
            new_sentence=new_sentence+letter.lower()
    count=len(new_sentence)%2
    mid=len(new_sentence)//2
    sentence1 = new_sentence[:mid]
    if count!=0:
        sentence2 = new_sentence[mid+1:]
    else:
        sentence2 = new_sentence[mid:]

    sentence2=sentence2[::-1]
    if sentence1==sentence2:
            return True
    else:
            return False


print(palindrome("A Santa Lived As a Devil at NASA"))