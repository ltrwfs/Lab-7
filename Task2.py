import requests
import json


API_key = 'd711e9230c1d45a1b0e964a0c53afade'
question = 'Russia'    # Новостной запрос
date = '2025-03-14'    # Дата новости
filter = 'popularity'    # Способ сортировки новостей


def get_news(question, date, filter):
    URL = (f'https://newsapi.org/v2/everything?'
           +f'q={question}&from={date}&sortBy={filter}&apiKey={API_key}')
    response = requests.get(URL)
    inf = json.loads(response.text)
    return inf


def output(data):
    print(f'Total number of news by request "{question}" from {date} '
          +f'is {data['totalResults']}. There is the first most popular one '
          +f'(source: {data['articles'][0]['source']['name']}):\n')
    print(f'Title: {data['articles'][0]['title']}')
    print(f'Description: {data['articles'][0]['description']}')
    print(f'To read more visit: {data['articles'][0]['url']}')


if __name__ == "__main__":
    data = get_news(question, date, filter)
    output(data)