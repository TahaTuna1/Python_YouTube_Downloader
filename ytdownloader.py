import os
from urllib.parse import urlparse
from pytube import YouTube
from pytube.exceptions import RegexMatchError


def is_valid_url(url):
    parts = urlparse(url)
    return bool(parts.scheme and parts.netloc)


def download_video():
    while True:
        link = input("Enter Link:  ")
        if is_valid_url(link):
            try:
                yt = YouTube(link)
                break
            except RegexMatchError:
                print("Not a valid YouTube URL. Please enter a valid YouTube URL.")
        else:
            print("Not a valid URL. Please enter a valid URL.")

    print("Title: ", yt.title)
    print("Available Download Options: ")
    print("___________________________")
    # Getting available video resolutions
    videos = yt.streams.filter(progressive=True)
    video_list = []
    for i in range(len(videos)):
        print(i, '. Resolution ', videos[i].resolution)
        video_list.append(videos[i])

    # Choose resolution
    while True:
        n = input("Enter selected resolution number: ")
        if n.isdigit():
            n = int(n)
            if 0 <= n < len(video_list):
                break
        print("Invalid input. Please enter a number between 0 and ", len(video_list) - 1)

    ys = video_list[n]

    print("Downloading...")
    ys.download(os.path.expanduser('~/Downloads'))
    print("------------------------------------")
    print("-------- Download completed --------")
    print("------------------------------------")


if __name__ == "__main__":
    while True:
        download_video()
