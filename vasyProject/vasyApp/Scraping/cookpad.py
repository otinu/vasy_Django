import requests
from bs4 import BeautifulSoup

URL_PATTERN = "クックパッドのURL"

html_doc = requests.get("https://cookpad.com/search/%E3%81%98%E3%82%83%E3%81%8C%E3%81%84%E3%82%82").text
soup = BeautifulSoup(html_doc, 'html.parser')
titles = soup.select("html > body > div > div > div > div > div > div > section > main > section > ul > li > div > div > div > h2")
images = soup.select("html >body >div >div >div >div >div >div >section >main >section >ul >li")


"""
for (title, image) in zip(titles, images):
    try:
        
        print(title.a.text)
        print(image.a['href'])
        print(image.img['src'])
        print()

    except Exception as e:
        print(e)
        continue

"""


for (title, image) in zip(titles, images):
    try:
        text = title.a.text
        link = image.a['href']
        image = image.img['src']

        if text is not None and link is not None and image is not None:
            print(text)
            print(URL_PATTERN + link)
            print(image)
            print()
        else:
            raise(Exception)

    except Exception as e:
        # print("\n" + "例外発生" + "\n")
        continue
