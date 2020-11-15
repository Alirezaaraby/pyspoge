import requests

Current_Song = "https://api.genius.com/search?q=Song_Name%Artist_Name"
headers = {
    "Authorization": "Bearer " + "Genius_Token"
}
req = requests.get(url=Current_Song, headers=headers).json()
for hit in req['response']['hits']:
    remote_song_info = hit
    break
Song_Number=None
Song_Number= remote_song_info['result']['api_path']
print(Song_Number)