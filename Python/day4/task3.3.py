alphabet="abcdefghijklmnopqrstuvwxyz"
alphabet2='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def decrypt_key(key1, alphabet):
    key={}
    i=0

    for letter in key1:
        if letter.isalpha():
            j=alphabet.find(letter)
            key[i]=j
        else:
            key[i]=0

        i=i+1

    return key


def vigenere_encrypt(key, str, alphabet, alphabet2):
    new_str = ""
    key_position = 0

    for i in range(len(str)):
        flag = 0

        if str[i].isalpha():

            j = alphabet.find(str[i])

            if j == -1:
                flag = 1
                j = alphabet2.find(str[i])

            j = j + key[key_position]

            key_position = key_position + 1

            if key_position == len(key):
                key_position = 0

            if j >= 26:
                j = j - 26

            if flag == 0:
                new_str = new_str + alphabet[j]
            else:
                new_str = new_str + alphabet2[j]

        else:
            new_str = new_str + str[i]

    print(new_str)


raw_key='cat'
raw_key=raw_key.lower()

key=decrypt_key(raw_key, alphabet)

str=('he very first well-documented description of a polyalphabetic cipher was by Leon Battista Alberti around 1467 and used a metal cipher disk to switch between cipher alphabets. Albertis system only switched alphabets after several words, and switches were indicated by writing the letter of the corresponding alphabet in the ciphertext. Later, Johannes Trithemius, in his work Polygraphia (which was completed in manuscript form in 1508 but first published in 1518),[6] invented the tabula recta, a critical component of the Vigenère cipher.[7] The Trithemius cipher, however, provided a progressive, rather rigid and predictable system for switching between cipher alphabets')

vigenere_encrypt(key, str, alphabet, alphabet2)