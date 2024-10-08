# Для строки вывести статистику по количеству входящих в нее символов (без учета регистра), 
# сортируя по алфавиту. Игнорируйте всё, кроме букв латиницы и кириллицы. 
# Вывод: символ, пробел, количество. Приоритет вывода у латиницы, вывод символов в нижнем регистре.

import string as s

text = 'Hello 123 ** hello мама'.lower()
d = dict()

symbols = s.punctuation + s.digits + ' '

for i in symbols:
    if i in text:
        text = text.replace(i, '')

sorted_text = sorted(text)

for i in sorted_text:
    count = sorted_text.count(i)
    d[i] = count
    
for k, v in d.items():
    print(k, v)