# Написать программу для сжатия строки, в которой алгоритм работает следующим образом: 
# string = 'xxxxtttсyyaaa' преобразуется в 'x4t3с1y2a3', то есть последовательность 
# одинаковых символов строки заменяется на этот символ и количество его повторений 
# в текущей позиции строки.


# text = 'xxxxtttсyyaaattt'
# d = dict()

# for i in text:
#     count = text.count(i)
#     d[i] = count
# rezult = ''.join(f'{k}{v}' for k, v in d.items())
# print(rezult)

text = 'xxxxtttсyyaaattt'
rez = '' 
while len(text): 
    rez += text[0] + str(len(text) - len(text.lstrip(text[0]))) 
    text = text.lstrip(text[0]) 
print(rez)







