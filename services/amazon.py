import requests
from bs4 import BeautifulSoup


def get_product_info(search_word):
    url = "https://www.amazon.co.jp/s?k="
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
    html = requests.get(url+search_word,headers=headers).content
    soup = BeautifulSoup(html,'html.parser')
    
    result = []
    items = soup.select('.s-result-item')
    for item in items:
        price = None
        price_span = item.select_one('.a-price-whole')
        if price_span:
            price = int(price_span.get_text().replace(',',''))
            if not price:
                price = None

        result.append(dict(
            service_name = "amazon",
            title = item.select_one('h2').get_text(),
            price = price,
            image = item.select_one('img')['src'],
            link = "https://www.amazon.co.jp"+item.select_one('h2 a')['href'],
            info = [],
            icon = "https://www.amazon.co.jp/favicon.ico"
        ))
    return result
