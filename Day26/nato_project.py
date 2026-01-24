# TODO: 1. Create a dictionary in this format:

"""
{'A' : 'Alfa', 'B' : 'Beta', 'C' : 'Charlie', 'D' : 'Delta'}
keys == letters
values == code
"""

import pandas as pd

df = pd.read_csv("NATO-alphabet-data/nato_phonetic_alphabet.csv")
print(df.head())

data = {row.letter:row.code for (index, row) in df.iterrows()}
print(data)

# TODO: 2. Create a list of phonetic code words from a word that user inputs
user_input = input("Enter a word: ").upper()
data_list = [data[letter] for letter in user_input]
print(data_list)