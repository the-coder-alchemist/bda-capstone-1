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

def get_video_metadata(url):

    ydl_options = {
        "quiet": True,           
        "skip_download": True,  
    }

    with yt_dlp.YoutubeDL(ydl_options) as ydl:
        try:
            # Extract video information without downloading
            info = ydl.extract_info(url, download=False)
            
            # Create metadata dictionary
            metadata = {
                "title": info.get("title", "Unknown Title"),
                "duration": info.get("duration", 0),
                "uploader": info.get("uploader", "Unknown Uploader"),
                "view_count": info.get("view_count", 0),
                "ext": info.get("ext", "mp4"),
                "url": url
            }
            return metadata
            
        except Exception as e:
            print(f"Error extracting metadata for {url}: {e}")
            # Return a fallback dictionary if extraction fails
            return {
                "title": "Error: Could not extract",
                "duration": 0,
                "uploader": "Unknown",
                "view_count": 0,
                "ext": "unknown",
                "url": url
            }            