import requests
from bs4 import BeautifulSoup


link = "https://www.nutrione.co.kr/goods/goods_view.php?goodsNo=1000000712&mtn=1%5E%7C%5E%EB%B2%A0%EC%8A%A4%ED%8A%B8%EC%83%81%ED%92%88%5E%7C%5En"
page = requests.get(link)

soup = BeautifulSoup(page.text, "html.parser")

item_detail_list = soup.find('div', {'class': 'item_detail_list'})
firstDl = item_detail_list.find('dl')
# firstDl = soup.find_all('dl')[0]


price = firstDl.find('strong')
price = price.get_text()
print(price)