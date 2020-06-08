import requests
import bs4
import urllib
import zipfile
import glob
import os
import app

def create_zip(username):

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
        # get name of clip
        index = link.rfind("/")
        clip_name = link[index + 1:]
        # go to clip page to get download link
        page = requests.get(link)
        n = str(page.content, 'utf-8')
        index = n.find("720.mp4")
        index_end = index
        while n[index] != '\"':
            index -= 1
        video_link = "https:" + n[index + 1:index_end+7]
        links.append((video_link, clip_name))

    # remove duplicate links
    links = list(set(links))

    # different video names, download videos
    video_increment = 0
    for link in links:
        app.handle_message("testie")
        try:
            urllib.request.urlretrieve(link[0], link[1] + ".mp4")
            video_increment += 1
        except:
            print("not a video link")

    # create zip file
    zipObj = zipfile.ZipFile("static/" + username + "_PlaysTVClips.zip", "w")
    
    # Add multiple files to the zip
    for i in range(0, video_increment):
        try:
            zipObj.write(links[i][1] + ".mp4")
        except:
            print("can't find video to add to zip")

    # close the Zip File
    zipObj.close()

    # remove video files
    for video in glob.glob("*.mp4"):
        try:
            os.remove(video)
        except:
            print("can't find video to delete")