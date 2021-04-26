# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

english_dictionary = pd.read_csv("english_dictionary.csv")


english_dictionary["useage"] = np.nan
english_dictionary["etymology"] = np.nan
english_dictionary["synonymns"] = np.nan
english_dictionary["antonyms"] = np.nan

english_dictionary.to_csv("english_dictionary_extended.csv")


