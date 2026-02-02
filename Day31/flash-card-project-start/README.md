# Day 31: French Flash Card App

I built a flash card app to learn French vocabulary with automatic card flipping and progress tracking.

## What I Learned

### Auto-Flip Timer with window.after()
- I used `window.after(3000, func)` to flip cards after 3 seconds
- I learned to cancel timers with `window.after_cancel()` when clicking to next card
- I passed function references (not calls) to `window.after()`

### Progress Tracking with CSV
- I started with `french_words.csv` containing all 100 words
- When I mark a word as "known" (✓ button), I remove it from the list
- I save remaining words to `to_learn.csv` 
- Next time I run the app, it loads from `to_learn.csv` so I only study words I haven't learned

### Dynamic Canvas Updates
- I changed canvas images with `canvas.itemconfig(image_id, image=new_image)`
- I changed text color with `canvas.itemconfig(text_id, fill="white")`
- I updated multiple canvas elements from the same function

### File Exception Handling
```python
try:
    df = pd.read_csv("data/to_learn.csv")  # Try to load progress
except FileNotFoundError:
    df = pd.read_csv("data/french_words.csv")  # First time, use full list
else:
    french_df = df.to_dict(orient="records")  # Convert to list of dicts
```

## How My App Works

### Card Display Flow
1. App shows a French word on white card (front)
2. After 3 seconds, card automatically flips to green (back) showing English translation
3. I click ✗ to skip to next word OR ✓ to mark as learned

### Progress System
- **✗ (wrong_btn)**: Moves to next random word, keeps current word in study list
- **✓ (right_btn)**: Removes word from list, saves progress, moves to next word
- Words I mark as learned won't appear again


## Files I Need

```
project/
├── main.py
├── data/
│   ├── french_words.csv      (100 French-English pairs)
│   └── to_learn.csv           (auto-created, tracks progress)
└── images/
    ├── card_front.png         (white card)
    ├── card_back.png          (green card)
    ├── right.png              (✓ checkmark)
    └── wrong.png              (✗ cross)
```

## How to Run

```bash
pip install pandas
python main.py
```

## Key Functions I Built

**`random_french()`** - Picks random word, shows French side, starts 3-second timer
**`swap_card()`** - Flips to English side after 3 seconds
**`is_learned()`** - Removes current word from list, saves progress

## What Makes This Smart

- I don't waste time reviewing words I already know
- Progress persists between sessions
- Timer resets when I click to next card (doesn't flip mid-transition)
- First run uses full word list, subsequent runs use `to_learn.csv`

## CSV Format

**french_words.csv / to_learn.csv:**
```csv
French,English
partie,part
histoire,history
chercher,search
```

## Color Scheme
- Background: `#B1DDC6` (light teal)
- Front card: White background, black text
- Back card: Green background, white text

## What I'd Improve

- Add a progress bar showing how many words left
- Add a "reset progress" button to start over
- Show statistics (words learned, accuracy rate)
- Add audio pronunciation
- Support multiple languages

---

**Study Tip**: The 3-second delay gives me time to try recalling the translation before the card flips!