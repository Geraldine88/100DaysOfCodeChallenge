# Day 25: Working with CSV Data and Pandas

A collection of exercises learning to read, analyze, and manipulate 
CSV data using Python's pandas library, culminating in a US States guessing game.

## What Was Covered

### Reading CSV Files
- Reading with built-in `csv` module
- Reading with `pandas` (easier and more powerful)
- Introduction to Data Analysis

### Pandas Basics
- Loading CSV files: `pd.read_csv()`
- Accessing columns: `data['column']` or `data.column`
- Converting to lists: `.tolist()`
- Converting to dictionaries: `.to_dict()`

### Data Analysis
- Statistical operations: `.mean()`, `.max()`, `.min()`, `.sum()`
- Filtering data: `data[data.column == value]`
- Working with Series and accessing specific values

### Creating & Exporting Data
- Creating DataFrames from dictionaries
- Exporting to CSV: `.to_csv()`
- Using `index=False` to avoid extra index column

## Projects Included

1. **weather_data.csv** - Basic temperature analysis and filtering
2. **squirrel_count.py** - Analyzing Central Park squirrel census data by fur color
3. **guess_us_state.py** - Interactive game using turtle graphics and pandas

## Main Project: US States Guessing Game

Guess all 50 US states and see them appear on a map!

### Features
- Interactive GUI with turtle graphics
- Score tracking (X/50)
- Saves missed states to learn later
- Prevents duplicate guesses
