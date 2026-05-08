# Day 29: Password Manager with JSON & Exception Handling

I upgraded my password manager app from Day 26 by replacing the text file with JSON file handling, a search feature, and proper exception handling.

## What I Learned

### Exception Handling
- I used `try/except/else/finally` blocks to manage errors gracefully
- I caught specific exceptions: `FileNotFoundError`, `KeyError`, `IndexError`, `TypeError`
- I raised my own exceptions using `raise ValueError()` and `raise KeyError`

### JSON File Handling
- I switched from `data.txt` to `data.json` for structured data storage
- I used `json.dump()` to write and `json.load()` to read
- I learned to update existing JSON data without overwriting everything
- I used `indent=4` for readable JSON formatting

### Search Functionality
- I built a search function that looks up saved passwords by website
- I display results using `messagebox.showinfo()`
- I handle cases where the website doesn't exist in the saved data

## How My Password Manager Works

### Save Flow
1. I enter a website, email, and password
2. I click "Add" to save
3. My app checks if `data.json` exists
4. If it doesn't exist, I create it with the new entry
5. If it does exist, I load the data, update it, and write it back
6. I clear the fields after saving

### Search Flow
1. I type a website name in the website field
2. I click "Search"
3. My app reads `data.json` and looks for the website
4. If found, it shows the email and password in a popup
5. If not found, it displays an error message

### Password Generator
- I reused my password generator from Day 5
- It creates a 16-character password (8 letters, 4 symbols, 4 numbers)
- It automatically copies the password to my clipboard using `pyperclip`


## My Exception Handling Pattern
```python
try:
    # Read existing data from data.json
    with open("data.json", "r") as f:
        data = json.load(f)
except FileNotFoundError:
    # File doesn't exist yet, create it
    with open("data.json", "w") as f:
        json.dump(new_dict, f, indent=4)
else:
    # File exists, update and save
    data.update(new_dict)
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)
finally:
    # Always clear the input fields
    web_entry.delete(0, END)
    pwd_entry.delete(0, END)
```

## Files I Need
- `logo.png` - Logo displayed on the canvas
- `personal_brand.png` - Background image
- `data.json` - Auto-created when I save my first password

## How to Run
```bash
pip install pyperclip Pillow
python main.py
```

## What I Changed From Day 5
- Switched from plain text file to JSON for cleaner data storage
- Added a search button to look up saved passwords
- Added input validation with error message boxes
- Added a background image and white content frame for better UI
- Added exception handling to prevent crashes

## What I'd Improve Next
- Hide password input with `show="*"` in the Entry widget
- Add a delete/update password feature
- Add a "show all saved websites" dropdown
- Encrypt stored passwords before saving