from lxml import html
import requests

joongangUniv = 'https://www.nutrione.co.kr/goods/goods_view.php?goodsNo=1000000712&mtn=1%5E%7C%5E%EB%B2%A0%EC%8A%A4%ED%8A%B8%EC%83%81%ED%92%88%5E%7C%5En'

response = requests.get(joongangUniv)

tree = html.fromstring(response.content)
russia = tree.xpath("/html/body/div[3]/div/div/div[1]/div[2]/form/div/div/div[2]/dl[2]/dd/strong/strong/text()")[0]
print(russia)

# /html/body/div[4]/div[2]/article/div[1]/p[2]/text()