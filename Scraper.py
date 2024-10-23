import requests
from bs4 import BeautifulSoup
import random

def scrapeWikiArticle(url):
    responce = requests.get(url=url)
    soup = BeautifulSoup(responce.text, 'html.parser')

    title = soup.find(id="firstHeading")
    print(title.string)

    allLinks = soup.find(id="bodyContent").find_all('a')
    random.shuffle(allLinks)
    linkToScrape = 0

    for link in allLinks:
        if link['href'].find('/wiki/') == -1:
            continue
        linkToScrape = link
        break

    if linkToScrape == 0:
        print("No suitable link found.")
        return
    scrapeWikiArticle("https://en.wikipedia.org" + linkToScrape['href'])

scrapeWikiArticle('https://en.wikipedia.org/wiki/Web_scraping')