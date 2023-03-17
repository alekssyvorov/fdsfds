import requests
from bs4 import BeautifulSoup
import lxml
import time

for j in range(1, 5):
    url = f"https://allo.ua/ua/zarjadnye-stancii/p-{j}/"

    header = {'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}

    response = requests.get(url, headers=header)
    soup = BeautifulSoup(response.text, 'lxml')

    all_product = soup.find('div', class_='products-layout__container products-layout--grid')
    products = all_product.find_all('div', class_='product-card')
    for i in range(len(products)):
        title = products[i].find('a', class_='product-card__title')
        price = products[i].find('div', class_='v-pb')
        print(title.text)
        print(price.text)
    time.sleep(5)
    print('Страница', j)

