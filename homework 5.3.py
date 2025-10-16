import re

text = input("Введите строку: ").strip()
words = re.findall(r"\w+", text, flags=re.UNICODE)
capitalized = (w[:1].upper() + w[1:].lower() for w in words if w)
core = "".join(capitalized)

if not core:
    print("")
else:
    hashtag = "#" + core
    if len(hashtag) > 140:
        hashtag = hashtag[:140]
    print(hashtag)