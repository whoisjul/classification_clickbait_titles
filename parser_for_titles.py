# -*- coding: utf-8 -*-
import collections
collections.Callable = collections.abc.Callable
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
from collections.abc import Callable
from time import sleep
import csv
file = open('non_clickbait_text', 'w', encoding='utf-8')
clickbait_sites = [
        'https://ria.ru/politics/',
        'https://ria.ru/society/',
        'https://ria.ru/science/',
        'https://ria.ru/culture/',
        'https://ria.ru/world/',
        'https://ria.ru/economy/',
        'https://ria.ru/religion/'
]
driver = webdriver.Chrome()

def get_titles_from_site(url):
    try:
        driver.get(url)
        for i in range(50):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(4)
        

        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        


        titles = [title.text.strip() for title in soup.find_all('h3', {"class":"list-item__title color-font-hover-only"})]

        return titles
    except Exception as e:
        print(f"Ошибка при обработке {url}: {e}")
        return []

counter = 0
for i in clickbait_sites:
  for title in get_titles_from_site(i):
    file.write(title+'\n')
    print(title)
    counter += 1

print(counter)

file.close()