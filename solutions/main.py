from library import download_video
from library import read_video_urls
from library import get_video_metadata
import csv 
import time 
from multiprocessing import Pool

if __name__ == "__main__":

    video_url = read_video_urls("data/video_urls.csv")
    """
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
    """

    print("-" * 40)
    print(f"Starting parallel download of {len(video_url)} videos...")

    
    # Start timing for parallel execution
    parallel_start = time.perf_counter()
    

    download_results = []    
    # Use multiprocessing.Pool to download videos in parallel
    with Pool() as pool:
        download_results = pool.map(download_video, video_url)
    
    # End timing for parallel execution
    parallel_end = time.perf_counter()
    parallel_elapsed = parallel_end - parallel_start
    
    # Use round() to show the time with 2 decimal points
    parallel_time = round(parallel_elapsed, 2)
    print(f"Parallel execution: {parallel_time}")    

    print()
    print("-" * 40)
    
    
    successful = []
    failed = []
    
    for result in download_results:
        if result["status"] == "success":
            successful.append(result)
            print(f"SUCCESS: {result['url']}")
        else:
            failed.append(result)
            print(f"FAILED: {result['url']}")
            print(f"Error: {result['error']}")
    print()
    print("-" * 40)
    print(f"Successful downloads: {len(successful)}/{len(video_url)}")
    print(f"Failed downloads: {len(failed)}/{len(video_url)}")
    print()
    print("-" * 40)
     # List to store all metadata
    metadata_rows = []

    for url in video_url:
        
        # Get metadata using the new function
        metadata = get_video_metadata(url)
        metadata_rows.append(metadata)

    
    with open("data/video_metadata.csv", "w", newline="", encoding="utf-8") as file:
        fieldnames = ["title", "duration", "uploader", "view_count", "ext", "url"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        writer.writeheader()
        writer.writerows(metadata_rows)
    
    print(f" Metadata saved to: data/video_metadata.csv")
    print(f" Total videos processed: {len(metadata_rows)}")     


   