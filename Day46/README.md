# Billboard → YouTube Playlist Automation  
A Python automation tool that scrapes the Billboard Hot 100 for any date and automatically generates a fully populated YouTube playlist using the YouTube Data API.

---

## Project Structure

```
project-folder/
│
├── main.py                               # Main automation script
├── client_secret.json                    # Google OAuth credentials (NOT committed)
├── .gitignore                            # Ensures secrets stay private
├── scrapped-billboard-songs-YYYY-MM-DD/  # Optional saved output
└── README.md                             # Project documentation
```

---

## Overview

This project automates the entire workflow of turning a Billboard Hot 100 chart into a YouTube playlist:

1. Prompt the user for a date  
2. Scrape the Billboard Hot 100 for that date  
3. Search YouTube for each song  
4. Create a YouTube playlist  
5. Add all found videos to the playlist  

The original project used **Spotify**, but due to API restrictions and OAuth complexity, this version uses **YouTube**, which provides a more flexible and accessible API for playlist creation.

---

## Skills Demonstrated

- Web scraping with **BeautifulSoup**
- HTTP requests with custom headers
- OAuth 2.0 authentication using **Google Auth**
- YouTube Data API v3 integration
- Error handling and quota management
- Secure credential handling
- Real‑world automation and API orchestration

---

## Google Authentication Setup

### 1. Create a Google Cloud Project  
Visit: `https://console.cloud.google.com`  
Create a new project (e.g., *Billboard YouTube Playlist*).

### 2. Enable the YouTube Data API v3  
- Go to **APIs & Services → Library**  
- Search for **YouTube Data API v3**  
- Enable it  

### 3. Configure OAuth Consent Screen  
- User type: **External**  
- App name: anything you like  
- Add your email under **Test Users**  
  (Required because the app is in Testing mode)

### 4. Create OAuth Credentials  
- Go to **Credentials → Create Credentials → OAuth Client ID**  
- Application type: **Desktop App**  
- Download the JSON file  
- Rename it to `client_secret.json`  
- Place it in your project folder  

### 5. Add `client_secret.json` to `.gitignore`

```
client_secret.json
```

### Why this file must be hidden  
It contains sensitive information:

- `client_id`  
- `client_secret`  
- redirect URIs  
- OAuth endpoints  

Anyone with this file could impersonate your app.  
Therefore, it must **never** be committed to GitHub.

---

## How OAuth Works in This Project

1. The script loads `client_secret.json`  
2. A local server starts on port 8888  
3. Your browser opens a Google login page  
4. You grant permission  
5. Google returns an access token  
6. The script uses that token to call the YouTube API  

Once authenticated, the script can:

- search YouTube  
- create playlists  
- add videos  

---

## Scraping Billboard

The script scrapes the Billboard Hot 100 using:

```python
soup.select("li.o-chart-results-list__item h3")
```

Each `<h3>` contains a song title.  
The titles are cleaned and stored in a Python list.

---

## YouTube Search

Each song is searched using:

```python
youtube.search().list(
    part="snippet",
    q=query,
    type="video",
    maxResults=1
)
```

The script extracts the **videoId** of the top result.

---

## Playlist Creation

A playlist is created using:

```python
youtube.playlists().insert(...)
```

The playlist is named:

```
Billboard Hot 100 – YYYY-MM-DD
```

---

## Adding Songs to the Playlist

Each video is added using:

```python
youtube.playlistItems().insert(...)
```

One API call per song.

---

## Error Handling & Quota Notes

### YouTube API Quota  
- Each search = **100 units**  
- Daily free quota = **10,000 units**  
- Searching 100 songs = **10,000 units**  

This means the full script can run **once per day**.

### Error handling includes:  
- Returning `None` when no video is found  
- Preventing invalid playlist entries  
- Printing which songs were found/not found  
- Wrapping playlist creation and insertion in clean functions  

---

## Testing Without Using Full Quota

To test safely:

```python
for song in song_names[:5]:
```

This avoids burning all 10,000 units.

---

## Functions Summary

| Function | Purpose |
|---------|---------|
| `searchYoutubeVid()` | Searches YouTube and returns a videoId |
| `search_all_songs()` | Searches YouTube for all scraped songs |
| `createPlaylist()` | Creates a YouTube playlist |
| `addToPlaylist()` | Adds a single video to the playlist |
| `add_all_videos()` | Adds all videos to the playlist |
| Main script | Orchestrates scraping → searching → playlist creation |

---

## .gitignore

 `.gitignore` includes:

```
client_secret.json
__pycache__/
*.pyc
```

This protects our credentials and keeps the repository clean.

---

## Final Result

Running the script produces:

- A brand‑new YouTube playlist  
- Named after the Billboard date  
- Populated with the top 100 songs  
- Fully automated from start to finish  

---

## How It Works (Diagram)

```
┌──────────────────────────────────────────────────────────────┐
│                      USER RUNS SCRIPT                        │
└──────────────────────────────────────────────────────────────┘
                │
                ▼
┌──────────────────────────────────────────────────────────────┐
│         1. Authenticate with Google OAuth (YouTube)           │
│   - Loads client_secret.json                                  │
│   - Opens browser for login                                   │
│   - Returns authenticated YouTube client                      │
└──────────────────────────────────────────────────────────────┘
                │
                ▼
┌──────────────────────────────────────────────────────────────┐
│         2. Ask user for a Billboard date (YYYY-MM-DD)         │
└──────────────────────────────────────────────────────────────┘
                │
                ▼
┌──────────────────────────────────────────────────────────────┐
│         3. Scrape Billboard Hot 100 for that date             │
│   - Requests chart page                                       │
│   - Parses HTML with BeautifulSoup                            │
│   - Extracts top 100 song titles                              │
└──────────────────────────────────────────────────────────────┘
                │
                ▼
┌──────────────────────────────────────────────────────────────┐
│         4. Search YouTube for each song                       │
│   - Uses YouTube Data API search endpoint                     │
│   - Returns top videoId for each title                        │
└──────────────────────────────────────────────────────────────┘
                │
                ▼
┌──────────────────────────────────────────────────────────────┐
│         5. Create a YouTube playlist                          │
│   - Title: Billboard Hot 100 – DATE                           │
│   - Privacy: private                                           │
└──────────────────────────────────────────────────────────────┘
                │
                ▼
┌──────────────────────────────────────────────────────────────┐
│         6. Add each videoId to the playlist                   │
│   - One API call per song                                     │
│   - Prints progress                                            │
└──────────────────────────────────────────────────────────────┘
                │
                ▼
┌──────────────────────────────────────────────────────────────┐
│         7. Playlist is ready on YouTube                       │
└──────────────────────────────────────────────────────────────┘
```