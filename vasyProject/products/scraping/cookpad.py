import requests
from bs4 import BeautifulSoup
import json

URL_PATTERN = "https://cookpad.com/"

def read():
    html_doc = requests.get("https://cookpad.com/search/%E3%81%98%E3%82%83%E3%81%8C%E3%81%84%E3%82%82").text
    soup = BeautifulSoup(html_doc, 'html.parser')
    titles = soup.select("html > body > div > div > div > div > div > div > section > main > section > ul > li > div > div > div > h2")
    links_images = soup.select("html >body >div >div >div >div >div >div >section >main >section >ul >li")

    posted_data = {}
    count = 0
    for (title, link_image) in zip(titles, links_images):
        try:
            title = title.a.text
            link = link_image.a['href']
            image = link_image.img['src']

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

    return json.dumps(posted_data)