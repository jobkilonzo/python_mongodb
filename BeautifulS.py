from bs4 import BeautifulSoup
import requests

req = requests.get("https://www.jumia.co.ke/mlp-hisense-store/")

soup = BeautifulSoup(req.text, 'lxml')

# names = soup.find_all("div", {"class": "name"})
prices = soup.find_all("div", {"class": "prc"}, "h3", {"class": "name"})
for name in prices:
    print(name.text)
