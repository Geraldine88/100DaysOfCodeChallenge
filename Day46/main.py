import requests
from bs4 import BeautifulSoup
import time

# ****************************************************************************************
# GOOGLE AUTHENTICATION
# ****************************************************************************************
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/youtube"]


def authenticate_youtube():
    """Handles OAuth flow and returns an authenticated YouTube client."""
    flow = InstalledAppFlow.from_client_secrets_file(
        "client_secret.json", SCOPES
    )
    cred = flow.run_local_server(port=8888)
    youtube = build("youtube", "v3", credentials=cred)
    print("Authentication Successful!")
    return youtube


# ****************************************************************************************
# SCRAPE BILLBOARD
# ****************************************************************************************
def scrape_billboard(date):
    """Scrapes Billboard Hot 100 for the given date and returns a list of song titles."""

    # Creating/ Building the Billboard URL
    url = "https://www.billboard.com/charts/hot-100/" + date

    # Send a request with User-Agent
    # TODO: 3. Include a header when you make your request to billboard.com. See HTTP headers
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"
    }

    response = requests.get(url=url, headers=headers)

    # Parsing the HTML with Beautiful Soup
    soup = BeautifulSoup(response.text, "html.parser")

    # Selecting song titles, targetting <h3>
    music_names_tags = soup.select("li.o-chart-results-list__item h3")

    song_names = []
    # Extract and clean the text
    for tag in music_names_tags:
        title = tag.getText().strip()
        song_names.append(title)

    return song_names


# ****************************************************************************************
# ADDING YOUTUBE SEARCH FUNCTIONS
# ****************************************************************************************
def searchYoutubeVid(youtube, query):
    # sending a 'search' request
    request = youtube.search().list(
        part="snippet",
        q=query,
        type="video",
        maxResults=1,  # Getting the top video as per the search
    )
    response = request.execute()

    items = response.get("items", [])
    # returning the video id, otherwise None if nothing is found
    if not items:
        return None  # This to also prevent corruption of playlist in lieu of 'Video not found'
    else:
        return items[0]["id"]["videoId"]


def search_all_songs(youtube, song_names):
    """Searches YouTube for each song and returns a list of video IDs."""
    video_ids = []
    print("\n Searching YouTube for each song... \n")

    for song in song_names:
        video_id = searchYoutubeVid(youtube, song)
        if video_id:
            video_ids.append(video_id)  # collect video ids
            print(f"Found: {song} - {video_id}")
        else:
            print(f"Not found: {song} - {video_id}")

        # Prevent rate-limit spikes
        time.sleep(0.3)

    return video_ids


# ****************************************************************************************
# CREATING A PLAYLIST
# ****************************************************************************************
def createPlaylist(youtube, date):
    request = youtube.playlists().insert(
        part="snippet, status",
        body={
            "snippet": {
                "title": f"Billboard Hot 100 - {date}",
                "description": f"Top 100 songs from Billboard Hot 100 on {date}",  # name playlist using date
            },
            "status": {
                "privacyStatus": "private",
            },
        },
    )
    response = request.execute()
    return response["id"]


# ****************************************************************************************
# ADDING SONGS TO PLAYLIST
# ****************************************************************************************
def addToPlaylist(youtube, playlistId, video_id):
    request = youtube.playlistItems().insert(
        part="snippet",
        body={
            "snippet": {
                "playlistId": playlistId,
                "resourceId": {
                    "kind": "youtube#video",
                    "videoId": video_id,  # inserts just 1 video into the playlist
                },
            }
        },
    )
    request.execute()


def add_all_videos(youtube, playlistId, video_ids):
    print("\n Adding songs to the playlist... \n")
    for v in video_ids:
        addToPlaylist(youtube, playlistId, v)
        print(f"Added video: {v}")
        time.sleep(0.2)


# ****************************************************************************************
# MAIN EXECUTION FLOW
# ****************************************************************************************
if __name__ == "__main__":

    youtube = authenticate_youtube()

    # Ask the user for a date
    year_preference = input(
        "Which year would you like to travel to? Type the date in this format YYYY-MM-DD: \n"
    )

    # Scrape Billboard
    song_names = scrape_billboard(year_preference)
    print(song_names)

    # Search YouTube
    video_ids = search_all_songs(youtube, song_names)

    # Create playlist
    print("\n Creating YouTube playlist... \n")
    playlistId = createPlaylist(youtube, year_preference)
    print(f"Playlist created! ID: {playlistId}")

    # Add songs
    add_all_videos(youtube, playlistId, video_ids)