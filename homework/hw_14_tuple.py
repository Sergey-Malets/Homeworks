# Задача№2
#  Выведите статистику частности букв в кортеже
#  long_word = ( 'т', 'т', 'а', 'и', 'и', 'а', 'и’,
#  'и', 'и', 'т', 'т', 'а', 'и', 'и',
#  'и', 'и', 'и', 'т', 'и’)
#  Примечание: Статистика частности - число повторений каждой из букв.

long_word = ('т', 'т', 'а', 'и', 'и', 'а', 'и', 'и', 'и', 'т', 'т', 'а','d','d', 'и', 'и', 'и', 'и', 'и', 'т', 'и')
t=0
a=''
i=0
for j in long_word:
    if j in a:
        continue
    else:
        a= a+j
        x = long_word.count(j)
        print(f'Буква {j} повторяется {x} раз.')
print(a)

# for j in long_word:
#     if j=='т':
#         t +=1
#     elif j=='а':
#         a +=1
#     else:
#         i +=1
# print(f'т={t} раз, а={a} раз, и={i} раз')