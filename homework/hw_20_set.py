#Задача№1
#Проверить, есть ли в последовательности чисел списка дубликаты.

#a = [1,234,546,3,22,1,2,2,3345,2,11,1,234]
a = input('Введите список чисел через пробел:')
a = a.split()
b = set(a)
print(a)
print(b)

if len(a)>len(b):
    print("В списке есть дубликаты чисел")
else:
    print("В списке нет дубликатов чисел")