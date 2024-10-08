# Веб-сайт требует, чтобы пользователи вводили пароль для регистрации, соответствующий определенным требованиям. 
# Напишите программу для проверки правильности ввода пароля пользователями.
# Ниже приведены критерии проверки пароля:
# 1. Минимум 1 буква латинского алфавита в нижнем регистре [az]
# 2. Минимум 1 число от [0–9]
# 3. Минимум 1 буква латинского алфавита в верхнем регистре [AZ]
# 4. Минимум 1 специальный символ
# 5. Минимальная длина пароля : 6
# 6. Максимальная длина пароля: 12
# Программа должна возвращать True или False.

import re

def true_password(password):
    flag = 0
    while True:
        if (len(password) < 6 and len(password) > 12):
            flag = -1
            break
        elif not re.search('[a-z]', password):
            flag = -1
            break
        elif not re.search('[A-Z]', password):
            flag = -1
            break
        elif not re.search('[0-9]', password):
            flag = -1
            break
        elif not re.search('[@_!$%^&*()<>?/\|}{~:#]', password):
            flag = -1
            break
        elif re.search("\s" , password):
            flag = -1
            break
        else:
            flag = 0
            return True
            break

    if flag == -1:
        return False
    
          

password = true_password('Pass10wrd!')
print(password)