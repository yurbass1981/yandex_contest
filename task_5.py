# Создайте функцию, которая принимает переменное количество аргументов и находит среднее арифметическое ненулевых из них.

def my_func(*args):
    count = len(args)
    for a in args:
        if len(args) > 1 and a == 0:
            count -= 1
    rezult = sum(args) / count
    if rezult % 1 == 0:
        return int(rezult)
    else:
        return rezult


num = my_func(0)
print(num)