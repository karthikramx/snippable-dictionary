"""
PyDictionary Package to get wordmeanings
Q to exit from the loop
"""

from PyDictionary import PyDictionary

dictionary = PyDictionary()

while True:
    word = raw_input("Enter word for meaning:")
    if str(word) != "Q":
        print(dictionary.meaning(word))
    else:
        break

print("Bye!")
