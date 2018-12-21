from tqdm import tqdm
import os, sys

def encrypt(plaintext, key):
    cyphertext = ''
    for character in plaintext:
        if character.isalpha():
            number = ord(character)
            number += key%26
            if character.isupper():
                if number > ord('Z'):
                    number -= 26
                elif number < ord('A'):
                    number += 26
            elif character.islower():
                if number > ord('z'):
                    number -= 26
                elif number < ord('a'):
                    number += 26
            character = chr(number)
        cyphertext += character
    return cyphertext

def caesar(input_file, key):
    text = open(input_file,'r',encoding="utf8", errors='ignore').read()
    print(input_file)
    output_file = open(input_file, 'w', encoding= "utf-8", errors='ignore')
    for k in tqdm(range(1)):
        print("")
    cyphertext = encrypt(text, key)
    output_file.write(cyphertext)

def get_file(path):
    files = []
    for r, d, f in os.walk(path):
        for file in f:
            files.append(os.path.join(r, file))
    return files

if __name__ == '__main__':
    try:
        path = sys.argv[1]
        key = int(sys.argv[2])
        for file in get_file(path):
            caesar(file,key)
    except Exception as e:
        print("Something's wrong! Check your input again!\nError: ")
        print(e)