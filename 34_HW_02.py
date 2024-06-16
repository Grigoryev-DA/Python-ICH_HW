import re

text = "This is a sample text. We need to highlight Python and programming."
keywords = ["python", "programming"]

def highlight_keywords(text, keywords):
    for i in keywords:
        words_fin = "".join(re.findall(i, text, re.IGNORECASE))
        text = re.sub(i, f'*{words_fin}*', text, flags=re.IGNORECASE)
    print(text)


highlight_keywords(text, keywords)