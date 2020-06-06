import requests
import bs4
import urllib
import zipfile
import glob
import os

# input username
username = "bluepancake69"

# plays.tv profile link
user_profile_page_url = "https://web.archive.org/web/20191210043532/https://plays.tv/u/"
user_profile_page_url += username
page = requests.get(user_profile_page_url)
soup = bs4.BeautifulSoup(page.text, 'html.parser')
clip_link_list = soup.findAll(class_='thumb-link')
links = []

for elem in clip_link_list:
    # link of clip
    link = "https://web.archive.org" + elem.get("href")

    # get video link for download of clip
    index = link.find("?")
    link = link[:index]
    page = requests.get(link)
    n = str(page.content, 'utf-8')
    index = n.find("720.mp4")
    index_end = index
    while n[index] != '\"':
        index -= 1
    video_link = "https:" + n[index + 1:index_end+7]
    links.append(video_link)

# remove duplicate links
links = list(set(links))

# different video names
video_increment = 1
for link in links:
    try:
        urllib.request.urlretrieve(link, "clip" + str(video_increment) + ".mp4")
        video_increment += 1
    except:
        print("not a video link")

# create zip file
zipObj = zipfile.ZipFile('PlaysTVClips.zip', 'w')
 
# Add multiple files to the zip

for i in range(1, video_increment):
    zipObj.write("clip" + str(i) + ".mp4")

# close the Zip File
zipObj.close()

# remove video files
for video in glob.glob("*.mp4"):
    os.remove(video)