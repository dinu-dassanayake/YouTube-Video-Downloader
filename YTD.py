from pytube.cli import on_progress
from pytube import YouTube
import os

video_link = input("Paste your video link: ")

try:

    yt = YouTube(video_link, on_progress_callback=on_progress)
    yt.streams\
        .filter(file_extension='mp4')\
        .get_highest_resolution()\
        .download()

except EOFError as err:
    print(err)

else:
    print("Download is complete successfully")
