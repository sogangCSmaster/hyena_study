import requests
import json

# query = input("검색할 블로그 글을 입력하세요: ")
url = "https://openapi.naver.com/v1/search/blog?query=콜라겐&display=100&sort=date"

print(url)

# 인증과정
headers = {'X-Naver-Client-Id': 'ziyGV0xl5Xal6ACOl3k0', 'X-Naver-Client-Secret': 'P0T11CRz7i'}

response = requests.get(url, headers=headers)
data = response.json()
items = data['items']

for item in items:
    print(item['title'])