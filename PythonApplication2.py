import yt_dlp
import tkinter as tk
from tkinter import filedialog, messagebox

class YouTubeVideoDownloader:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Video Downloader")
        self.root.geometry("400x150")

        # Create and grid the widgets
        self.url_label = tk.Label(root, text="Video URL:")
        self.url_label.grid(row=0, column=0, padx=5, pady=5)

        self.url_entry = tk.Entry(root, width=50)
        self.url_entry.grid(row=0, column=1, padx=5, pady=5)

        self.format_label = tk.Label(root, text="Format:")
        self.format_label.grid(row=1, column=0, padx=5, pady=5)

        self.format_var = tk.StringVar(root)
        self.format_var.set("bestvideo[height<=720]+bestaudio/best[height<=144]")  # default value
        self.format_option = tk.OptionMenu(root, self.format_var, 
                                            "bestvideo[height<=720]+bestaudio/best[height<=144]", 
                                            "best", 
                                            "worst")
        self.format_option.grid(row=1, column=1, padx=5, pady=5)

        self.download_button = tk.Button(root, text="Download", command=self.download_video)
        self.download_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.save_label = tk.Label(root, text="Save to:")
        self.save_label.grid(row=3, column=0, padx=5, pady=5)

        self.save_entry = tk.Entry(root, width=50)
        self.save_entry.grid(row=3, column=1, padx=5, pady=5)

        self.browse_button = tk.Button(root, text="Browse", command=self.browse_save_location)
        self.browse_button.grid(row=3, column=2, padx=5, pady=5)

    def browse_save_location(self):
        save_location = filedialog.askdirectory()
        self.save_entry.delete(0, tk.END)
        self.save_entry.insert(0, save_location)

    def download_video(self):
        video_url = self.url_entry.get()
        ydl_opts = {
            'format': self.format_var.get(),
            'outtmpl': self.save_entry.get() + '/%(title)s.%(ext)s',
        }
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_url])
            messagebox.showinfo("Success", "Video downloaded successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = YouTubeVideoDownloader(root)
    root.mainloop()
