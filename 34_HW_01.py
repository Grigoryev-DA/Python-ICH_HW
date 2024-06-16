import re

with open('emails_hw.txt', 'r', encoding="utf-8") as file:
    text = file.read()

text_HW = re.findall("\S{1,}@\w{1,}\.\w{2,}", text)
print(text_HW)


