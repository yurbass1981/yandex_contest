# print('Введите четырёхзначное число: ')
# num = int(input ())

# a = num // 1000
# b = num // 100 % 10
# c = num // 10 % 10
# d = num % 10

# first_didgit, second_didgit, third_digit, fourth_digit = a, b, c, d

# if a <= b and b <= c and c <= d:
#     first_didgit, second_didgit, third_digit, fourth_digit = a, b, c, d
# elif a <= b and b <= d and d <= c:
#     first_didgit, second_didgit, third_digit, fourth_digit = a, b, d, c
# elif a <= c and c <= b and b <= d:
#     first_didgit, second_didgit, third_digit, fourth_digit = a, c, b, d
# elif a <= c and c <= d and d <= b:
#     first_didgit, second_didgit, third_digit, fourth_digit = a, c, d, b
# elif a <= d and d <= b and b <= c:
#     first_didgit, second_didgit, third_digit, fourth_digit = a, d, b, c
# elif a <= d and d <= c and c <= b:
#     first_didgit, second_didgit, third_digit, fourth_digit = a, d, c, b

# elif b <= a and a <= c and c <= d:
#     first_didgit, second_didgit, third_digit, fourth_digit = b, a, c, d
# elif b <= a and a <= d and d <= c:
#     first_didgit, second_didgit, third_digit, fourth_digit = b, a, d, c
# elif b <= c and c <= a and a <= d:
#     first_didgit, second_didgit, third_digit, fourth_digit = b, c, a, d
# elif b <= c and c <= d and d <= a:
#     first_didgit, second_didgit, third_digit, fourth_digit = b, c, d, a
# elif b <= d and d <= a and a <= c:
#     first_didgit, second_didgit, third_digit, fourth_digit = b, d, a, c
# elif b <= d and d <= c and c <= a:
#     first_didgit, second_didgit, third_digit, fourth_digit = b, d, c, a

# elif c <= a and a <= b and b <= d:
#     first_didgit, second_didgit, third_digit, fourth_digit = c, a, b, d
# elif c <= a and a <= d and d <= b:
#     first_didgit, second_didgit, third_digit, fourth_digit = c, a, d, b
# elif c <= b and b <= a and a <= d:
#     first_didgit, second_didgit, third_digit, fourth_digit = c, b, a, d
# elif c <= b and b <= d and d <= a:
#     first_didgit, second_didgit, third_digit, fourth_digit = c, b, d, a
# elif c <= d and d <= a and a <= b:
#     first_didgit, second_didgit, third_digit, fourth_digit = c, d, a, b
# elif c <= d and d <= b and b <= a:
#     first_didgit, second_didgit, third_digit, fourth_digit = c, d, b, a

# elif d <= a and a <= b and b <= c:
#     first_didgit, second_didgit, third_digit, fourth_digit = d, a, b, c
# elif d <= a and a <= c and c <= b:
#     first_didgit, second_didgit, third_digit, fourth_digit = d, a, c, b
# elif d <= b and b <= a and a <= c:
#     first_didgit, second_didgit, third_digit, fourth_digit = d, b, a, c
# elif d <= b and b <= c and c <= a:
#     first_didgit, second_didgit, third_digit, fourth_digit = d, b, c, a
# elif d <= c and c <= a and a <= b:
#     first_didgit, second_didgit, third_digit, fourth_digit = d, c, a, b
# elif d <= c and c <= b and b <= a:
#     first_didgit, second_didgit, third_digit, fourth_digit = d, c, b, a

# if first_didgit == 0 and second_didgit > 0:
#     first_didgit, second_didgit = second_didgit, first_didgit
# elif first_didgit == 0 and second_didgit == 0 and third_digit > 0:
#     first_didgit, third_digit = third_digit, first_didgit
# elif first_didgit == 0 and second_didgit == 0 and third_digit == 0:
#     first_didgit, fourth_digit = fourth_digit, first_didgit


# result = (first_didgit * 1000) + (second_didgit * 100) + (third_digit * 10) + (fourth_digit * 1)
# print(first_didgit, second_didgit, third_digit, fourth_digit, sep='')

print('Введите четырёхзначное число: ')
num = int(input ())

a = num // 1000
b = num // 100 % 10
c = num // 10 % 10
d = num % 10

if a > b:
    a, b = b, a 
if c > d:
    c, d = d, c 
if a > c:
    a, c = c, a 
if b > d:
    b, d = d, b 
if b > c:
    b, c = c, b
    
if a == 0 and b > 0:
    a, b = b, a
elif a == 0 and b == 0 and c > 0:
    a, c = c, a
elif a == 0 and b == 0 and c == 0:
    a, d = d, a
    
print(a, b, c, d, sep='')