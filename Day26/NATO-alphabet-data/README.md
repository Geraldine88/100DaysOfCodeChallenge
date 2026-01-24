# Day 26: NATO Phonetic Alphabet Converter

Convert any word into NATO phonetic alphabet code words using Python list and dictionary comprehension and pandas.

## What Was Covered

### Dictionary Comprehension
- Creating dictionaries from lists: `{key:value for item in list}`
- Filtering with conditions: `{k:v for k,v in dict.items() if test}`
- Looping through dictionaries: `.items()`

### Pandas DataFrame Iteration
- Reading CSV files
- Iterating through rows: `.iterrows()`
- Accessing row data by column name

## Main Project: NATO Alphabet Converter

Enter a word and get the NATO phonetic code for each letter.

### Example
```
Input: HELLO
Output: ['Hotel', 'Echo', 'Lima', 'Lima', 'Oscar']
```

### How It Works
1. Loads NATO alphabet from CSV
2. Creates dictionary using comprehension: `{row.letter:row.code}`
3. Converts user input to phonetic codes using list comprehension

### Files Needed
- `nato_phonetic_alphabet.csv` (with columns: letter, code)
