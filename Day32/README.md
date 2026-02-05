# Day 32: Birthday Wisher Email Project

## Project Structure

```
Day32/
├── Birthday Wisher (Day 32)/
│   ├── main.py              # Practice: datetime & smtplib basics
│   └── quotes.txt           # Motivational quotes
│
└── birthday-wisher-hard-start/
    ├── letter_templates/    # Folder with 4 birthday letter templates (.txt)
    ├── birthdays.csv        # Contact list: names, emails, birth dates
    └── main.py              # Main birthday wisher automation
```

## What It Does

**Automated Birthday Email Sender** that:
1. Checks if today matches anyone's birthday in `birthdays.csv`
2. Randomly selects a birthday letter template
3. Personalizes it with the person's name
4. Sends the customized email automatically

## Technologies Used

- **smtplib** - Send emails via SMTP
- **datetime** - Check current date and compare with birthdays
- **pandas** - Read and parse CSV data
- **random** - Select random letter templates
- **os** - Navigate letter template files

## Setup Requirements

### 1. Update `birthdays.csv`
Add your contacts with format:
```
name,email,year,month,day
John,john@email.com,1990,2,3
```

### 2. Create Letter Templates
Add `.txt` files in `letter_templates/` folder with `[NAME]` placeholder:
```
Dear [NAME],

Happy Birthday! 🎂

Wishing you an amazing day!
```

### 3. Gmail App Password
- Enable 2-Factor Authentication in Google Account
- Generate App Password (Security → App Passwords)
- Use the 16-character password in `gmail_password` variable

## ▶️ How to Run

```bash
python main.py
```

The script will:
- ✅ Check today's date against birthdays
- ✅ Send personalized emails if matches found
- ✅ Print confirmation or "No birthdays today"

## Security Note

Never commit real credentials! Use environment variables:
```python
import os
my_gmail = os.environ.get('MY_EMAIL')
gmail_password = os.environ.get('MY_PASSWORD')
```

---

**Day 32 Complete!** 🎉 Automated birthday wishes via email.