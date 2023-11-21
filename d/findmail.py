import re

text = "123456@i.ru, 123_456@ru.name.ru, login@i.ru, логин-1@i.ru, login.3@i.ru, login.3-67@i.ru, 1login@ru.name.ru"
pattern = r"@([\w\.-]+)(\.[\w\.]+)"

if re.findall(pattern, text):
    print(text)
else:
    print("not found")