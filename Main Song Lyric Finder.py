from urllib.request import Request, urlopen
import requests
import bs4 as bs
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

req = Request('https://genius.com/songs/'+Song_Number, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

soup = bs.BeautifulSoup(webpage,'lxml')
for div in soup.find_all('div', class_='lyrics'):
    print(div.text)