#Напиши программу, которая вычисляет квадраты чисел от 1 до 10 (использовать цикл while)
a = 1
result=''
while a<=10:
    a2=a**2
    result = result + ',' + str(a2)
    a = a+1
else:
    print(result)