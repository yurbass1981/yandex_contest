# Строка считается действительной, если все символы в строке встречаются одинаковое количество раз. 
# Также допустимо, если для выполнения этого условия будет достаточно удалить 1 символ из строки. 
# Напишите функцию, которая возвращает True, если строка действительна и False, если нет.
from collections import Counter

def is_string(text):
    x = Counter(text)
    elements = x.values()
    lst = []
    
    for i in elements:
        lst.append(i)
    if sum(lst) // min(lst) == len(lst):
        return True
    elif sum(lst) - 1 // min(lst) == len(lst):
        return True
    else:
        return False


rezult = is_string(input())
print(rezult)

    

        


