from urllib.request import Request, urlopen
req = Request('https://genius.com/songs/Song_ID', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
import bs4 as bs

soup = bs.BeautifulSoup(webpage,'lxml')
for div in soup.find_all('div', class_='lyrics'):
    print(div.text)
print("Coded By AlirezaAraby")