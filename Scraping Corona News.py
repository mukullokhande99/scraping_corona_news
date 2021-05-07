from bs4 import BeautifulSoup as soup
import requests
from datetime import date
today = date.today()
d = today.strftime("%m-%d-%y")
print("date =", d)


cnn_url="https://edition.cnn.com/world/live-news/coronavirus-pandemic-{}-intl/index.html".format(d)
cnn_url
html = requests.get(cnn_url)
bsobj = soup(html.content,'lxml')
bsobj
for link in bsobj.findAll("h2"):    
    print("Headline : {}".format(link.text))
for news in bsobj.findAll('article',{'class':'sc-jqCOkK sc-kfGgVZ hQCVkd'}):
    print(news.text.strip())


nbc_url='https://www.nbcnews.com/health/coronavirus'
r = requests.get('https://www.nbcnews.com/health/coronavirus')
b = soup(r.content,'lxml')
for news in b.findAll('h2'):
    print(news.text)

links = []
for news in b.findAll('h2',{'class':'teaseCard__headline'}):
    links.append(news.a['href'])    
links

for link in links:
    page = requests.get(link)
    bsobj = soup(page.content)
    for news in bsobj.findAll('div',{'class':'article-body__section article-body__last-section'}):
        print(news.text.strip())

