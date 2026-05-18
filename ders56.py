import requests
from bs4 import BeautifulSoup

url="https://www.trendyol.com/"
res=requests.get(url)
soup=BeautifulSoup(res.text,"html.parser")
print(soup.title.text)
