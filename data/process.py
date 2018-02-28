import os, sys

from downsub_scraper import download_transcript
from scrape_metadata import get_video_data

vloggers = {}

for filename in os.listdir("retrieved_links"):
    if filename != ".DS_Store":

        filename = filename[:filename.index(".txt")]

        with open("retrieved_links/" + filename) as f:
            links = f.readlines()

            vloggers[filename] = []

            for elem in links:
                if elem[24:29] == "watch":
                    vloggers[filename].append(elem.replace("\n", ""))

for vlogger, vlogs in vloggers.items():
    total = len(vlogs)
    all = 0
    count = 0

    for vlog in vlogs:
        all += 1
        print(vlogger + ": " + str(all) + " of " + str(total))

        try:
            count += 1
            download_transcript(vlogger, count, vlog)
            view_count, published = get_video_data(vlog)

            with open("overview.txt", "a") as f:
                f.write(vlogger + "," + str(count) + "," + vlog + "," + view_count + "," + published + "\n")
        except:
            print("Video " + vlog + " from " + vlogger + " not supported!")

    print("Total Score for " + vlogger + ": " + str(count))
