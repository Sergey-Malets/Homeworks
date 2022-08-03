#Напишите рекурсивную функцию, которая осуществляет суммирование чисел в списке.
# Список должен быть сгенерирован из 10 чисел, каждое в диапазоне от 1 до 100

import random
a = [random.randint (1,100) for i in range(10)]
print(a)

q=0
for i in a:
    q+=i
print(q) #проверка


def sum_ten(n):
    s = 0
    if n!=0:
        s = s + a[n - 1]+sum_ten(n-1)
        return s
    else:
        return 0
print(sum_ten(len(a)))

    