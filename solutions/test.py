import yt_dlp

urls = [
    "https://www.youtube.com/watch?v=jNQXAC9IVRw",
]

ydl_options = {
    "quiet": True,
    "skip_download": True,
}

with yt_dlp.YoutubeDL(ydl_options) as ydl:
    for url in urls:
        info = ydl.extract_info(url, download=False)

        print("Title:", info.get("title"))
        print("Duration:", info.get("duration"))
        print("Uploader:", info.get("uploader"))
        print("Views:", info.get("view_count"))
        print("Extension:", info.get("ext"))
        print("URL:", url)