import csv

with open("data/video_urls.csv", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row["title"], row["url"])