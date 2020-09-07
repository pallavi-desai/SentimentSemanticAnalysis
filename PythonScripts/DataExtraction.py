import requests
import json

everything_news_url = 'https://newsapi.org/v2/everything'
everything_payload = {
    'q': 'Canada OR University OR Dalhousie University OR Halifax OR Canada Education OR Moncton OR Toronto',
    'language': 'en',
    'pageSize': 100}
headers = {'Authorization': '234c17b6582f4e8c87f30dc403bea5e8'}

response = requests.get(url=everything_news_url, headers=headers, params=everything_payload).json()
article = response['articles']

with open('data1.json', 'w') as outputFile:
    json.dump(article, outputFile)
