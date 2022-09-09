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
    URL_PATTERN = "https://www.kurashiru.com"

    html_doc = requests.get("https://www.kurashiru.com/search?query=" + keyword).text
    soup = BeautifulSoup(html_doc, 'html.parser')

    # imgタグのalt値からタイトルも取得
    titles_images = soup.select("html > body > div > section > div > div > div > div > div > ul > li > div > a > div > div > noscript")
    links = soup.select("html > body > div > section > div > div > div > div > div > ul > li > div")

    datas = {}
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
                datas[count] = add_data
                count += 1
            else:
                raise(Exception)
        except Exception as e:
            continue

    return datas