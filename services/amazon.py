import requests
from bs4 import BeautifulSoup


def scrape(word):
    url = "https://www.amazon.co.jp/s?k="

    html = requests.get(url+word).content
    soup = BeautifulSoup(html,'html.parser')
    
    result = []
    for item in soup.select('.s-result-item'):
        price = 0
        price_span = item.select_one('.a-price-whole')
        if price_span:
            price = int(price_span.get_text().replace(',',''))

        result.append(dict(
            title = item.select_one('h2').get_text(),
            price = price,
            image = item.select_one('img')['src'],
            link = "",
            info = []
        ))
    return result
