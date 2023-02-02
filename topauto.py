import requests as rq
from bs4 import BeautifulSoup as bs


def parser():
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    
    url = f'https://baza-gai.com.ua'
    r = rq.get(url, headers=headers)
    html = bs(r.content, 'html.parser')

    return html




all = parser().find_all('li', class_="list-item px-1")

all_cars = []
for i in range(50):
    all_cars.append(all[i].text)

all_cars_out = []
for i in range(50):
    all_cars_edit = all_cars[i].splitlines()

    all_cars_edit = all_cars_edit[1].strip() + ' ' + all_cars_edit[3].strip()

    out = f'{i+1}: {all_cars_edit}'

    all_cars_out.append(out)






