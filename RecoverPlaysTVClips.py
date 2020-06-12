import requests
import bs4
import urllib
import zipfile
import glob
import os
import app
import shutil

def create_zip(username, sid):
    app.handle_message(str(0)  + "%", sid)

    # plays.tv profile link
    user_profile_page_url = "https://web.archive.org/web/20191210043532/https://plays.tv/u/"
    user_profile_page_url += username
    page = requests.get(user_profile_page_url)
    soup = bs4.BeautifulSoup(page.text, 'html.parser')
    clip_link_list = soup.findAll(class_='thumb-link')
    links = []
    path = "static/"+ sid + "/"

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

    # create directory for each client
    os.mkdir("static/"+ sid)

    # different video names, download videos
    video_increment = 0
    length = len(links)
    for link in links:
        app.handle_message(str(int((video_increment/length) * 100))  + "%", sid)
        try:
            urllib.request.urlretrieve(link[0], path + link[1] + ".mp4")
            video_increment += 1
        except:
            print("not a video link")

    # create zip file
    app.handle_message("Download Complete", sid)
    shutil.make_archive(base_name="static/" + username + "_PlaysTVClips", format="zip", root_dir="static/", base_dir=sid);

    # delete all mp4s in client dir
    for video in glob.glob(path + "*"):
        try:
            os.remove(video)
        except:
            print("can't find video to delete")

    # removes client dir
    os.removedirs(path)
    
def delete_zip(username):
    myfile = "static/" + username + "_PlaysTVClips.zip"
    if os.path.isfile(myfile):
        os.remove(myfile)