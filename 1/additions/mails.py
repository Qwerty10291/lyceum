import re
output = []
mails = {}

# с помощью регулярных выражений ищем количество адресов
for i in range(int(input())):
    text = input()
    if not re.search(r'\d', text):
        mails[re.split(r'@', text)[0]] = 0
    else:
        mails[re.split(r'\d@', text)[0]] += 1

# создаём новые адреса
for i in range(int(input())):
    text = input()
    if text in mails:
        mails[text] += 1
        output.append(f'{text}{mails[text]}@untitled.py')
    else:
        output.append(f'{text}@untitled.py')
[print(i) for i in output]
