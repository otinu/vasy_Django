import requests
from bs4 import BeautifulSoup
import json

def read():

    URL_PATTERN = "https://www.kurashiru.com"


    html_doc = requests.get("https://www.kurashiru.com/search?query=%E3%81%98%E3%82%83%E3%81%8C%E3%81%84%E3%82%82").text
    soup = BeautifulSoup(html_doc, 'html.parser')

    # imgタグのalt値からタイトルも取得
    titles_images = soup.select("html > body > div > section > div > div > div > div > div > ul > li > div > a > div > div > noscript")
    links = soup.select("html > body > div > section > div > div > div > div > div > ul > li > div")

    posted_data = {}
    count = 0
    for (title_image, link) in zip(titles_images, links):
        try:
            title = title_image.img['alt']
            link = URL_PATTERN + link.a['href']
            image = title_image.img['src']

            if title is not None and link is not None and image is not None:
                add_data = {
                    "title": title,
                    "link": link,
                    "image": image, 
                    "count": count
                }
                posted_data[count] = add_data
                count += 1
            else:
                raise(Exception)
        except Exception as e:
            continue

    return posted_data