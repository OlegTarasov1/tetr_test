# https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту
from bs4 import BeautifulSoup
import requests
import lxml
import csv

def run():

    base_url = 'https://ru.wikipedia.org'
    url = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'

    RUS = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЭЮЯ-'
    result = {}
    final = False

    while not final:
        
        src = requests.get(url, headers={'Accept': '*/*'})
        soup = BeautifulSoup(src.text, 'lxml')

        id_with_li =soup.find('div', id = 'mw-pages')
        final_id_with_lis = id_with_li.find('div', class_='mw-category-group')
        for i in final_id_with_lis.find_all('li'):
            if not i.text.strip()[0] in RUS:
                final = True
                break
            else:
                pass
            try:
                result[i.text.strip()[0]] += 1
            except:
                result[i.text.strip()[0]] = 1
                

        next_page = base_url + id_with_li.find('a', string = 'Следующая страница')['href']
        url = next_page


    with open('beasts.csv', 'w', encoding = 'utf-8') as file:
        writer = csv.writer(file)
        for i, value in result.items():
            writer.writerow([i, value])
