# -*- coding: utf-8 -*-

import pandas as pd

# deal with index numbers
dictionary = pd.read_csv('english_dictionary.csv')
dictionary = dictionary.loc[:, ~dictionary.columns.str.contains('^Unnamed')]


def get_word_meaning(word):
    print(dictionary['word'] == word)

    return dictionary.loc[dictionary['word'] == word].meaning.iloc[0]


def get_word_type(word):
    return dictionary.loc[dictionary['word'] == word].wtype.iloc[0]


print(get_word_meaning("abetment"))

get_word_type("Abetment")
