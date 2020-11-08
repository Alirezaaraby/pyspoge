import io
import webbrowser
import PIL
from PIL import Image
from tkinter import *
from PIL import ImageTk
import requests
import spotify_token as st

data = st.start_session("sp_dc","sp_key")
access_token = data[0]

Current_Song = "https://api.spotify.com/v1/me/player/currently-playing"
headers = {
    "Authorization": "Bearer " + str(access_token)
}

res = requests.get(url=Current_Song, headers=headers)

try:
    Result = res.json()
except Exception:
    Result = "No Recently Song Played"

print(Result)


# json = json.loads(Result)

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

def on_click(event=None):
    webbrowser.open_new(song_url)


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)


        response = requests.get(image)
        image_bytes = io.BytesIO(response.content)

        img = PIL.Image.open(image_bytes)

        render = ImageTk.PhotoImage(img)
        img = Label(self, image=render)
        img.image = render
        img.place(relx=0.5,rely=0.5,anchor='center')
        img.bind('<Button-1>', on_click)

        Label(root, text="Codded By AlirezaArabi").pack()

        Label(root, text="Song Name:"+song_name).place(relx = 0.5,rely = 0.0,anchor ='ne')
        Label(root, text="Artist Name:"+artist_name).place(relx = 0.5,rely = 0.1,anchor ='ne')
        Label(root, text="Is Playing:"+str(is_playing)).place(relx = 0.5,rely = 0.9,anchor ='ne')


root = Tk()
app = Window(root)
root.wm_title("Tkinter window")
root.geometry("500x500")
root.mainloop()