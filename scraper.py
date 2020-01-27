import requests
from bs4 import BeautifulSoup

url = 'https://www.amazon.com.br/Monitor-LG-25UM58-P-AWZ-LED-25/dp/B01AWG4S4K/ref=lp_16364756011_1_1?s=computers&ie=UTF8&qid=1580095560&sr=1-1'
headers = {
    "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
}
page = requests.get(url, headers = headers)
soup = BeautifulSoup(page.content, 'html.parser')
title = soup.find(id = "productTitle").get_text()
price = soup.find(id="priceblock_ourprice").get_text()

print(title.strip())
print(price.strip())