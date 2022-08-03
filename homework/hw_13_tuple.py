# Задача№1
# Создайте кортеж с цифрами от 0 до 9 и посчитайте сумму
import random
a = [random.randint(0,9) for i in range(10)]
a = tuple(a)
print(a)
print(sum(a))
