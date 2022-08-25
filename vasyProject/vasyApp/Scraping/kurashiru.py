import requests
from bs4 import BeautifulSoup
import time

URL_PATTERN = "https://www.kurashiru.com"

html_doc = requests.get("https://www.kurashiru.com/search?query=%E3%81%98%E3%82%83%E3%81%8C%E3%81%84%E3%82%82").text
soup = BeautifulSoup(html_doc, 'html.parser')

# imgタグのalt値からタイトルも取得
titles_images = soup.select("html > body > div > section > div > div > div > div > div > ul > li > div > a > div")
links = soup.select("html > body > div > section > div > div > div > div > div > ul > li > div")

i = 1
for (title_image, link) in zip(titles_images, links):
    try:
        print("========================")
        print(str(i) + ".")
        
        print(title_image.img['alt'])
        print(title_image.img['src'])
        print(URL_PATTERN + link.a['href'])
        print("========================")
        i = i + 1
        time.sleep(1)

        
    except Exception as e:
        print(e)
        continue