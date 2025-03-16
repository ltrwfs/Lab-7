import tkinter as tk
import requests
from urllib.request import urlopen, Request
from PIL import ImageTk, Image
import json
import io


def close():
    window.destroy()


def get_picture():
    URL = 'https://randomfox.ca/floof/'
    response = requests.get(URL)
    image_link = json.loads(response.text)['image']
    req = Request(image_link, headers = {"User-Agent": "Mozilla/5.0"})
    with urlopen(req) as u:
        raw_data = u.read()
    image = Image.open(io.BytesIO(raw_data))
    picture = ImageTk.PhotoImage(image)
    label.configure(image=picture)
    label.image = picture
    

window = tk.Tk()
window.title('Random Fox Picture')
window.geometry('800x600')
window.resizable(True, True)

frame = tk.Frame(window)
frame.place(relx=0.5, rely=0.5, anchor='center')

URL = 'https://randomfox.ca/floof/'
response = requests.get(URL)
image_link = json.loads(response.text)['image']
req = Request(image_link, headers = {"User-Agent": "Mozilla/5.0"})
with urlopen(req) as u:
    raw_data = u.read()
image = Image.open(io.BytesIO(raw_data))
picture = ImageTk.PhotoImage(image)
label = tk.Label(frame, image=picture)
label.pack(anchor='center', padx=10, pady=10)

btn_exit = tk.Button(window, text='Close', command=close)
btn_exit.pack(anchor='ne', padx=10, pady=10)
btn_gen2 = tk.Button(window, text='Change Picture', command=get_picture)
btn_gen2.pack(anchor='ne', padx=10, pady=10)

window.mainloop()