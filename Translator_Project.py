from gettext import translation
import csv

class DictionaryDefinition():
    """Defining a dictionary for usage."""

    def WordsCSV():
        """Storing the CSV into a list,"""
        filename = 'pl_di_csv.csv'
        with open(filename) as dictio:
            reader = csv.reader(dictio)
            pl_en_equivalents = next(reader)
            return pl_en_equivalents

    def CreatingDictionary():
        """making a dictionary that stores the words from each language."""

        pl_words = []
        en_words = []
        dictionary = {}
        pl_en_equivalents = DictionaryDefinition.WordsCSV()

        for i in range (0,int(len(pl_en_equivalents))): #slicing the whole list into separate lists
            if divmod(i,2)[1] == 0:
                en_words.append(pl_en_equivalents[i])
                pl_words.append(pl_en_equivalents[i+1])

        for i in range (0,int(len(pl_en_equivalents)/2)): #making them turn into a dictionary.
            dictionary[en_words[i]] = pl_words[i] #en_words is the key and pl_words is the value.
        return dictionary

class Translator():
    """Gives the translation of the message."""

    def UserInput():
        """store the user input into a list."""

        my_word = input("Which word do you want me to translate? ")  # storing the user's intended word/phrase.
        list_message = my_word.split()  # list_message is a list which has every word typed by the user.
        return list_message

    def TranslatingWords():
        """Shows the polish word for the input."""

        translation = ""
        dictionary = DictionaryDefinition.CreatingDictionary()
        list_message = Translator.UserInput()

        DictionaryDefinition.CreatingDictionary()

        for word_message in list_message:

            for key, value in dictionary.items():

                if key == word_message.lower(): #Line 10
                    translation += f"{value} "
        print(translation.rstrip() + ".\n")

Translator.TranslatingWords()

"""my_word = input("Which word do you want me to translate? ")  # storing the user's intended word/phrase.
list_message = my_word.split()
to_be_test = {"i am":"jestem","you are":"jestes",
    "he is":"on jest","she is":"ona jest","it is":"to jest","we are":"jestesmy",
    "youu are": "jestescie", "they are":"sa"}

variable = ""
for i in range (0,2):
    variable += f"{list_message[i]} "

for i in range (0,len(to_be_test)):
    if variable == to_be_test [i]:"""

#\