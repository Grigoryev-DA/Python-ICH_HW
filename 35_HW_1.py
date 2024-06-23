# 1. Напишите функцию get_response(url), которая отправляет GET-запрос по заданному
# URL-адресу и возвращает объект ответа. Затем выведите следующую информацию об
# ответе:
# - Код состояния (status code)
# - Текст ответа (response text)
# - Заголовки ответа (response headers)
# Пример использования:
# url = "https://api.example.com"
# response = get_response(url)
# print("Status Code:", response.status_code)
# print("Response Text:", response.text)
# print("Response Headers:", response.headers)

import requests
import re

def get_response(url):
    response = requests.get(url)
    print(response.status_code)  # статус
    print(response.headers)      # заголовки ответа

    texts = response.text        # текст страницы

    text_new = ''
    for teg in texts.split('\n'):
        if teg.startswith('<p>'):
            text_new += teg

    links = re.findall(r'<a\s.+?>.*?<\/a>', text_new)    # пробую очистить код от ссылок

    for link in links:                                          # циклом сохраняю ключевое слово в ссылке
        worts = re.findall(r'>\D{1,}<', link)
        text_new = re.sub(r'<a\s.+?>.*?<\/a>', str(worts), text_new, count=1)

    text_new = re.sub(r'<\S{1,5}>', "", text_new)       # двумя паттернами пытаюсь немного очистить текст
    text_new = re.sub(r'[\[\]\'\<\>]', "", text_new)
    print(text_new)

get_response('https://de.wikipedia.org/wiki/Amtshauptmannschaft_Fl%C3%B6ha')
