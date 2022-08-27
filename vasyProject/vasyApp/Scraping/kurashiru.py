import requests
from bs4 import BeautifulSoup
import time

URL_PATTERN = "https://www.kurashiru.com"

html_doc = requests.get("https://www.kurashiru.com/search?query=%E3%81%98%E3%82%83%E3%81%8C%E3%81%84%E3%82%82").text
soup = BeautifulSoup(html_doc, 'html.parser')

# imgタグのalt値からタイトルも取得
titles_images = soup.select("html > body > div > section > div > div > div > div > div > ul > li > div > a > div > div > noscript")
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
        
    except Exception as e:
        print(e)
        continue

# なぜか、10番目以降が取得できない。prettify()でチラッと見た感じでは、<noscript>というタグで囲まれていた。
# ⇒ただし、20番目あたりの話。9番目より上を見たくともコンソールに出力しきれなかった。
# 　⇒ここの問題が解決すれば、10番目以降も取得できると思うが、今はそこまで多くのデータ取得をすることが目的ではない。
#     ⇒後々、「もっと多くの件数を出力させたい」という場面がきた際に、再度検討。