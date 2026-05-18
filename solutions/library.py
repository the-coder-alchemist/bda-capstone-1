from pathlib import Path
import yt_dlp
import csv
import time 

def download_video(url):

    Path("videos").mkdir(exist_ok=True)

    #url = "https://www.youtube.com/watch?v=jNQXAC9IVRw"

# Save inside videos/ using the video title as the filename
    ydl_options = {
        "outtmpl": "videos/%(title)s.%(ext)s"
    }

    with yt_dlp.YoutubeDL(ydl_options) as ydl:
        ydl.download([url])


def read_video_urls(csv_path):
    listurl = []
    with open(csv_path, newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            #print(row["url"]) 
            listurl.append(row["url"])
        return listurl


def time_counter():
    start = time.perf_counter()

# code to time goes here

    end = time.perf_counter()
    elapsed = end - start
#Use round() to show the time with 2 decimal points:

    serial_time = round(elapsed, 2)
    print(f"Serial execution: {serial_time}")