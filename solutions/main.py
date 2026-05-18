from library import download_video
from library import read_video_urls
import time 


if __name__ == "__main__":


    video_url = read_video_urls("data/video_urls.csv")

        # Track individual times
    individual_times = []
        
        # Start total timing
    start = time.perf_counter()

    for i,url in enumerate(video_url,1):
        print(f"Downloading video {i}/{len(video_url)}...")
            
            # Time individual download
        video_start = time.perf_counter()
        download_video(url)
        video_end = time.perf_counter()
        video_elapsed = video_end - video_start
        video_time = round(video_elapsed, 2)
        individual_times.append(video_time)
            
        print(f"Video {i} took: {video_time} seconds\n")
        
        # End total timing
    end = time.perf_counter()

    elapsed = end - start
        
        # Use round() to show the time with 2 decimal points
    total_time = round(elapsed, 2)
    print(f"Total execution time: {total_time}")