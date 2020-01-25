import requests
from bs4 import BeautifulSoup

url = 'https://www.amazon.com.br/Smartwatch-Xiaomi-Preto-Original-Lacrado/dp/B07SNG23JW/ref=sr_1_1?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=JHDJAZ33OSC4&keywords=mi+nand+4&qid=1579994931&sprefix=mi+namd%2Caps%2C303&sr=8-1'
headers = {
    "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
}
page = requests.get(url, headers = headers)

soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify())