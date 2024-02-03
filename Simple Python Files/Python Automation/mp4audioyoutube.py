import os
import requests
import shutil
from pytube import YouTube

def download_youtube_mp3(youtube_url, output_file):
    # Download YouTube video as mp3 using the ffmpeg option
    yt = YouTube(youtube_url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_stream.download(output_file)

def main():
    # Get YouTube URL from user input
    youtube_url = input("Enter the YouTube URL: ")

    # Generate output file name from the video title
    yt = YouTube(youtube_url)
    output_file = f"{yt.title}.mp3"

    # Download YouTube video as mp3
    download_youtube_mp3(youtube_url, output_file)
    print(f"Downloaded and converted to MP3: {output_file}")

if __name__ == "__main__":
    main()
