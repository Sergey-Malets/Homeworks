a = int(input('Введите трехзначное число: '))
a = str(a)
itog = 0
for s in a:
    print (s)
    s = int (s)
    itog = itog + s
print("Сумма цифр вашего числа =",itog)

