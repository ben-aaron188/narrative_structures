# load dependencies
from __future__ import division
import requests
import sys
import os
from bs4 import BeautifulSoup
import re


def get_video_data(url):
    html = requests.get(url).text

    view_count_start = html.index("watch-view-count") + 18
    view_count_end = html.index("Aufrufe</div>") - 1
    # likes = html.index("likes")
    # dislikes = html.index("dislikes")
    published = html.index("Published") + 20
    # title = html.index("title")
    # comment_count = html.index("count-text")

    view_count = html[view_count_start:view_count_end]
    # print(html[likes - 100:likes + 100])
    # print(html[dislikes - 100:dislikes + 100])
    date_published = html[published:published + 10]
    # print(html[title - 100:title + 100])
    # print(html[comment_count - 100:comment_count + 100])

    return view_count, date_published
