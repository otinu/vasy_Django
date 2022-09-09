import requests
from bs4 import BeautifulSoup

def Allread():
    keywords = {"potato": "%E3%81%98%E3%82%83%E3%81%8C%E3%81%84%E3%82%82",
                "tomato": "%E3%83%88%E3%83%9E%E3%83%88",
                "japanese_nasu": "%E3%83%8A%E3%82%B9"}

    potato_datas = scraping(keywords["potato"])
    tomato_datas = scraping(keywords["tomato"])
    japanese_nasu_datas = scraping(keywords["japanese_nasu"])

    return potato_datas, tomato_datas, japanese_nasu_datas



def scraping(keyword):
    URL_PATTERN = "https://cookpad.com/"

    html_doc = requests.get("https://cookpad.com/search/" + keyword).text
    soup = BeautifulSoup(html_doc, 'html.parser')
    titles = soup.select("html > body > div > div > div > div > div > div > section > main > section > ul > li > div > div > div > h2")
    links_images = soup.select("html >body >div >div >div >div >div >div >section >main >section >ul >li")

    posted_datas = {}
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
                    "count": count
                }
                posted_datas[count] = add_data
                count += 1
            else:
                raise(Exception)
        except Exception as e:
            continue

    return posted_datas
