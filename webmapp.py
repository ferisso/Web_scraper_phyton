import requests
from bs4 import BeautifulSoup

url = 'https://www.amazon.com.br/s?k=notebook&__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2SIBC2QV14PV&sprefix=noteb%2Caps%2C274&ref=nb_sb_ss_i_1_5'
headers = {
    "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
}
pagina = requests.get(url, headers = headers)
soup = BeautifulSoup(pagina.content, 'html.parser')
notebook_price = soup.find('span',class_ = 'a-price-whole').get_text()
input_price = float(input('> '))
maximum_price = input_price / 1000
new_notebook_price = float(notebook_price[0:5])
if new_notebook_price > maximum_price:
    print("Don't Buy it")
else:
    print('Buy it')

print(new_notebook_price)