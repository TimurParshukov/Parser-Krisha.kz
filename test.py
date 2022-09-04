import requests
from bs4 import BeautifulSoup

url = 'https://krisha.kz/complex/search/aktobe/?state[]=1&state[]=2'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes_price = soup.find_all('p', class_='complex-card__square-price')
quotes = soup.find_all('p', class_='complex-card__title')

for i in range(0, len(quotes)):
    print(quotes[i].text, quotes_price[i].text)
    #print(quotes_price[i].text)

