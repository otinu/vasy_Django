import requests
from bs4 import BeautifulSoup
import json

"""
URL_PATTERN = "https://cookpad.com/"

html_doc = requests.get("https://cookpad.com/search/%E3%81%98%E3%82%83%E3%81%8C%E3%81%84%E3%82%82").text
soup = BeautifulSoup(html_doc, 'html.parser')
titles = soup.select("html > body > div > div > div > div > div > div > section > main > section > ul > li > div > div > div > h2")
images = soup.select("html >body >div >div >div >div >div >div >section >main >section >ul >li")

posted_data = {}
count = 0
for (title, image) in zip(titles, images):
    try:
        title = title.a.text
        link = image.a['href']
        image = image.img['src']

        if title is not None and link is not None and image is not None:
            add_data = {
                "title": title,
                "link": URL_PATTERN + link,
                "image": image, 
            }
            posted_data[count] = add_data
            count += 1
        else:
            raise(Exception)
    except Exception as e:
        continue

print(json.dumps(posted_data))

"""

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
            link = title_image.img['src']
            image = title_image.img['src']

            if title is not None and link is not None and image is not None:
                add_data = {
                    "title": title,
                    "link": URL_PATTERN + link,
                    "image": image, 
                }
                posted_data[count] = add_data
                count += 1
            else:
                raise(Exception)
        except Exception as e:
            continue

    return(json.dumps(posted_data))