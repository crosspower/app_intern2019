import requests
from bs4 import BeautifulSoup


def get_product_info(search_word):
    url = "https://search.rakuten.co.jp/search/mall/"
    
    html = requests.get(url+search_word).content
    soup = BeautifulSoup(html,'html.parser')

    result = []
    items = soup.select('.searchresultitem')
    for item in items:
        price_span = item.select_one('.price')
        if price_span:
            price = int(price_span.select_one('.important').get_text().replace(',','').replace('円',''))
            if not price:
                price = None
        else:
            price = None
        item.select_one('.title')
        result.append(dict(
            service_name = "rakuten",
            title = item.select_one('.title').get_text(),
            price = price,
            image = item.select_one('img')['src'],
            link = item.select_one('.title a')['href'],
            info = [],
            icon = "https://www.rakuten.co.jp/favicon.ico"
        ))
    return result