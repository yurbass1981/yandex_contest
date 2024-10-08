# Кот нос ток сон клад рама вход книга вдох
# text = sorted(input().lower().split())

# for i in text:
#     for j in text:
#         if sorted(i) == sorted(j) and i != j:
#             text.remove(i)
#             text.remove(j)
#             print(i, j)
    

text = sorted(input().lower().split())
d = dict()
for word in text:
    d.setdefault(tuple(sorted(word)), []).append(word)
for val in d.values():
    if len(val) > 1:
        print(*val)
