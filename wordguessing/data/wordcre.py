"""this is a script that is created for generating words for the game 
by getting a corpera."""

from nltk.tokenize import word_tokenize



def open_file(path, lang):
    """this function will open the file that the path of 
    it is givven and then tokenize and ngram it and return the result"""

    with open(file = path, mode='r', encoding="utf-8") as file:

        text = file.read()
        words = word_tokenize(text,language=lang)

    return words

def check(words):
    """this func checks all the words for finding the best one to use"""

    CHARACTERS = "0123456789!@#$%&*(_+=-'/\|.,><~` )"
    accepted_words = []
    accepted_word_length = 6
    inde = False

    for  word in words:
        for letter in word:

            if letter in CHARACTERS :
                inde = False
                break
            else:
                inde = True

        if inde and len(word) >= accepted_word_length:
            if word not in accepted_words:
                accepted_words.append(word)
        
    return accepted_words

def save(path, words):
    """this method save whole the words 
    in the givven path"""

    with open(file= path, mode='a', encoding='utf-8') as file:

        for word in words:
            file.write(word+'\n')












