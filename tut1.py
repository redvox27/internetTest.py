import urllib.request
import requests
import urllib.parse
from bs4 import BeautifulSoup
import webbrowser
import time
import re

tut_url = "https://www.youtube.com/watch?v=XjNm9bazxn8"

def spider(max_pages):
    page = 0

    while page < max_pages:
        url = "https://thepiratebay.org/search/the%20walking%20dead/0/" + str(page)
        headers = {}
        headers["User-Agent"] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"

        req = requests.get(url,headers=headers)

        plain_text = req.text

        soup = BeautifulSoup(plain_text)

        for link in soup.findAll("a",{"class" : "detLink"}) :
            href = "https://thepiratebay.org" + link.get("href")
            title = link.string


            #print(href)
            if "S07" in title:
                get_magnet_link(href)
        page +=1



def get_magnet_link(url):
    headers = {}
    headers["User-Agent"] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"

    req = requests.get(url,headers=headers)
    plain_text = req.text
    soup = BeautifulSoup(plain_text)
    link_list = []
    i = 1


    for magnet in soup.findAll("a",{"title":"Get this torrent"}):
        link = magnet.get("href")

        if link not in link_list:
            link_list.append(link)



    print(link_list)
    for link in link_list:
        webbrowser.open(link)
        time.sleep(10)






spider(1)