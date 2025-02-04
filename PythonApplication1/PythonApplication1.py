import yt_dlp
import tkinter as tk
from tkinter import filedialog

def download_video():
    video_url = url_entry.get()
    ydl_opts = {
        'format': 'bestvideo[height<=720]+bestaudio/best[height<=144]',
        'outtmpl': '%(title)s.%(ext)s',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

root = tk.Tk()
root.title("YouTube Video Downloader")

# Create and grid the widgets
url_label = tk.Label(root, text="Video URL:")
url_label.grid(row=0, column=0, padx=5, pady=5)

url_entry = tk.Entry(root, width=50)
url_entry.grid(row=0, column=1, padx=5, pady=5)

download_button = tk.Button(root, text="Download", command=download_video)
download_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
