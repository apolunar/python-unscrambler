import re

def load_words():
    mypattern = re.compile("^[a-z]{2,8}$")

    with open('words.txt') as word_file:
        valid_words = dict()

        for word in word_file.read().split():
            lword = word.lower()

            if mypattern.match(lword):
                mykey = ''.join(sorted(lword))

                wordList = valid_words.get(mykey)
                if not wordList:
                    wordList = set()
                    valid_words[mykey] = wordList

                wordList.add(word)

    word_file.close()
    return valid_words

if __name__ == '__main__':
    english_words = load_words()

possible_words = set()

while True:
    letters = input("Enter letters : ")

    if letters == "stop":
        break

    lettersSorted = ''.join(sorted(letters))

    wordsfound = english_words.get(lettersSorted)

    if wordsfound:
        print("possible words = {}".format(wordsfound))
    else:
        print("uh oh, no words found!!")
        
        
    
