en = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
      "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
ru = ["А", "Б", "В", "Г", "Д", "Е", "Ё", "Ж", "З", "И", "Й", "К", "Л", "М", "Н", "О",
      "П", "Р", "С", "Т", "У", "Ф", "Х", "Ц", "Ч", "Ш", "Щ", "Ъ", "Ы", "Ь", "Э", "Ю", "Я"]

text = input()
num = int(input())
first = ''
second = ''
for i in text:
    try:
        first += en[en.index(i) - num]
        second += en[en.index(i) + num]
    except ValueError:
        first += ru[ru.index(i) - num]
        second += ru[ru.index(i) + num]
print(first, text, second, sep='\n')
