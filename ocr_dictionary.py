import pytesseract
import pandas as pd

dictionary = pd.read_csv('english_dictionary.csv')
dictionary = dictionary.loc[:, ~dictionary.columns.str.contains('^Unnamed')]


def get_word_meaning(input_word):
    return dictionary.loc[dictionary['word'] == input_word].meaning.iloc[0]


def get_word_type(input_word):
    return dictionary.loc[dictionary['word'] == input_word].wtype.iloc[0]


result = pytesseract.image_to_string('C:/Users/karthik/Desktop/CSV-Format-English-Dictionary/resources/OCR/development.png')
print("RESULT FROM PY-TESSERACT: {}".format(result))
word = result.split("\n")[0].capitalize()
word = ''.join(e for e in word if e.isalnum())
print("WORD: {}".format(word))

meaning = get_word_meaning(word)
meaning = meaning.replace(";", "\n")
type = get_word_type(word)

print("MEANING:\n {}".format(meaning))
print("WORD TYPE: {}".format(type))
