import re

with open('emails_hw.txt', 'r', encoding="utf-8") as file:
    text = file.read()

text_HW = re.findall("\S{1,}@\w{1,}\.\w{2,}", text)         # не менее 1 любого непробельного символа, @, не менне 1 буквы или цифры, ".", не менне 2 букв или цифер
print(text_HW)


