#Creates a GUI (Does not work as intended)
import customtkinter as ctk
from tkinter import ttk
from pytube import YouTube
import os

def download_video():
    url = entry_url.get()
    resolution = resolution_var.get()

    progress_label.pack(pady=("10p", "5p"))
    progress_bar.pack(pady=("10p", "5p"))
    status_label.pack(pady=("10p", "5p"))

    try:
        yt = YouTube(url)
        stream = yt.streams.filter(res=resolution).first()
        os.path.join("downloads", f"{yt.title}.mp4")
        stream.download(output_path="downloads", filename=yt.title)
        
        status_label.configure(text=f"Downloaded", text_color="white", fg_color="green")

    except Exception as e:
        status_label.configure(text=f"Error {str(e)}", text_color="white", fg_color="red")

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_completed = bytes_downloaded / total_size * 100

    progress_label.configure(text=str(int(percentage_completed)) + "%")
    progress_label.update()

#Root window
root = ctk.CTk()
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

#Title of Window
root.title("YouTube Video Downloader")

#Sets the min and max width and the height
root.geometry("720x480")
root.minsize(720, 480)
root.maxsize(1080, 720)

#Create a frame to hold content
content_frame = ctk.CTkFrame(root)
content_frame.pack(fill=ctk.BOTH, expand=True, padx=10, pady=10)

#Creates a label and entry widget for video url
url_label = ctk.CTkLabel(content_frame, text="YouTube link here:")
entry_url = ctk.CTkEntry(content_frame, width=400, height=40)
url_label.pack(pady=("10p", "5p"))
entry_url.pack(pady=("10p", "5p"))

#Creates a download button
download_button = ctk.CTkButton(content_frame, text="Download", command=download_video)
download_button.pack(pady=("10p", "5p"))

#Creates Resolution Box
resolutions = ["720p", "360p", "240p"]
resolution_var = ctk.StringVar()
resolution_combobox = ttk.Combobox(content_frame, values=resolutions, textvariable=resolution_var)
resolution_combobox.pack(pady=("10p", "5p"))
resolution_combobox.set("720p")

#Creates a label and progress bar to display download progress
progress_label = ctk.CTkLabel(content_frame, text="0%")

progress_bar = ctk.CTkProgressBar(content_frame, width = 400)
progress_bar.set(0)

#Status label
status_label = ctk.CTkLabel(content_frame, text="")

#Starts the app
root.mainloop()