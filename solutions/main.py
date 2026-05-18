from library import download_video
from library import read_video_urls, time_counter


if __name__ == "__main__":
    video_url = read_video_urls("data/video_urls.csv")
    for url in video_url:
        download_video(url)
        time_counter()