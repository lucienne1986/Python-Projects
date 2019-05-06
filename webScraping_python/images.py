from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
import os

def startSearch():
    search = input("Enter search term: ")
    params = {"q": search}
    dir_name= search.replace(" ","_").lower()

    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)

    r = requests.get("http://www.bing.com/images/search", params=params)

    soup = BeautifulSoup(r.text, "html.parser")
    links = soup.findAll("a", {"class": "thumb"})

    for item in links:
        try:
            img_obj = requests.get(item.attrs["href"])
            print("getting", item.attrs["href"])
            title = item.attrs["href"].split("/")[-1]
            try:
                img = Image.open(BytesIO(img_obj.content))
                img.save("./" + dir_name + "/"+title, img.format)
            except:
                print("could not save images")
        except:
            print("could not request image")

    startSearch()

startSearch()

