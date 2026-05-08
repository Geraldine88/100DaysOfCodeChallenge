# Wedding Invitation Letter Generator

This is a Python script that automatically generates personalized wedding invitation letters for multiple guests. Provide a list of names and a template letter, and get customized invitations for each guest!

## Features

- Bulk letter generation from a single template
- Automatic name replacement in letters
- Individual file creation for each guest
- Clean formatting with whitespace removal

## Project Structure

```
merging/
│
├── input/
│   ├── names/
│   │   └── invites.txt           # List of guest names (one per line)
│   └── letters/
│       └── starting_letter.txt   # Letter template with [name] placeholder
│
├── output/
│   └── ready_to_send/            # Generated personalized letters
│
├── wedding_invite.py                       # Wedding invitation generator
└── README.md
── main.py            # File reading/writing examples and practice
```

## Quick Start

### 1. Setup Folders
Create the folder structure above.

### 2. Add Guest Names
Create `input/names/invites.txt` with one name per line:
For example
```
Alice Johnson
Bob Smith
Charlie Brown
```

### 3. Create Template
Create `input/letters/starting_letter.txt` with `[name]` placeholder:
```
INVITATION TO MY WEDDING

Dear [name],

It is with great joy and honor that I invite you to celebrate with me as I am joined in
Holy Matrimony with Prince Charming.

You have been an integral part of my life and growth process and truly appreciate you
that.

Inline with my motive to express my gratitude, I would also be honored if you graced my
blessed celebration with your esteemed presence at The Royal Palace, Zion Kingdom
777 ST, WEST RIVER SIDE, Heaven.

With great love and regards,

my_name.
```

### 4. Run the Script
```bash
python main.py
```

Find your personalized letters in `output/ready_to_send/`!

## Code Overview

**wedding_invite.py** - Generates personalized invitations:


**main.py** - File handling examples:

## Troubleshooting

- **FileNotFoundError**: Check folder structure matches exactly
- **Names not replacing**: Ensure placeholder is exactly `[name]` with brackets
- **Permission errors**: Create `output/ready_to_send/` folder manually

## Key Python Concepts

- **`with open()`**: Context manager for safe file handling
- **`readlines()`**: Returns list with each line as an item
- **`read()`**: Returns entire file as a single string
- **`strip()`**: Removes whitespace and newlines
- **`replace()`**: Substitutes text
- **File modes**: `"r"` (read), `"w"` (write/overwrite), `"a"` (append)

## Author

Created as part of the 100 Days of Code challenge - Day 24

# 😄 !!! NOTE: THIS IS A WEDDING INVITE FOR FUTURE USE, NOT NOW !!!!
