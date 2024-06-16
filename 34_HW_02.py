# Напишите функцию highlight_keywords(text, keywords), 
# которая выделяет все вхождения заданных ключевых слов в тексте,
#  окружая их символами *. 
# Функция должна быть регистронезависимой при поиске ключевых слов.

import re

text = "This is a sample text. We need to highlight Python and programming."
keywords = ["python", "programming"]

def highlight_keywords(text, keywords):
    for i in keywords:
        words_fin = "".join(re.findall(i, text, re.IGNORECASE))
        text = re.sub(i, f'*{words_fin}*', text, flags=re.IGNORECASE)
    print(text)

highlight_keywords(text, keywords)
