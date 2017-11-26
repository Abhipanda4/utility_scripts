#! /usr/bin/python2.7

from bs4 import BeautifulSoup
import requests
import webbrowser

playlist_url = input("Enter the Complete Youtube URL of the Playlist: ")
html = requests.get(playlist_url)
print("Constructing the DOM...........")
soup = BeautifulSoup(html.content, "html5lib")

video_links = soup.find_all("a", class_="pl-video-title-link")

final_links = []
for link in video_links:
    print("Fetching proper link.......")
    l = "https://keepvid.com/?url=" + "https://www.youtube.com" + link['href']
    final_links.append(l)

print("Go to your default browser now.......")
for link in final_links:
    try:
        webbrowser.open(link)
    except:
        print("This link is a pain: ", link)
