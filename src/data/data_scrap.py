from bs4 import BeautifulSoup


def scrap_data(response):
    soup = BeautifulSoup(response.text, 'html.parser')

    symbol = soup.select_one("span.a-price-symbol")   
    price = soup.select_one("span.a-price-whole")

    symbol_text = symbol.get_text(strip=True)
    price_text = price.get_text(strip=True)

    return symbol_text, price_text

