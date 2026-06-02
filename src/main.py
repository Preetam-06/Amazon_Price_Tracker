from auth.authorize import *
from data.data_scrap import *
import sys

sys.stdout.reconfigure(encoding="utf-8")

target_url = "https://www.amazon.in/ASUS-Gaming-4050-6GB-Windows-V3607VU-RP550WS/dp/B0F5N2ZK2S/ref=sr_1_3?crid=2MG1XGDJWL3E3&dib=eyJ2IjoiMSJ9.v-8tXo_ZG24RCQAiFaVVbSfILC6sLWArGLbWfhBnWuqqMKZXXKhcLWk7UGbXscjktXq7kZjIbqGLxv30LRkXTrhB6jA3ShvBv9yim-YnU0pzWr6ukmO5V0rYIOPuQ9WZPh87k3zNtVr380t1-WKaVwEmoxR7OLd8pONr-5K3hg3Lq9XDEHIfJ_n091Z658corNkaN2VVhRLTg7yBqfiQ3fJM3g_uFt6h9NzgxJKQiJM08Ano-O5lMPF92ga2v0OutWDIwQiS5sqXjfmuQ1SHSeFtoaH5Zan5ilBwTouvA5o.Eqwwy9P_RuyIxpo5dFxCz_8NdhE73P1p4O-Qc_K91FI&dib_tag=se&keywords=asus%2Bgaming%2Bv16&qid=1780421918&s=computers&sprefix=asus%2Bv16%2Ccomputers%2C334&sr=1-3&th=1"

target = (input("Enter the Product "))
target_price = float(input(f"Enter the {target} target price: "))

if __name__ == "__main__":

    response = get_page_content(target_url)
    symbol_text, price_text = scrap_data(response)

    symbol = symbol_text
    price = float(price_text.replace(',', ''))

    print(f"Amazon Current Price is {symbol}{price} ")
    if target_price >= price:
        print(f"The price of {target} is below the target price. Consider purchasing now. \nAmazon Link : http://www.amazon.in/")
