import spotify_token as st

data = st.start_session("sp_dc","sp_key")
access_token = data[0]
expiration_date = data[1]

import requests

Current_Song = "https://api.spotify.com/v1/me/player/currently-playing"
headers = {
    "Authorization": "Bearer " + str(access_token)
}

res = requests.get(url=Current_Song, headers=headers)
try:
    Result = res.json()
except Exception:
    Result = "No Recently Song Played"

item = Result["item"]
album = item["album"]
# _______________Song Url_______________________ # ?
external_urls = item["external_urls"]
song_url = external_urls["spotify"]
# _______________Music Cover_______________________ #
images = album["images"]
images_list = [ sub['url'] for sub in images ]
image = images_list[0]
# _______________Artist Name_______________________ #?
artists= album["artists"]
artist_name_list = [ sub['name'] for sub in artists ]
artist_name = ' '.join([str(elem) for elem in artist_name_list])
# _______________Song Name_______________________ #?
song_name= item["name"]
# __________________Is Playing____________________ #?
is_playing = Result["is_playing"]

print(
"Song Name"+":"+song_name+"\n",
"Artist Name"+":"+artist_name+"\n",
"Song Url"+":"+song_url+"\n",
"Song Cover"+":"+image+"\n",
"Is Playing"+":"+str(is_playing)+"\n")